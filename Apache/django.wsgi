import os
import sys
import site

sys.path.append('/home/japhy/launcher')
sys.path.append('/home/japhy/launcher/cubetube')

os.environ['DJANGO_SETTINGS_MODULE'] = 'launcher.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()