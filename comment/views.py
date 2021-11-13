from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from product.models import Product
from .forms import ReviewAddForm
from .models import Review


class ReviewAdd(CreateView):
    model = Review
    form_class = ReviewAddForm
    template_name = 'school/review_add.html'
    def form_valid(self,form):
        self.object = form.save(commit=False)
        product = get_object_or_404(Product, slug=self.kwargs['id'])
        self.object.product = product
        self.object.save()
        return super(ReviewAdd, self).form_valid(form)
