from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SocialConversationViewSet,
    SocialMessageViewSet,
    SocialProfilePreferenceViewSet,
    SocialGiftCatalogViewSet,
    SocialGiftTransactionViewSet,
)
from .api.protection_views import IdentityProtectionViewSet

router = DefaultRouter()
router.register(r"conversations", SocialConversationViewSet, basename="social-conversation")
router.register(r"messages", SocialMessageViewSet, basename="social-message")
router.register(r"preferences", SocialProfilePreferenceViewSet, basename="social-preference")
router.register(r"gift-catalog", SocialGiftCatalogViewSet, basename="social-gift-catalog")
router.register(r"gift-transactions", SocialGiftTransactionViewSet, basename="social-gift-transaction")
router.register(r"protection", IdentityProtectionViewSet, basename="social-protection")

urlpatterns = [
    path("", include(router.urls)),
]
