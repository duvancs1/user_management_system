from django.urls                        import path
from .create.views                      import TaskCreateView
from .list.views                        import UserListView
from .update.views                        import TaskUpdateView
from .delete.views                        import TaskDeleteView


app_name = 'user_tasks'

urlpatterns = [
    path('create/',               TaskCreateView.as_view(), name='create'),
    path('list/',                 UserListView.as_view(),   name='list'),
    path('update/<int:task_id>/', TaskUpdateView.as_view(), name='update'),
    path('delete/<int:task_id>/', TaskDeleteView.as_view(), name='delete'),
]
