from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from logistics.forms import ItineraryForm, CityForm
from logistics.models import Itinerary, City


class HomePageView(TemplateView):
    """ Главная страница """

    template_name = 'logistics/home.html'

    def get_context_data(self, **kwargs):
        """ Определяем контекстную информацию """

        context = super().get_context_data(**kwargs)

        context['title'] = 'Транспортная логистика'

        return context


class CityListView(ListView):
    """ Список объектов город """

    model = City

    template_name = 'logistics/cities_list.html'

    def get_context_data(self, **kwargs):
        """ Контекстная информация """

        context = super().get_context_data(**kwargs)

        cities = City.objects.all().order_by('city_name')  # получаем все города отсортированные по названию

        context['title'] = 'Города'
        context['cities'] = cities

        return context


class CityCreateView(CreateView):
    """ Создание объекта город """

    model = City

    form_class = CityForm
    template_name = 'logistics/city_form.html'

    def form_valid(self, form):
        """ Проверка и сохранение данных """

        self.object = form.save(commit=False)
        self.object.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """ Контекстная информация """

        context = super().get_context_data(**kwargs)

        context['title'] = 'Добавление города'

        return context

    def get_success_url(self):
        return reverse('logistics:cities_list')


class CityUpdateView(UpdateView):
    """ Изменение объекта транспортное средство """

    model = City

    form_class = CityForm
    success_url = reverse_lazy('logistics:cities_list')

    def form_valid(self, form):
        """ Проверка и сохранение данных """

        if form.is_valid():
            new_city = form.save()
            new_city.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """ Контекстная информация """

        context = super().get_context_data(**kwargs)

        context['title'] = 'Изменение города'

        return context


class CityDeleteView(DeleteView):
    """ Удаление объекта транспортное средство """

    model = City
    success_url = reverse_lazy('logistics:cities_list')


class ItineraryListView(ListView):
    """ Список объектов маршруты """

    model = Itinerary

    template_name = 'logistics/itineraries_list.html'

    def get_context_data(self, **kwargs):
        """ Контекстная информация """

        context = super().get_context_data(**kwargs)

        itineraries = Itinerary.objects.all()  # получаем все маршруты

        context['title'] = 'Маршруты'
        context['vehicles'] = itineraries

        return context


class ItineraryCreateView(CreateView):
    """ Создание объекта маршрут """

    model = Itinerary

    form_class = ItineraryForm
    template_name = 'logistics/itinerary_form.html'

    def form_valid(self, form):
        """ Проверка и сохранение данных """

        self.object = form.save(commit=False)

        # присваиваем значение создателя маршрута текущего пользователя
        self.object.itinerary_owner = self.request.user

        self.object.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """ Контекстная информация """

        context = super().get_context_data(**kwargs)

        context['title'] = 'Создание маршрута'

        return context

    def get_success_url(self):
        return reverse('company:vehicles_list')
