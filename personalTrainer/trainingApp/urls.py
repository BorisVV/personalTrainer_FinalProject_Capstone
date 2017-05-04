from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views, views_sendEmails

app_name = 'trainingApp'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # ex: /
    url(r'^index$', views.IndexView.as_view(), name='index'),
    # ex: /5/ wher 5 is the id number.
    url(r'^number/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /5/starts/
    url(r'^(?P<question_id>[0-9]+)/stars/$', views.stars, name='stars'),
    # emails
    url(r'^messages/$', views_sendEmails.send_email, name='emails'),
    url(r'^form/$', views_sendEmails.viewEmailForm, name='emailForm'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
