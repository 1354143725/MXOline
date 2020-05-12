
from django.contrib import admin
from django.urls import path
import xadmin
# from apps.users import views
from django.views.generic import TemplateView
from apps.users.views import LoginView
from apps.courses.views import CourseView
from apps.organization.views import OrgView
from django.conf.urls import url,include
from django.views.static import serve
from MXOline.settings import MEDIA_ROOT
urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    # path('', views.index),
    # 第一种定义路由的方式
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    # 配置授课机构列表展示
    # path('orglist/', OrgView.as_view(), name='orglist'),
    # 配置上传文件的访问的url
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    path('courselist/', CourseView.as_view(), name='course-list'),
    # 授课机构相关操作
    url(r'^org/', include(('apps.organization.urls', 'organization'), namespace='org')),


]
