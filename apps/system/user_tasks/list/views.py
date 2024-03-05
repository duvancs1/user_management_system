from django.contrib.auth.mixins     import LoginRequiredMixin
from django.shortcuts               import render
from django.views                   import View


from apps.admin.user_tasks.models         import UserTask


class UserListView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        user_tasks = UserTask.objects.all()

        return render(
            self.request,
            template_name = 'system/user_tasks/list/task_list.html',
            context       = {
                'user_tasks'     : user_tasks,
                'logged_in_user' : self.request.user.id,
                'admin_user'     : self.request.user.is_admin
            }
        )

