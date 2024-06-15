from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/list', views.snippets_list, name='snippets-list'),
    path('snippets/<int:user_id>/list', views.snippets_list, name='snippets-user'),
    path('snippets/<int:snippet_id>', views.snippet_detail, name='snippet-detail'),
    path('snippets/<int:snippet_id>/edit', views.snippet_edit, name='snippet-edit'),
    path('snippets/add', views.snippet_add, name='snippets-add'),
    path('snippets/<int:snippet_id>/delete', views.snippet_delete, name='snippet-delete'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.user_add, name='register')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
