from django.conf.urls import url
from library_app import views

urlpatterns = [
    url(r'^authors/$', views.author_list),
    url(r'^authors/(?P<pk>[0-9]+)/$', views.author_detail),
    url(r'^books/$', views.book_list),
    url(r'^books/(?P<pk>[0-9]+)/$', views.book_detail),
]
