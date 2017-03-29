from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cuentas/', views.account_list,name='cuentas_list'),
    url(r'^profile/edit/$', views.profile_edit,name='profile_edit'),
    url(r'^transaction/create$', views.transaction,name='create_transaction'),
    #url(r'^$', 'marcador.views.bookmark_list', name='marcador_bookmark_list'),
]