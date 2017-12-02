from django.conf.urls import url

from bookshit.views import AuthorDelete, AuthorUpdate, AuthorCreate, AuthorList
from . import views

urlpatterns = [
    # ...
    url(r'^$', views.index, name='home'),
    url(r'^author-list/$', AuthorList.as_view(), name='author-list'),
    url(r'author/add/$', AuthorCreate.as_view(), name='author-add'),
    url(r'author/(?P<pk>[0-9]+)/$', AuthorUpdate.as_view(), name='author-update'),
    url(r'author/(?P<pk>[0-9]+)/delete/$', AuthorDelete.as_view(), name='author-delete'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetail.as_view(), name='author-detail'),
]