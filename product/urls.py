from django.conf.urls.static import static
from django.urls import path

from comment.views import ReviewAdd
from watch_shop import settings
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    SearchListView, filter_product_list

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
    path('filter/', filter_product_list, name='filter')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)