from django.contrib import messages
from django.contrib.auth.mixins     import LoginRequiredMixin

from django.shortcuts               import render
from django.views                   import View

from django_htmx.http               import trigger_client_event, HttpResponseClientRefresh

from apps.admin.user.models         import User

from .forms                         import UserProfileForm

from .lib                           import validate as validate_lib


class UserProfileView(LoginRequiredMixin, View):

    def get(self, request, user_id, *args, **kwargs):

        user = User.objects \
            .get(
                id = user_id
            )

        response = render(
            self.request,
            template_name = 'system/user/profile/user_profile.html',
            context = {
                'user' : user,
                'form' : UserProfileForm(instance=user)
            }
        )

        trigger_client_event(response, 'openmodal')

        return response

    def post(self, request, user_id, *args, **kwargs):

        user = User.objects \
            .get(
                id = user_id
            )

        form = UserProfileForm(request.POST, instance=user)

        if not validate_lib.check_current_user(self, form, user):
            messages.success(self.request, 'Error: Cannot Deactivate currently logged in user')
            return HttpResponseClientRefresh()

        if not form.is_valid():
            return render(
                self.request,
                template_name = 'system/user/profile/user_profile.html',
                context = {
                    'user' : user,
                    'form' : form
                }
            )

        form.save()

        messages.success(self.request, 'Success: User has been updated')

        return HttpResponseClientRefresh()
