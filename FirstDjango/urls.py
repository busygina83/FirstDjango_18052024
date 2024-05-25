from django.urls import path # type: ignore
from MainApp import views


urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('items', views.item_list),
    path('item/<int:item_id>', views.item_detail)
]