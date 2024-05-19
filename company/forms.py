from django import forms

from company.models import Driver, Vehicle


class DriverForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super(DriverForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Driver
        fields = '__all__'


class VehicleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super(VehicleForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Vehicle
        fields = '__all__'
