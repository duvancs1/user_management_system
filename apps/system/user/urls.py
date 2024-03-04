from django.urls                        import path
from .create.views                      import UserCreateView
from .read.views                        import UserListIew
from .update.views                      import UserUpdateView
from .delete.views                      import UserDeleteView
from .profile.views                     import UserProfileView
from .hierarchy.views                   import UserHierarchyView

app_name = 'user'

urlpatterns = [
    path('create_user/',                UserCreateView.as_view(),    name='create_user'),
    path('user_profile/<int:user_id>/', UserProfileView.as_view(),   name='user_profile'),
    path('list_user/',                  UserListIew.as_view(),       name='list_user'),
    path('update_user/<int:user_id>/',  UserUpdateView.as_view(),    name='update_user'),
    path('delete_user/<int:user_id>/',  UserDeleteView.as_view(),    name='delete_user'),
    path('user_hierarchy/',             UserHierarchyView.as_view(), name='user_hierarchy'),
]
