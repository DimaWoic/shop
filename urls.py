from django.conf import settings # только для разработки
from django.conf.urls.static import static # только для разработки
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    #path('<slug:category_slug>/', views.ProductsByCategorySlug.as_view(), name='by_category_slug'),
    #path('available/', views.ProductsByAvailable.as_view(), name='by_available'),
    #path('<int:id>/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('about/', views.AboutUsView.as_view(), name='about'),
    path('products/', views.ServicesView.as_view(), name='products'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
