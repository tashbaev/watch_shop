from django import forms
from extra_views import InlineFormSetFactory

from .models import Product, Image


# class CreateProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'
#
class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductInline(InlineFormSetFactory):
    model = Product
    fields = '__all__'


class ImageInline(InlineFormSetFactory):
    model = Image
    fields = '__all__'
