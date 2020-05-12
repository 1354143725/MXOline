from django.conf.urls import url,include
from apps.organization.views import OrgView
urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name='list'),
]
