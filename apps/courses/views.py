from django.shortcuts import render
from django.views.generic import View
from apps.courses.models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


class CourseListView(View):
    def get(self, request, *args, **kwargs):
        """
        展示公开课列表页
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        """获取课程列表信息"""
        all_courses = Course.objects.order_by("-add_time")
        hot_orgs = all_courses.order_by("-click_nums")[:3]

        sort = request.GET.get('sort', "")
        if sort == 'students':
            # 根据学生人数排序  减号代表倒序排序的意思
            all_courses = all_courses.order_by('-students')
        elif sort == 'hot':
            # 根据课程数进行排序
            all_courses = all_courses.order_by('-fav_nums')
        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, per_page=10, request=request)  # 每页显示多少个per_page
        courses = p.page(page)

        return render(request, 'course-list.html',
                      {"all_courses": courses,
                      "sort": sort,
                      "hot_orgs": hot_orgs,

                       })