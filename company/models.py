from django.db import models


class Driver(models.Model):
    """ Модель объекта водитель """

    driver_name = models.CharField(max_length=255, verbose_name='Имя водителя')

    def __str__(self):
        return self.driver_name

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'


class Vehicle(models.Model):
    """ Модель объекта транспортное средство """

    vehicle_brand = models.CharField(max_length=255, verbose_name='Марка авто')
    vehicle_registration = models.CharField(max_length=255, verbose_name='Регистрационный номер')
    need_inspection = models.BooleanField(default=False, verbose_name='Необходимость осмотра')
    need_technical_inspection = models.BooleanField(default=False, verbose_name='Необходимость ТО')
    is_overloading = models.BooleanField(default=False, verbose_name='Перегруз')
    is_overheating = models.BooleanField(default=False, verbose_name='Перегрев')

    def __str__(self):
        return self.vehicle_registration

    class Meta:
        verbose_name = 'Транспортное средство'
        verbose_name_plural = 'Транспортные средства'
