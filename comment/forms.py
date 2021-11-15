from django import forms

from .models import Review


class ReviewAddForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ['product', 'name',]