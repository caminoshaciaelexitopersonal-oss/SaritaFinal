from rest_framework import viewsets, permissions
from .models import KitchenStation, MenuItemDetail, RestaurantTable
from .serializers import KitchenStationSerializer, MenuItemDetailSerializer, RestaurantTableSerializer

class KitchenStationViewSet(viewsets.ModelViewSet):
    serializer_class = KitchenStationSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return KitchenStation.objects.filter(provider=self.request.user.perfil_prestador)

class MenuItemDetailViewSet(viewsets.ModelViewSet):
    serializer_class = MenuItemDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        # MenuItemDetail se vincula vía Product, filtramos por el proveedor del producto
        return MenuItemDetail.objects.filter(product__provider=self.request.user.perfil_prestador)

class RestaurantTableViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantTableSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return RestaurantTable.objects.filter(provider=self.request.user.perfil_prestador)
