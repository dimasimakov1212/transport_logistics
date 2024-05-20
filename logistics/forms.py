from django import forms

from logistics.models import Itinerary


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# class CityForm(StyleFormMixin, forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#
#         super(CityForm, self).__init__(*args, **kwargs)
#
#     class Meta:
#         model = City
#         fields = '__all__'


class ItineraryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        super(ItineraryForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Itinerary
        # fields = '__all__'
        exclude = ('itinerary_owner',)

        widgets = {
            'itinerary_date_start': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),
            'itinerary_date_finish': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}),
            'itinerary_vehicle': forms.Select()
        }
