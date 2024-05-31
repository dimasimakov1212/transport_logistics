from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView

from company.models import Vehicle, Driver
from logistics.forms import ItineraryForm
from logistics.models import Itinerary
from logistics.services import get_plan_days
from users.models import User


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


def itinerary_create(request):
    """ Создание объекта маршрут """

    if request.method == 'POST':

        form = ItineraryForm(request.POST)

        if form.is_valid():
            new_itinerary = Itinerary()
            save_itinerary(
                request=request,
                new_itinerary=new_itinerary,
                itinerary_form=form,
            )

        vehicles = Vehicle.objects.all()  # получаем всех транспортных средств
        drivers = Driver.objects.all()  # получаем всех водителей

        context = {
            'title': 'Создание маршрута',
            'vehicles': vehicles,
            'drivers': drivers,
        }

        return render(request, 'logistics/itineraries_list', {'context': context})

    else:
        form = ItineraryForm()

    return render(request, 'logistics/itinerary_form.html', {'form': form})


class ItineraryUpdateView(generic.edit.UpdateView):
    """ Изменение объекта маршрут """

    model = Itinerary

    form_class = ItineraryForm

    # fields = ['itinerary_number',
    #           'itinerary_date_start',
    #           'itinerary_date_finish',
    #           'itinerary_point_from',
    #           'itinerary_point_to',
    #           'itinerary_vehicle',
    #           'itinerary_driver']

    template_name = 'logistics/itinerary_update.html'

    success_url = reverse_lazy('logistics:itineraries_list')

    def get_object(self, queryset=None):
        itinerary = super(ItineraryUpdateView, self).get_object()

        return itinerary

    def form_valid(self, form):
        """ Проверка и сохранение данных """

        if form.is_valid():
            new_itinerary = form.save()
            new_itinerary.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """ Определяем контекстную информацию """

        context = super().get_context_data(**kwargs)

        vehicles = Vehicle.objects.all()  # получаем всех транспортных средств
        drivers = Driver.objects.all()  # получаем всех водителей

        context['title'] = 'Изменение маршрута'
        context['vehicles'] = vehicles
        context['drivers'] = drivers
        # context['itinerary_number'] = self.object.itinerary_number

        return context


class ItineraryDeleteView(DeleteView):
    """ Удаление объекта маршрут """

    model = Itinerary
    success_url = reverse_lazy('logistics:itineraries_list')


class ItineraryPlanListView(ListView):
    """ Список запланированных разгрузок """

    model = Itinerary

    template_name = 'logistics/itineraries_plan_list.html'

    def get_context_data(self, **kwargs):
        """ Контекстная информация """

        context = super().get_context_data(**kwargs)

        itineraries = Itinerary.objects.all()  # получаем все маршруты
        users = User.objects.all()  # получаем всех пользователей

        days = get_plan_days()  # получаем список дат планируемых разгрузок

        context['title'] = 'Маршруты'
        context['itineraries'] = itineraries
        context['users'] = users
        context['days'] = days

        return context
