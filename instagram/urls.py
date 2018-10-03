from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.insta, name='insta'),
    ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)