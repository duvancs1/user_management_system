from django.urls import path, include

urlpatterns = [
    path('dashboard/',     include('apps.system.dashboard.urls')),
    path('documentation/', include('apps.system.documentation.urls')),
    path('user/',          include('apps.system.user.urls')),
    path('api/',           include('apps.system.api.urls')),
]
