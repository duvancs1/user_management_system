from django.contrib.auth.mixins     import LoginRequiredMixin
from django.shortcuts               import render
from django.views                   import View


class TechnicalDocView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):

        return render(
            self.request,
            template_name = 'system/documentation/technical_doc.html',
            context = {}
        )
