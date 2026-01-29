import os
import django
import sys
from unittest.mock import MagicMock, patch

# Configurar el entorno de Django
sys.path.append('/workspace/backend')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

from api.models import CustomUser
from apps.sadi_agent.voice_orchestrator import VoiceOrchestrator
from apps.sadi_agent.semantic_engine import SemanticEngine
from apps.sadi_agent.voice_providers import WhisperProvider, OpenAITTSProvider
from apps.sadi_agent.translation_service import TranslationService

def test_full_voice_operation_cycle():
    print("--- Probando Ciclo de Operación 100% por Voz ---")

    # 1. Mocks de servicios externos
    stt = MagicMock()
    stt.transcribe.return_value = ("Sarita, crea un comprobante contable por quinientos mil pesos", "es")

    tts = MagicMock()

    # Simular detección del Intent Engine
    from apps.sadi_agent.models import Intent
    intent = Intent.objects.filter(name='ERP_CREATE_VOUCHER').first()

    semantic = SemanticEngine()
    semantic.interpret = MagicMock(return_value=(
        intent,
        {"valor": 500000},
        {
            "actor": "super_admin",
            "domain_name": "contable",
            "intent_name": "ERP_CREATE_VOUCHER",
            "accion": "crear",
            "entidad": "comprobante",
            "parameters": {"valor": 500000}
        }
    ))

    translation = TranslationService()

    # 2. Orquestador de Voz
    orchestrator = VoiceOrchestrator(stt, tts, semantic, translation)

    # 3. Usuario Admin
    admin = CustomUser.objects.filter(is_superuser=True).first()

    # 4. Mock de la API de Agentes para verificar la directiva
    import uuid
    valid_mission_id = str(uuid.uuid4())
    with patch('requests.post') as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 202
        mock_response.json.return_value = {"mission_id": valid_mission_id}
        mock_post.return_value = mock_response

        with patch.object(VoiceOrchestrator, '_poll_mission_status') as mock_poll:
            mock_poll.return_value = {
                "estado": "COMPLETADA",
                "reporte_final": {"status": "SUCCESS", "message": "Comprobante creado."}
            }

            # Crear archivo dummy para el audio
            from pathlib import Path
            audio_path = Path("input.wav")
            audio_path.write_bytes(b"data")

            print("Ejecutando comando de voz: 'Sarita, crea un comprobante...'")
            response_text, _ = orchestrator.handle_audio_command(
                user=admin,
                api_token="valid-token",
                audio_path=audio_path,
                output_audio_path=Path("output.wav")
            )

            print(f"Respuesta verbal generada: {response_text}")

            # Verificación de la directiva enviada al router
            args, kwargs = mock_post.call_args
            sent_directive = kwargs['json']

            print("\n--- Verificación de Estructura ---")
            print(f"¿Dominio correcto?: {sent_directive['domain'] == 'contable'}")
            print(f"¿Intención correcta?: {sent_directive['mission']['type'] == 'ERP_CREATE_VOUCHER'}")
            print(f"¿Parámetros extraídos?: {sent_directive['parameters']['valor'] == 500000}")

            if audio_path.exists(): audio_path.unlink()

            if sent_directive['domain'] == 'contable' and "created" in response_text.lower() or "creado" in response_text.lower():
                print("\n✅ PRUEBA DE OPERACIÓN POR VOZ EXITOSA.")
            else:
                print("\n⚠️ Verifique la respuesta del LLM en el feedback loop.")

if __name__ == "__main__":
    test_full_voice_operation_cycle()
