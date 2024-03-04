from django.contrib.auth.mixins     import LoginRequiredMixin
from django.shortcuts               import render
from django.views                   import View


from apps.admin.user.models         import User


class UserGravatarView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):

        user = User.objects.filter(
            id = self.kwargs['user_id']
        ).first()

        return render(
            self.request,
            template_name = 'system/api/gravatar/gravatar_profile.html',
            context = {
                'user' : user,
            }
        )

    def post(self, request, *args, **kwargs):

        print('test')

        # form = UserCreateForm(request.POST)
        #
        # # If the form is not valid we return using a client refresh, prompted with the error below
        # if not form.is_valid():
        #     messages.success(self.request, 'Error: User has not been created')
        #     return HttpResponseClientRefresh()
        #
        # form.save()
        #
        # messages.success(self.request, 'Success: User has been created')
        #
        # return redirect(
        #     self.request,
        #     template_name = 'system/user/list/user_list.html'
        # )

