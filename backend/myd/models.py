from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name="名称", help_text="名称")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态", help_text="状态")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Paper(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name="问卷名称")
    desc = models.CharField(max_length=100, blank=True, verbose_name="摘要")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    owener = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="创建者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '问卷'

#题目
class Topic(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    TYPE_RADIO = 1
    TYPE_CHECKBOX = 2
    TYPE_RATE = 3
    TYPE_ITEMS = (
        (TYPE_RADIO, '单选'),
        (TYPE_CHECKBOX, '多选'),
        (TYPE_RATE, '评分')
    )

    name = models.CharField(max_length=50, verbose_name="题目名称")
    desc = models.CharField(max_length=100, blank=True, verbose_name="摘要")
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, verbose_name="所属问卷")
    types = models.PositiveIntegerField(default=TYPE_RADIO, choices=TYPE_ITEMS, verbose_name="题目类型")
    owener = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="创建者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '问题'
        ordering = ['-id']

#选项
class Options(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name="选项名称")
    desc = models.CharField(max_length=100, blank=True, verbose_name="摘要")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="所属问题")
    score = models.IntegerField(verbose_name="分值")
    owener = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="创建者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '选项'
        ordering = ['-id']

#调查记录
class Records(models.Model):

    name = models.CharField(max_length=50, verbose_name="姓名", help_text="姓名")
    sex = models.CharField(max_length=20, blank=True, verbose_name="性别")
    age = models.CharField(max_length=20, blank=True, verbose_name="年龄")
    id_no = models.CharField(max_length=18, blank=True, verbose_name="身份证号")
    address = models.CharField(max_length=100, blank=True, verbose_name="详细地址")
    tel = models.CharField(max_length=20, verbose_name="电话号码")
    types = models.CharField(max_length=50, verbose_name="就诊类别")
    hospital = models.CharField(max_length=10, verbose_name="院区")
    dept = models.CharField(max_length=100, verbose_name="就诊科室")
    doctor = models.CharField(max_length=20, verbose_name="医生")
    times = models.IntegerField(verbose_name="就诊次数", blank=True)
    cost = models.DecimalField(max_digits = 20, blank=True, decimal_places=4, verbose_name="总费用")
    pat_type = models.CharField(max_length=4, blank=True, verbose_name="门诊住院")
    visit_time = models.DateTimeField(blank=True, verbose_name="就诊时间") 
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '调查记录'
        ordering = ['-id']


#调查详情
class RecordDetails(models.Model):

    record = models.ForeignKey(Records, on_delete=models.CASCADE, verbose_name="调查记录")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name="所属问题")
    options = models.ForeignKey(Options, on_delete=models.CASCADE, verbose_name="问题结果")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = verbose_name_plural = '调查详情'
        ordering = ['-id']