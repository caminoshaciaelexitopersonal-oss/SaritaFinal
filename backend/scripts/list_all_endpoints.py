import os
import django
from django.urls import get_resolver

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puerto_gaitan_turismo.settings')
django.setup()

def list_urls(lis, prefix=''):
    for entry in lis:
        if hasattr(entry, 'url_patterns'):
            list_urls(entry.url_patterns, prefix + str(entry.pattern))
        else:
            methods = 'N/A'
            if hasattr(entry.callback, 'view_class'):
                methods = list(entry.callback.view_class.http_method_names)
            elif hasattr(entry.callback, 'cls'):
                methods = list(entry.callback.cls.http_method_names)

            print(f"{prefix}{str(entry.pattern)} | {methods}")

resolver = get_resolver()
list_urls(resolver.url_patterns)
