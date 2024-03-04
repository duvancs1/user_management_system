from django.contrib import messages
from django.contrib.auth.mixins     import LoginRequiredMixin

from django.shortcuts               import render
from django.views                   import View

from django_htmx.http               import trigger_client_event, HttpResponseClientRefresh

from apps.admin.user.models         import User

from .forms                         import UserUpdateForm


class UserUpdateView(LoginRequiredMixin, View):

    def get(self, request, user_id, *args, **kwargs):

        user = User.objects \
            .get(
                id = user_id
            )

        response = render(
            self.request,
            template_name = 'system/user/update/user_update.html',
            context = {
                'user' : user,
                'form' : UserUpdateForm(instance=user)
            }
        )

        trigger_client_event(response, 'openmodal')

        return response

    def post(self, request, user_id, *args, **kwargs):

        user = User.objects \
            .get(
                id = user_id
            )

        form = UserUpdateForm(request.POST, instance=user)

        if not form.is_valid():
            return render(
                self.request,
                template_name = 'system/user/update/user_update.html',
                context = {
                    'user' : user,
                    'form' : form
                }
            )

        form.save()

        messages.success(self.request, 'Success: User has been updated')

        return HttpResponseClientRefresh()
