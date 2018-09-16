from . import models
from . import serializers
from rest_framework import viewsets, permissions


class BaseTableViewSet(viewsets.ModelViewSet):
    """ViewSet for the BaseTable class"""

    queryset = models.BaseTable.objects.all()
    serializer_class = serializers.BaseTableSerializer
    permission_classes = [permissions.IsAuthenticated]


