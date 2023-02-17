from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('str:<category_slug>', views.product_list, name='product_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]