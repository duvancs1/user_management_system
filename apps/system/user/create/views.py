from django.contrib                 import messages
from django.contrib.auth.mixins     import LoginRequiredMixin

from django.shortcuts               import render, redirect
from django.views                   import View

from django_htmx.http               import trigger_client_event, HttpResponseClientRefresh

from .forms                         import UserCreateForm


class UserCreateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        response = render(
            self.request,
            template_name = 'system/user/create/user_create.html',
            context = {
                'form' : UserCreateForm()
            }
        )

        trigger_client_event(response, 'openmodal')

        return response

    def post(self, request, *args, **kwargs):

        form = UserCreateForm(request.POST)

        # If the form is not valid we return using a client refresh, prompted with the error below
        if not form.is_valid():
            messages.success(self.request, 'Error: User has not been created')
            return HttpResponseClientRefresh()

        form.save()

        messages.success(self.request, 'Success: User has been created')

        return redirect(
            self.request,
            template_name = 'system/user/list/user_list.html'
        )
