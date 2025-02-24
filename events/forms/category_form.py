from django import forms
from events.models import Category

class StyledFormMixin:
    default_classes = "border border-blue-800 px-[.8rem] py-[.4rem] w-full focus-visible:outline focus-visible:outline-blue-700 rounded-lg mb-[2.4rem]"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': "e.g. Musical, Drama"
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': "e.g. Marks a musical event"
                })

class CategoryModelForm(StyledFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

    class Meta:
        model = Category
        fields = '__all__'