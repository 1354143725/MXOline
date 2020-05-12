from django.shortcuts import render
from django.views.generic import View
from apps.courses.models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class CourseView(View):
    def get(self, request, *args, **kwargs):
        """
        展示公开课列表页
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        all_course=Course.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_course, per_page=3, request=request)  # 每页显示多少个per_page
        course = p.page(page)

        return render(request,'course-list.html',{'all_course':course})