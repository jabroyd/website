from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('', include('landingpage.urls')),
    path('register/', include('landingpage.urls')),
    path('login/', include('landingpage.urls')),

]
