from django.conf.urls import patterns, url
from coffee import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^no-sale/$', views.no_sale, name='no_sale'),
    url(r'^coffee-order/$', views.coffee_order, name='coffee_order'),
    url(r'^(?P<id>[0-9]+)/cancel/$', views.cancel_line, name='cancel_line'),
)
