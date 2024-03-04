from django.contrib.auth.mixins     import LoginRequiredMixin
from django.shortcuts               import render
from django.views                   import View


from apps.admin.user.models         import User

from .lib                           import process as process_lib


class UserHierarchyView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):

        hierarchy_dict = {}

        users = User.objects.all().order_by('id')

        if users:
            hierarchy_dict = process_lib.create_user_hierarchy_dict(users)

        return render(
            self.request,
            template_name = 'system/user/hierarchy/user_hierarchy.html',
            context = {
                'users'          : users,
                'hierarchy_dict' : hierarchy_dict,
            }
        )

