"""
This module defines API endpoints using Django REST Framework.
Includes a viewset for managing VisaApplication data.
"""

"""
This module defines API endpoints using Django REST Framework.
Includes viewsets for Visa Application operations.
"""

from rest_framework import viewsets
from .models import VisaApplication
from .serializers import VisaApplicationSerializer

class VisaApplicationViewSet(viewsets.ModelViewSet):
    queryset = VisaApplication.objects.all()
    serializer_class = VisaApplicationSerializer
