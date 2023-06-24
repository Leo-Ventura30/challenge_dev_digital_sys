from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('customers.urls')),
    path('', RedirectView.as_view(
        url='http://localhost:3000', permanent=False), name='not-found')
]
