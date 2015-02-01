from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kyudokaiapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #expresiones regulares la R significa expresiones regulares, la ^ es desde donde comienza y el $ aqui con esto termina
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'librokyudo.views.login'),
    url(r'^hola/(?P<personaid>\d+)$', 'librokyudo.views.saludos'),#P = parametro \d = cualquier digito + = 1 o mas
)
