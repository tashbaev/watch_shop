from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, DeleteView

from extra_views import CreateWithInlinesView, UpdateWithInlinesView

from comment.forms import ReviewAddForm
from watch_shop.settings import MEDIA_ROOT
from .forms import ImageInline
from .models import Category, Product


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
    paginate_by = 8
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'
    # print(MEDIA_ROOT)


    def get_queryset(self):
        queryset = super().get_queryset()
        # search_word = self.request.GET.get('q')
        print(self.request)
        band = self.request.GET.get('band')
        price_min = self.request.GET.get('pmax')
        price_max = self.request.GET.get('pmin')
        if band is not None:
            queryset = queryset.filter(band=band)
        if price_min:
            queryset = queryset.filter(price__lte=price_min)
        if price_max:
            queryset = queryset.filter(price__gte=price_max)
        return queryset

    # def get_context_data(self, **kwargs):
    #     context = super(ListView, self).get_context_data(**kwargs)
    #     context['men'] = self.model.objects.filter(category='men')
    #     context['women'] = self.model.objects.filter(category='women')
    #     context['smart'] = self.model.objects.filter(category='smart')
    #     return context




class ProductDetailView(DetailView):
    model = Product # Product.objects.get(product_id)
    template_name = 'detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = ReviewAddForm()
        return context


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


class ProductDeleteView(IsAdminCheckMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    pk_url_kwarg = 'product_id'


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        slug = self.object.category.slug
        self.object.delete()
        return redirect('list', slug)

def filter_product_list(request):
    print(request)
    return render(request, ProductListView, )