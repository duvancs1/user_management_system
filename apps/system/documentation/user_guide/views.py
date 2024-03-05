from django.contrib.auth.mixins     import LoginRequiredMixin
from django.shortcuts               import render
from django.views                   import View


class UserGuideView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):

        return render(
            self.request,
            template_name = 'system/documentation/user_guide.html',
            context = {}
        )
