from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.generic import RedirectView

from django.contrib.auth import views as auth_views

from . import views

app_name = 'trainingApp'

urlpatterns = [

    url(r'^$', views.home, name='home'),

    url(r'^clients/$', views.ClientsListView.as_view(), name='clients'),
    url(r'^(?P<pk>[0-9]+)/clientDetails/$', views.ClientsDetailView.as_view(), name=
    'clientDetails'),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
