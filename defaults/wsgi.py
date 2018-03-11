from django.core.wsgi import get_wsgi_application

from defaults import setenv

setenv(bundled=True)

application = get_wsgi_application()
