from django import forms
from catalog.models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):

    ban_words = ["казино", "криптовалюта", "крипта",
                 "биржа", "дешево", "бесплатно",
                 "обман", "полиция", "радар"]

    class Meta:
        model = Product
        fields = ["name", "description", "category", "price", "image", "is_in_stock"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({'class' : 'form-control',
                                                 'placeholder' : 'Введите название'})
        self.fields["description"].widget.attrs.update({'class': 'form-control',
                                                 'placeholder': 'Введите описание'})
        self.fields["price"].widget.attrs.update({'class': 'form-control',
                                                  'placeholder': 'Введите стоимость'})
        self.fields["is_in_stock"].widget.attrs.update({'class': 'form-check-input',
                                                        'id': 'stock_checkbox'})


    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
           raise ValidationError("Цена не может быть отрицательной")

        return price

    def clean_name(self):
        name = self.cleaned_data.get("name")

        is_name_in_ban = [word for word in self.ban_words if word in name.lower()]

        if is_name_in_ban:
            raise ValidationError(f'Имя не может содержать слово: {", ".join(is_name_in_ban)}')

        return name

    def clean_description(self):
        name = self.cleaned_data.get("description")

        is_description_in_ban = [word for word in self.ban_words if word in name.lower()]

        if is_description_in_ban:
            raise ValidationError(f'Описание не может содержать слово: {", ".join(is_description_in_ban)}')

        return description



    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get("name")
    #     description = cleaned_data.get("description")
    #
    #     is_name_in_ban = [word for word in ban_words if word in name.lower()]
    #     is_description_in_ban = [word for word in ban_words if word in description.lower()]
    #
    #     if name and description and any((is_name_in_ban, is_description_in_ban)):
    #
    #         if is_name_in_ban:
    #             self.add_error("name", f'Имя не может содержать слово: {", ".join(is_name_in_ban)}')
    #         if is_description_in_ban:
    #             self.add_error("description", f'Имя не может содержать слово {", ".join(is_description_in_ban)}')
    #
    #     return cleaned_data

class ProductDeleteForm(forms.Form):
    pass