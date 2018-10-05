
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.insta, name='insta'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^search/', views.search, name='search')

 ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)