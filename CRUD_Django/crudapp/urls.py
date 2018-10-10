
from django.urls import path
from . import views


urlpatterns = [
    path('',views.list_product,name='list_product'),
    path('new',views.create_product,name='create_product'),
    path('update/<int:id>',views.update_product,name='update_product'),
    path('delete/<int:id>',views.delete_product,name='delete_product'),

]
