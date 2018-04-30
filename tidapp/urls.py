from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cases/$', views.cases, name='cases'),
    url(r'^blogs/(?P<news_id>[0-9]+)/$', views.blogs, name='blogs'),
    url(r'^about/$', views.about, name='about'),
    url(r'^services/$', views.services, name='services'),
    url(r'^news/$', views.news, name='news'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^design/$', views.design, name='design'),
    url(r'^internet/$', views.internet, name='internet'),
    url(r'^uiux/$', views.uiux, name='uiux'),
    url(r'^application/$', views.application, name='application'),
    url(r'^website_design/$', views.website_design, name='website_design'),
    url(r'^success/$', views.success, name='success'),
    url(r'^work/(?P<work_id>[0-9]+)/$', views.work, name='work'),
]