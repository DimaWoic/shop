from django.conf import settings # только для разработки
from django.conf.urls.static import static # только для разработки
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProductListView.as_view(), name='index')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
