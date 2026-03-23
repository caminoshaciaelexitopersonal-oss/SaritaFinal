from decimal import Decimal
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    SocialConversation,
    SocialConversationMember,
    SocialMessage,
    SocialProfilePreference,
    SocialGiftCatalog,
    SocialGiftTransaction,
)
from .serializers import (
    SocialConversationSerializer,
    SocialConversationMemberSerializer,
    SocialMessageSerializer,
    SocialProfilePreferenceSerializer,
    SocialGiftCatalogSerializer,
    SocialGiftTransactionSerializer,
    SendGiftSerializer,
)

User = get_user_model()


class IsConversationMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, SocialConversation):
            return obj.memberships.filter(user=request.user).exists()
        if isinstance(obj, SocialMessage):
            return obj.conversation.memberships.filter(user=request.user).exists()
        return True


class SocialConversationViewSet(viewsets.ModelViewSet):
    serializer_class = SocialConversationSerializer
    permission_classes = [permissions.IsAuthenticated, IsConversationMember]

    def get_queryset(self):
        return SocialConversation.objects.filter(memberships__user=self.request.user).distinct()

    def perform_create(self, serializer):
        conversation = serializer.save(created_by=self.request.user)
        SocialConversationMember.objects.get_or_create(
            conversation=conversation,
            user=self.request.user,
            defaults={"is_admin": True},
        )

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated, IsConversationMember])
    def add_member(self, request, pk=None):
        conversation = self.get_object()
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({"detail": "user_id es requerido"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"detail": "Usuario no existe"}, status=status.HTTP_404_NOT_FOUND)

        membership, created = SocialConversationMember.objects.get_or_create(conversation=conversation, user=user)
        serializer = SocialConversationMemberSerializer(membership)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


class SocialMessageViewSet(viewsets.ModelViewSet):
    serializer_class = SocialMessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsConversationMember]

    def get_queryset(self):
        queryset = SocialMessage.objects.filter(conversation__memberships__user=self.request.user).distinct()
        conversation_id = self.request.query_params.get("conversation_id")
        if conversation_id:
            queryset = queryset.filter(conversation_id=conversation_id)
        return queryset

    def perform_create(self, serializer):
        conversation = serializer.validated_data["conversation"]
        if not conversation.memberships.filter(user=self.request.user).exists():
            raise permissions.PermissionDenied("No perteneces a esta conversación")
        serializer.save(sender=self.request.user)


class SocialProfilePreferenceViewSet(viewsets.ModelViewSet):
    serializer_class = SocialProfilePreferenceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SocialProfilePreference.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=["patch"], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        preference, _ = SocialProfilePreference.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(preference, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], permission_classes=[permissions.IsAuthenticated])
    def suggestions(self, request):
        my_pref = SocialProfilePreference.objects.filter(user=request.user).first()
        if not my_pref:
            return Response([], status=status.HTTP_200_OK)

        interests = my_pref.interests or []
        qs = SocialProfilePreference.objects.filter(visibility_enabled=True).exclude(user=request.user)
        if interests:
            qs = qs.filter(interests__overlap=interests)[:20]

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class SocialGiftCatalogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SocialGiftCatalogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SocialGiftCatalog.objects.filter(active=True)


class SocialGiftTransactionViewSet(viewsets.ModelViewSet):
    serializer_class = SocialGiftTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SocialGiftTransaction.objects.filter(sender=self.request.user) | SocialGiftTransaction.objects.filter(
            receiver=self.request.user
        )

    def get_serializer_class(self):
        if self.action in ["create", "send_gift"]:
            return SendGiftSerializer
        return SocialGiftTransactionSerializer

    def create(self, request, *args, **kwargs):
        return self._send_gift(request)

    @action(
        detail=False,
        methods=["post"],
        permission_classes=[permissions.IsAuthenticated],
        serializer_class=SendGiftSerializer,
    )
    def send_gift(self, request):
        return self._send_gift(request)

    def _send_gift(self, request):
        serializer = SendGiftSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        receiver_id = serializer.validated_data["receiver_id"]
        gift_id = serializer.validated_data["gift_id"]
        conversation_id = serializer.validated_data.get("conversation_id")

        try:
            receiver = User.objects.get(id=receiver_id)
            gift = SocialGiftCatalog.objects.get(id=gift_id, active=True)
        except User.DoesNotExist:
            return Response({"detail": "Receptor no existe"}, status=status.HTTP_404_NOT_FOUND)
        except SocialGiftCatalog.DoesNotExist:
            return Response({"detail": "Gift no existe o no está activo"}, status=status.HTTP_404_NOT_FOUND)

        tx = SocialGiftTransaction.objects.create(
            sender=request.user,
            receiver=receiver,
            gift=gift,
            conversation_id=conversation_id,
            amount=Decimal(gift.price),
            status=SocialGiftTransaction.TransactionStatus.COMPLETED,
            external_reference=f"SOCIAL-GIFT-{timezone.now().timestamp()}",
            processed_at=timezone.now(),
        )
        return Response(SocialGiftTransactionSerializer(tx).data, status=status.HTTP_201_CREATED)
