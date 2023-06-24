from django.urls import path, include
from rest_framework import routers
from .views import CustomersViewSet

router = routers.DefaultRouter()
router.register('customers', CustomersViewSet)

urlpatterns = [
    path('', include(router.urls))
]
