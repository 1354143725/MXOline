from django.shortcuts import render
from django.views.generic import View
from apps.courses.models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.operations.models import UserFavorite, UserCourse
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.courses.models import CourseResource
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


class CourseDetailView(View):
    def get(self, request, course_id, *args, **kwargs):
        """
        获取课程详情页
        :param request:
        :param args:
        :param kwargs:
        :return:
        # """

        # # 根据id查询课程
        course = Course.objects.get(id=int(course_id))
        # 点击到课程 的详情就记录一次点击数
        course.click_nums += 1
        course.save()
        # 获取收藏状态
        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated:
            # 查询用户是否收藏了该课程和机构 fav_type=1证明是课程收藏，如果有，证明用户收藏了这个课
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=2):
                has_fav_org = True

        return render(request, 'course-detail.html',
                      {"course": course,
                       "has_fav_course": has_fav_course,
                       "has_fav_org": has_fav_org
                       })


class CourseLessonView(LoginRequiredMixin,View):
    """"
    章节信息
    """
    login_url = '/login/'
    def get(self, request, course_id, *args, **kwargs):
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()
        # 该课的同学还学过
        # 查询当前用户都学了那些课
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        # 查询这个用户关联的所有课程
        all_courses = UserCourse.objects.filter(user_id__in=user_ids).order_by("-course__click_nums")[:5]
        # 过滤掉当前课程
        related_courses = []
        for item in all_courses:
            if item.course.id != course.id:
                related_courses.append(item.course)

        # 查询资料信息
        course_resource = CourseResource.objects.filter(course=course)
        return render(request, 'course-video.html',
                      {"course": course,
                       "course_resource":course_resource,
                       "related_courses": related_courses,
                       })