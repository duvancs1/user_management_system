from django.urls                        import path
from .create.views                      import TaskCreateView
from .list.views                        import UserListView


app_name = 'user_tasks'

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='create'),
    path('list/',   UserListView.as_view(),   name='list'),

]
