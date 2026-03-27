from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from ..services.identity_protection import IdentityProtectionService

class IdentityProtectionViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'], url_path='verify-phone')
    def verify_phone(self, request):
        phone = request.data.get('phone')
        otp = request.data.get('otp')
        if not phone or not otp:
            return Response({"error": "phone and otp are required"}, status=400)

        success = IdentityProtectionService.verify_phone_otp(request.user, phone, otp)
        if success:
            return Response({"status": "verified", "message": "Teléfono validado correctamente."})
        return Response({"error": "Código OTP inválido."}, status=400)

    @action(detail=False, methods=['post'], url_path='verify-face')
    def verify_face(self, request):
        image_data = request.data.get('image')
        if not image_data:
            return Response({"error": "image data is required"}, status=400)

        success = IdentityProtectionService.verify_face_biometry(request.user, image_data)
        if success:
            return Response({"status": "verified", "message": "Rostro validado exitosamente."})
        return Response({"error": "No se pudo validar el rostro. Intente nuevamente."}, status=400)

    @action(detail=False, methods=['get'], url_path='status')
    def get_status(self, request):
        return Response({
            "phone_verified": request.user.phone_verified,
            "face_verified": request.user.face_verified,
            "verification_status": request.user.verification_status,
            "is_protected": IdentityProtectionService.is_user_protected(request.user)
        })
