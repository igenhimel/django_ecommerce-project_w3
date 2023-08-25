from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('list/', views.product_list, name='product_list'),
    path('details/<int:product_id>/', views.product_details, name='product_details'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
    path('search/', views.search_products, name='search'),
    path('product_type/<str:product_type>/', views.product_type_search, name='product_type_search')
    
]
