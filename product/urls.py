from django.urls import path

from comment.views import ReviewAdd
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    SearchListView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='detail'),
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('product/update/<int:product_id>/', ProductUpdateView.as_view(),
         name='product-update'),
    path('product/delete/<int:product_id>/', ProductDeleteView.as_view(),
         name='product-delete'),
    path('search', SearchListView.as_view(), name='search'),
    path('comment/<int:product_id>', ReviewAdd.as_view(), name="add-review", ),

]