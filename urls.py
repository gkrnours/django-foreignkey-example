from django.conf.urls import url

from . import views

app_name = 'author'
urlpatterns = [
    url(r'^$', views.Authors.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.Books.as_view(), name='books'),
    url(r'^author/(?P<pk>[0-9]+)/add$', views.BookCreate.as_view(),
        name='book_create'),
    url(r'^book/(?P<pk>[0-9]+)/edit$', views.BookDelete.as_view(),
        name='book_delete'),
    url(r'^book/(?P<pk>[0-9]+)/add$', views.BookUpdate.as_view(),
        name='book_update'),
]
