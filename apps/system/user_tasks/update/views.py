from django.contrib import messages
from django.contrib.auth.mixins     import LoginRequiredMixin

from django.shortcuts               import render
from django.views                   import View

from django_htmx.http               import trigger_client_event, HttpResponseClientRefresh

from apps.admin.user_tasks.models         import UserTask

from .forms                         import TaskUpdateForm


class TaskUpdateView(LoginRequiredMixin, View):

    def get(self, request, task_id, *args, **kwargs):

        user_task = UserTask.objects \
            .get(
                id = task_id
            )

        response = render(
            self.request,
            template_name = 'system/user_tasks/update/task_update.html',
            context = {
                'user_task' : user_task,
                'form'      : TaskUpdateForm(instance=user_task)
            }
        )

        trigger_client_event(response, 'openmodal')

        return response

    def post(self, request, task_id, *args, **kwargs):

        user_task = UserTask.objects \
            .get(
                id=task_id
            )

        form = TaskUpdateForm(request.POST, instance=user_task)

        if not form.is_valid():
            return render(
                self.request,
                template_name = 'system/user_tasks/update/task_update.html',
                context = {
                    'user_task' : user_task,
                    'form'      : form
                }
            )

        form.save()

        messages.success(self.request, 'Success: User task has been updated')

        return HttpResponseClientRefresh()
