from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from product.models import Product
from .forms import ReviewAddForm
from .models import Review


class ReviewAdd(CreateView):
    model = Review
    form_class = ReviewAddForm
    # template_name = 'school/review_add.html'
    def form_valid(self,form):
        print(self.kwargs)

        self.object = form.save(commit=False)
        # product = get_object_or_404(Product, id=self.kwargs['product_id'])
        self.object.product_id = self.kwargs['product_id']
        self.object.verified = False

        self.object.save()
        return super(ReviewAdd, self).form_valid(form)

    def get_success_url(self):
        return self.object.product.get_absolute_url()