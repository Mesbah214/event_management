from django import forms
from events.models import Category, Event, Participant

class StyledFormMixin:
    default_classes = "border border-blue-800 px-[.8rem] py-[.4rem] w-full focus-visible:outline focus-visible:outline-blue-700 rounded-lg mb-[2.4rem]"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                })
            if isinstance(field.widget, forms.EmailInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                })
            if isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} w-max mr-[1rem]",
                })
            if isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} w-max ml-[1rem]",
                })
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} w-max ml-[1rem]",
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': self.default_classes,
                })

class CategoryModelForm(StyledFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

    class Meta:
        model = Category
        fields = '__all__'

class EventModelForm(StyledFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'category': forms.Select,
            'date': forms.SelectDateWidget,
            'time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'})
        }

class ParticipantModelForm(StyledFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

    class Meta:
        model = Participant
        fields = '__all__'
        widgets = {
            'event': forms.CheckboxSelectMultiple
        }
