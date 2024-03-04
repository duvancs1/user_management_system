from django.contrib                 import messages
from django.contrib.auth.mixins     import LoginRequiredMixin

from django.shortcuts               import render
from django.views                   import View

from django_htmx.http               import trigger_client_event, HttpResponseClientRefresh

from apps.admin.user.models         import User


class UserDeleteView(LoginRequiredMixin, View):

    def get(self, request, user_id, *args, **kwargs):

        user = User.objects \
            .get(
                id = user_id
            )

        response = render(
            self.request,
            template_name = 'system/user/delete/user_delete.html',
            context = {
                'user' : user,
            }
        )

        trigger_client_event(response, 'openmodal')

        return response

    def post(self, request, user_id, *args, **kwargs):

        user = User.objects \
            .get(
                id = user_id
            )

        if user_id == self.request.user.id:
            messages.error(self.request, "Error: Can't delete currently logged in user")
            return HttpResponseClientRefresh()

        if user:
            user.delete()
            messages.success(self.request, 'Success: User has been deleted')

        return HttpResponseClientRefresh()
