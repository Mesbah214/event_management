from django import forms
from events.models import Event


class StyledFormMixin:
    default_classes = "border border-blue-800 mb-[1.6rem] px-[.8rem] py-[.4rem] w-full focus-visible:outline focus-visible:outline-blue-700 rounded-lg"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if field_name == 'location' and isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': "e.g. Venue or Address"  # Custom placeholder for location field
                })
            elif isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} w-max block",
                })
            elif isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': "e.g. Concert mania"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': "e.g. Famous bands will get together to rock the evening"
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} w-max mr-[1rem]",
                })
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} w-max"
                })


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
            'time': forms.TimeInput(attrs={'type': 'time'})
        }
