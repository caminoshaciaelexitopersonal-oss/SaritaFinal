from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.apps import apps
from . import serializers

Account = apps.get_model('core_erp', 'Account')

class PlanCuentaViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = serializers.PlanCuentaSerializer  # Import from serializers
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code', 'type', 'is_active']

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(tenant=self.request.tenant)

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.tenant)

    @action(detail=False, methods=['get'])
    def tree(self, request):
        # Hierarchical tree
        accounts = self.get_queryset().select_related('parent_account')
        # Build tree logic here (recursive/dict)
        tree = self.build_tree(accounts)
        return Response(tree)

    def build_tree(self, accounts):
        # Simple tree builder
        account_dict = {a.id: a for a in accounts}
        roots = []
        for acc in accounts:
            if acc.parent_account_id:
                parent = account_dict.get(acc.parent_account_id)
                if parent:
                    if not hasattr(parent, 'children'):
                        parent.children = []
                    parent.children.append(acc)
            else:
                roots.append(acc)
        return [self.serialize_tree(acc) for acc in roots]

    def serialize_tree(self, acc):
        data = self.serializer_class(acc).data
        if hasattr(acc, 'children'):
            data['children'] = [self.serialize_tree(child) for child in acc.children]
        return data

