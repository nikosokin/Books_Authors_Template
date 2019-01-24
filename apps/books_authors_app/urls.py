from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addBook$', views.addBook),
    url(r'^addAuthor$', views.addAuthor),
    url(r'^books/(?P<num>\d+)$', views.showBook),
    url(r'^authors$', views.authors),
    url(r'^authors/(?P<num>\d+)$', views.showAuthor),
    url(r'^books/addAuthorToBook$', views.addAtoB),
    url(r'^authors/addBookToAuthor$', views.addBtoA)
]
