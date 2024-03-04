from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts           import render
from django.views               import View


class HomeView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):

        print('test')

        return render(self.request, 'system/dashboard/dashboard.html')

