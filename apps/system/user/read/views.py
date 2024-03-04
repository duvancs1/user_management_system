from django.contrib.auth.mixins     import LoginRequiredMixin
from django.shortcuts               import render
from django.views                   import View


from apps.admin.user.models         import User

from .lib                           import process as process_lib


class UserListIew(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        users = User.objects.all().order_by('-id')

        if users:
            process_lib.get_gravatar_images(users)

        return render(
            self.request,
            template_name = 'system/user/list/user_list.html',
            context       = {
                'users'          : users,
                'logged_in_user' : self.request.user.id,
                'admin_user'     : self.request.user.is_admin
            }
        )

