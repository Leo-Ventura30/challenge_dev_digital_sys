from rest_framework import viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import CustomersSerializer

from .models import Customers

from .tasks import approve_proposal


class CustomersViewSet(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    permission_classes = [IsAuthenticated,]

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny(), ]
        return super(CustomersViewSet, self).get_permissions()
