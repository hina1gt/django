from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('repairs/', repairs, name='repairs'),
    path('repairs/<int:pk>/', repair_detail, name='repair_detail'),
    path('create/', create, name='create'),
    path('sale/', sale, name='sale'),
    path('sale/<int:pk>/<slug>', sale_detail, name='sale_detail'),
    path('sale/<int:pk>/<slug>/delete/', sale_delete, name='sale_delete'),
    path('sale/<int:pk>/<slug>/update/', sale_update, name='sale_update'),
    path('about/', about, name='about'),
    path('aboutme', aboutme)
]
