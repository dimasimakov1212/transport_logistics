from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from company.forms import DriverForm, VehicleForm
from company.models import Driver, Vehicle


class DriversListView(ListView):
    """ Список объектов водители """

    model = Driver

    template_name = 'company/drivers_list.html'

    def get_context_data(self, **kwargs):
        """ Определяем контекстную информацию """

        context = super().get_context_data(**kwargs)

        drivers = Driver.objects.all()  # получаем всех водителей

        context['title'] = 'Водители'
        context['drivers'] = drivers

        return context


class DriverCreateView(CreateView):
    """ Создание объекта водитель """

    model = Driver

    form_class = DriverForm
    template_name = 'company/driver_form.html'

    def form_valid(self, form):
        """ Проверка и сохранение данных """

        self.object = form.save(commit=False)
        self.object.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """ Определяем контекстную информацию """

        context = super().get_context_data(**kwargs)

        context['title'] = 'Добавление водителя'

        return context

    def get_success_url(self):
        return reverse('company:drivers_list')


class DriverUpdateView(UpdateView):
    """ Изменение объекта водитель """

    model = Driver

    form_class = DriverForm
    success_url = reverse_lazy('company:drivers_list')

    def form_valid(self, form):
        """ Проверка и сохранение данных """

        if form.is_valid():
            new_driver = form.save()
            new_driver.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """ Определяем контекстную информацию """

        context = super().get_context_data(**kwargs)

        context['title'] = 'Изменения водителя'

        return context


class DriverDeleteView(DeleteView):
    """ Удаление объекта водитель """

    model = Driver
    success_url = reverse_lazy('company:drivers_list')


class VehicleListView(ListView):
    """ Список объектов транспортные средства """

    model = Vehicle

    template_name = 'company/vehicles_list.html'

    def get_context_data(self, **kwargs):
        """ Контекстная информация """

        context = super().get_context_data(**kwargs)

        vehicles = Vehicle.objects.all()  # получаем всех водителей

        context['title'] = 'Транспортные средства'
        context['vehicles'] = vehicles

        return context


class VehicleCreateView(CreateView):
    """ Создание объекта транспортное средство """

    model = Vehicle

    form_class = VehicleForm
    template_name = 'company/vehicle_form.html'

    def form_valid(self, form):
        """ Проверка и сохранение данных """

        self.object = form.save(commit=False)
        self.object.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """ Контекстная информация """

        context = super().get_context_data(**kwargs)

        context['title'] = 'Добавление транспортного средства'

        return context

    def get_success_url(self):
        return reverse('company:vehicles_list')


class VehicleUpdateView(UpdateView):
    """ Изменение объекта транспортное средство """

    model = Vehicle

    form_class = VehicleForm
    success_url = reverse_lazy('company:vehicles_list')

    def form_valid(self, form):
        """ Проверка и сохранение данных """

        if form.is_valid():
            new_vehicle = form.save()
            new_vehicle.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """ Контекстная информация """

        context = super().get_context_data(**kwargs)

        context['title'] = 'Изменение транспортного средства'

        return context


class VehicleDeleteView(DeleteView):
    """ Удаление объекта транспортное средство """

    model = Vehicle
    success_url = reverse_lazy('company:vehicles_list')
