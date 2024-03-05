from django.contrib                 import messages
from django.contrib.auth.mixins     import LoginRequiredMixin

from django.shortcuts               import render
from django.views                   import View

from django_htmx.http               import trigger_client_event, HttpResponseClientRefresh

from apps.admin.user_tasks.models   import UserTask


class TaskDeleteView(LoginRequiredMixin, View):

    def get(self, request, task_id, *args, **kwargs):

        user_task = UserTask.objects \
            .get(
                id = task_id
            )

        response = render(
            self.request,
            template_name = 'system/user_tasks/delete/task_delete.html',
            context = {
                'user_task' : user_task,
            }
        )

        trigger_client_event(response, 'openmodal')

        return response

    def post(self, request, task_id, *args, **kwargs):

        user_task = UserTask.objects \
            .get(
                id = task_id
            )

        if user_task:
            user_task.delete()
            messages.success(self.request, 'Success: Task has been deleted')

        return HttpResponseClientRefresh()
