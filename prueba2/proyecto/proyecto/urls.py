from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auto/', include('Auto.urls')),
    path('', lambda request: redirect('auto/', permanent=False)),  
]
