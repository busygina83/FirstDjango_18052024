from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('items', views.item_list, name='item-list'),
    path('item/<int:item_id>', views.item_details, name ='item-detail')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)