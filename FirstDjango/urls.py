from django.urls import path # type: ignore
from MainApp import views


urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('items', views.item_list),
    path('item/<int:id>', views.item_detail)
]