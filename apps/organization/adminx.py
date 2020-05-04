
import xadmin
from apps.organization.models import *
# 不用继承admin.ModelAdmin，
class CityAdmin(object):
    # 显示字典
    list_display = ["id", "name", "desc"]
    # 搜索字段
    search_fields = ["name", "desc"]
    list_filter = ["id", "name", "desc"]

class CourseOrgAdmin(object):
    # 显示字典
    list_display = ["id", "name", "tag", "category", "train"]
    # 搜索字段
    search_fields = ["name"]
    list_filter = ["id", "name", "tag", "category", "train"]


class TeacherAdmin(object):
    # 显示字典
    list_display = ["id", "teacher_name", "name",  "teach_characteristics"]
    # 搜索字段
    search_fields = ["name"]
    list_filter = ["id", "teacher_name", "name",  "teach_characteristics"]

xadmin.site.register(City, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)