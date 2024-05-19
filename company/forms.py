from django import forms

from company.models import Driver


class DriverForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super(DriverForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Driver
        fields = '__all__'
