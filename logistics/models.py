from django.db import models

from company.models import Vehicle, Driver
from config import settings


class Itinerary(models.Model):
    """ Модель объекта маршрут """

    itinerary_number = models.CharField(max_length=10, verbose_name='Номер маршрута')
    itinerary_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата составления')
    itinerary_date_start = models.DateTimeField(verbose_name='Дата погрузки')
    itinerary_date_finish = models.DateTimeField(verbose_name='Дата разгрузки')
    itinerary_point_from = models.CharField(max_length=100, verbose_name='Место погрузки')
    itinerary_point_to = models.CharField(max_length=100, verbose_name='Место разгрузки')
    itinerary_vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, verbose_name='Транспортное средство')
    itinerary_driver = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name='Водитель')
    itinerary_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                        verbose_name='Менеджер')

    def __str__(self):
        return f"{self.itinerary_date_finish} в {self.itinerary_point_to}"

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
