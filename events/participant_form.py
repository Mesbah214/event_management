from django import forms
from events.models import Participant


class StyledFormMixin:
    default_classes = "border border-blue-800 px-[.8rem] py-[.4rem] w-full focus-visible:outline focus-visible:outline-blue-700 rounded-lg"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': "e.g. John, Doe"
                })
            elif isinstance(field.widget, forms.EmailInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': "e.g. john@gmail.com"
                })

            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': 'space-y-2'
                })


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
