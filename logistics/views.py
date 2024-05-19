from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """ Главная страница """

    template_name = 'logistics/home.html'

    def get_context_data(self, **kwargs):
        """ Определяем контекстную информацию """

        context = super().get_context_data(**kwargs)

        context['title'] = 'Транспортная логистика'

        return context
