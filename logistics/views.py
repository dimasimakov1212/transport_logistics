from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from company.models import Vehicle, Driver
from logistics.forms import ItineraryForm
from logistics.models import Itinerary


class HomePageView(TemplateView):
    """ Главная страница """

    template_name = 'logistics/home.html'

    def get_context_data(self, **kwargs):
        """ Определяем контекстную информацию """

        context = super().get_context_data(**kwargs)

        context['title'] = 'Транспортная логистика'

        return context


class ItineraryListView(ListView):
    """ Список объектов маршруты """

    model = Itinerary

    template_name = 'logistics/itineraries_list.html'

    def get_context_data(self, **kwargs):
        """ Контекстная информация """

        context = super().get_context_data(**kwargs)

        itineraries = Itinerary.objects.all()  # получаем все маршруты

        context['title'] = 'Маршруты'
        context['itineraries'] = itineraries

        return context


class ItineraryCreateView(CreateView):
    """ Создание объекта маршрут """

    model = Itinerary

    # form_class = ItineraryForm
    fields = ['itinerary_number',
              'itinerary_date_start',
              'itinerary_date_finish',
              'itinerary_point_from',
              'itinerary_point_to',
              'itinerary_vehicle',
              'itinerary_driver']

    template_name = 'logistics/itinerary_form.html'

    def form_valid(self, form):
        """ Проверка и сохранение данных """

        self.object = form.save(commit=False)

        # присваиваем значение создателя маршрута текущего пользователя
        self.object.itinerary_owner = self.request.user

        self.object.save()
        print("Ok")

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """ Контекстная информация """

        context = super().get_context_data(**kwargs)

        vehicles = Vehicle.objects.all()  # получаем всех транспортных средств
        drivers = Driver.objects.all()  # получаем всех водителей

        context['title'] = 'Создание маршрута'
        context['vehicles'] = vehicles
        context['drivers'] = drivers

        return context

    def get_success_url(self):
        return reverse('logistics:itineraries_list')
