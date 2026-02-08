# Tests para validar la consistencia del contrato de la API
import yaml
from rest_framework.test import APITestCase
from django.urls import reverse

class ContractValidationTests(APITestCase):
    """
    Valida que el comportamiento real de la API se corresponda con los
    artefactos de contrato generados (OpenAPI).
    """

    def test_schema_conforms_to_expectations(self):
        """
        Verifica el esquema OpenAPI generado para asegurar que las reglas
        de negocio clave estén correctamente documentadas.
        """
        # Obtener el esquema generado en vivo
        response = self.client.get(reverse('schema'))
        self.assertEqual(response.status_code, 200)

        # Cargar el esquema YAML a un diccionario de Python
        schema = yaml.safe_load(response.content)

        # --- VALIDACIONES CLAVE DEL CONTRATO ---

        # 1. El path de facturas-venta debe existir
        facturas_path = '/api/v1/mi-negocio/comercial/facturas-venta/'
        self.assertIn(facturas_path, schema['paths'], "El endpoint de facturas no está en el esquema.")

        # 2. El método POST debe requerir 'cliente_id' y 'numero_factura'
        post_operation = schema['paths'][facturas_path]['post']
        request_body_schema = post_operation['requestBody']['content']['application/json']['schema']
        component_name = request_body_schema['$ref'].split('/')[-1]
        write_serializer_schema = schema['components']['schemas'][component_name]

        self.assertIn('cliente_id', write_serializer_schema['required'])
        self.assertIn('numero_factura', write_serializer_schema['required'])

        # 3. El método POST NO debe permitir enviar 'total' (debe ser readOnly)
        self.assertTrue(
            write_serializer_schema['properties']['total']['readOnly'],
            "El campo 'total' no está marcado como readOnly en el contrato de escritura."
        )

        # 4. El modelo debe incluir el nuevo estado 'COMERCIAL_CONFIRMADA'
        schema_node = schema['paths'][facturas_path]['get']['responses']['200']['content']['application/json']['schema']

        # Manejar paginación si existe
        if '$ref' in schema_node and 'Paginated' in schema_node['$ref']:
            component_name = schema_node['$ref'].split('/')[-1]
            pagination_schema = schema['components']['schemas'][component_name]
            factura_detail_schema_ref = pagination_schema['properties']['results']['items']['$ref']
        elif 'properties' in schema_node and 'results' in schema_node['properties']:
            factura_detail_schema_ref = schema_node['properties']['results']['items']['$ref']
        elif 'items' in schema_node:
            factura_detail_schema_ref = schema_node['items']['$ref']
        else:
            # Si no es ninguna de las anteriores, intentar acceder directamente (comportamiento original como fallback)
            factura_detail_schema_ref = schema_node['properties']['results']['items']['$ref']

        factura_detail_component = factura_detail_schema_ref.split('/')[-1]
        factura_detail_properties = schema['components']['schemas'][factura_detail_component]['properties']

        estado_prop = factura_detail_properties['estado']
        if 'enum' in estado_prop:
            estado_enum = estado_prop['enum']
        elif 'allOf' in estado_prop:
            enum_ref = estado_prop['allOf'][0]['$ref'].split('/')[-1]
            estado_enum = schema['components']['schemas'][enum_ref]['enum']
        else:
            self.fail("No se pudo encontrar el enum para el campo 'estado' en el esquema.")

        self.assertIn(
            'COMERCIAL_CONFIRMADA',
            estado_enum,
            "El nuevo estado 'COMERCIAL_CONFIRMADA' no está documentado en el enum del contrato."
        )

        print("\n--- Verificación de Contrato Automática: OK ---")
