from django.db import models
from apps.users.models import BaseModel
from apps.users.models import UserProfile
class City(BaseModel):
    name=models.CharField(verbose_name="城市名", max_length=50)
    desc = models.CharField(verbose_name="城市描述", max_length=300)
    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class CourseOrg(BaseModel):
    name = models.CharField(verbose_name="机构名称", max_length=50)
    tag = models.CharField(verbose_name="机构标签", max_length=10, default="")
    category = models.CharField(verbose_name="机构类别", max_length=20, default="")
    train = models.CharField(verbose_name="培训机构", choices=(("gr", "个人"), ("gx", "高校")),max_length=2)
    students = models.IntegerField(verbose_name="学习人数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏人数", default=0)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="logo", max_length=100)
    address= models.CharField(verbose_name="机构地址", max_length=300)
    learn_times = models.IntegerField(default=0, verbose_name="课程数")
    is_authentication = models.BooleanField(default=False,verbose_name="是否认证")
    is_banner = models.BooleanField(default=False,verbose_name="是否金牌")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="所在城市")

    class Meta:
        verbose_name = "培训机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="用户")
    name = models.CharField(verbose_name="所属机构", max_length=50)
    teacher_name = models.CharField(verbose_name="教师名", max_length=50)
    work_year = models.IntegerField(verbose_name="工作年限", default=0)
    company = models.CharField(verbose_name="就职公司", max_length=50)
    position = models.CharField(verbose_name="公司职位", max_length=50)
    teach_characteristics = models.CharField(verbose_name="教学特点", max_length=300, default="")
    fav_nums = models.IntegerField(verbose_name="收藏人数", default=0)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    age = models.IntegerField(verbose_name="年龄", default=0)
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="头像", max_length=100)
    class Meta:
        verbose_name = "老师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

