from django.urls        import path, include

from .home.views        import HomeView

app_name = 'system_dashboard'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home')
]
