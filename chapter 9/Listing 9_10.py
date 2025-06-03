#Listing 9_10: wsgi.py
import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channelproject.settings')
application = get_wsgi_application()
