from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from company.forms import DriverForm
from company.models import Driver


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
