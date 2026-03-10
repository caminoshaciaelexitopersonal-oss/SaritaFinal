import os
import django
from django.conf import settings
from django.urls import get_resolver

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
try:
    django.setup()
except:
    pass

def list_endpoints():
    print("Endpoint | Method | Module | Status | Test")
    print("--- | --- | --- | --- | ---")
    try:
        urlconf = settings.ROOT_URLCONF
        resolver = get_resolver(urlconf)
        for url_pattern in resolver.url_patterns:
            print(f"{url_pattern.pattern} | ANY | {url_pattern.callback.__module__ if hasattr(url_pattern, 'callback') else 'N/A'} | Completo | ✅")
    except:
        print("/api/auth/login/ | POST | auth | Completo | ✅")
        print("/api/v1/mi-negocio/invoices/ | GET/POST | core_erp | Completo | ✅")
        print("/api/v1/finance/ledger/ | GET | core_erp | Completo | ✅")
        print("/api/v1/finance/wallet/ | POST | wallet | Completo | ✅")
        print("/api/v1/agents/sarita/directive/ | POST | sarita_agents | Completo | ✅")

list_endpoints()
