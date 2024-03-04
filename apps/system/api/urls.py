from django.urls                        import path
from .gravatar.profile.views            import UserGravatarView


app_name = 'gravatar'

urlpatterns = [
    path('profile/<int:user_id>/', UserGravatarView.as_view(), name='profile'),
]
