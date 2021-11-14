from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.list import BaseListView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView

from comment.forms import ReviewAddForm
from comment.models import Review
from .forms import ProductInline, UpdateProductForm, ImageInline
from .models import Category, Product, Image


class SearchListView(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'results'



    def get_queryset(self):
        queryset = super().get_queryset()
        # print(self.request.GET)
        search_word = self.request.GET.get('q')
        if not search_word:
            queryset = Product.objects.none()
        else:
            queryset = queryset.filter(Q(name__icontains=search_word) |
                                        Q(description__icontains=search_word))
        return queryset


class CategoryListView(ListView):
    model = Category # Category.objects.all()
    template_name = 'home.html'
    context_object_name = 'categories'


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        # print(self.kwargs)
        # context['product_id'] = id_
        # context['comment_form'] = ReviewAddForm()
        context['men'] = Product.objects.filter(category='men')
        context['women'] = Product.objects.filter(category='women')
        context['smart'] = Product.objects.filter(category='smart')
        return context




class ProductDetailView(DetailView):
    model = Product # Product.objects.get(product_id)
    template_name = 'detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'


    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        # print(self.kwargs)
        # context['product_id'] = id_
        context['comment_form'] = ReviewAddForm()
        # context['mens'] = model.objects.filter(category='men')
        # context['comments'] = Product.comments
        # print(context)


        return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     # id_ = self.kwargs.get('id')
    #     # queryset = queryset.filter(review__product=id_)
    #     print(queryset)
    #     return queryset

class IsAdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

class ProductCreateView(CreateWithInlinesView):
    model = Product
    inlines = [ImageInline,]
    fields = '__all__'
    template_name = 'create_product.html'

    def get_success_url(self):
        return self.object.get_absolute_url()


class ProductUpdateView(UpdateWithInlinesView):
    model = Product
    inlines = [ImageInline, ]
    fields = '__all__'
    template_name = 'update_product.html'
    pk_url_kwarg = 'product_id'


    def get_success_url(self):
        return self.object.get_absolute_url()


# class ProductCreateView(IsAdminCheckMixin, CreateView):
#     model = Product
#     template_name = 'create_product.html'
#     form_class = CreateProductForm
#     # context_object_name = 'product_form'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['product_form'] = self.get_form(self.get_form_class())
#         return context

class ProductDeleteView(IsAdminCheckMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    pk_url_kwarg = 'product_id'


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        slug = self.object.category.slug
        self.object.delete()
        return redirect('list', slug)
#
# class ProductUpdateView(IsAdminCheckMixin, UpdateView):
#     model = Product
#     template_name = 'update_product.html'
#     form_class = UpdateProductForm
#     pk_url_kwarg = 'product_id'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['product_form'] = self.get_form(self.get_form_class())
#         return context