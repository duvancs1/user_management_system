from django.contrib                 import messages
from django.contrib.auth.mixins     import LoginRequiredMixin

from django.shortcuts               import render, redirect
from django.views                   import View

from django_htmx.http               import trigger_client_event, HttpResponseClientRefresh

from .forms                         import TaskCreateForm


class TaskCreateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        response = render(
            self.request,
            template_name = 'system/user_tasks/create/task_create.html',
            context = {
                'form' : TaskCreateForm()
            }
        )

        trigger_client_event(response, 'openmodal')

        return response

    def post(self, request, *args, **kwargs):

        form = TaskCreateForm(request.POST)

        # If the form is not valid we return using a client refresh, prompted with the error below
        if not form.is_valid():
            messages.success(self.request, 'Error: Task has not been created')
            return HttpResponseClientRefresh()

        form.save()

        messages.success(self.request, 'Success: User has been created')

        return HttpResponseClientRefresh()
