"""
This is a Python module in the VisaFlow project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'visa_tracker.settings')
application = get_wsgi_application()
