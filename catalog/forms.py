from django import forms
from catalog.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "price", "image"]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        ban_words = ["казино", "криптовалюта", "крипта",
                     "биржа", "дешево", "бесплатно",
                     "обман", "полиция", "радар"]

        is_name_in_ban = name.lower() in ban_words
        is_description_in_ban = description.lower() in ban_words

        if name and description and any((is_description_in_ban, is_description_in_ban)):

            if is_name_in_ban:
                self.add_error("name", f'Имя не может содержать слово {name}')
            if is_description_in_ban:
                self.add_error("description", f'Имя не может содержать слово {description}')