from django.contrib.auth.models import User, Group
from myd.models import Category, Options, Paper, Topic, Records, RecordDetails
from rest_framework import viewsets, filters
from myd.serializers import UserSerializer, GroupSerializer, CategorySerializeyr, OptionsSerializeyr, PaperSerializeyr, TopicSerializeyr,RecordsSerializeyr, RecordDetailsSerializeyr
from .custom_model_view_set import CustomModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .filters import OptionsFilter

class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CategoryViewSet(CustomModelViewSet):
    """
    list:
    分页查询分类对象

    retrieve:
    查询一个分类信息

    create:
    新增一个分类
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializeyr


class OptionsViewSet(CustomModelViewSet):
    """
    list:
    分页查询选项对象

    retrieve:
    查询一个选项信息

    create:
    新增一个选项
    """
    queryset = Options.objects.all()
    serializer_class = OptionsSerializeyr
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OptionsFilter

class PaperViewSet(CustomModelViewSet):
    """
    list:
    分页查询问卷对象

    retrieve:
    查询一个问卷信息

    create:
    新增一个问卷
    """
    queryset = Paper.objects.all()
    serializer_class = PaperSerializeyr

class TopicViewSet(CustomModelViewSet):
    """
    list:
    分页查询问题对象

    retrieve:
    查询一个问题信息

    create:
    新增一个问题
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializeyr

class RecordsViewSet(CustomModelViewSet):
    """
    list:
    分页查询调查记录对象

    retrieve:
    查询一个调查记录信息

    create:
    新增一个调查记录
    """
    queryset = Records.objects.all()
    serializer_class = RecordsSerializeyr
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    ordering_fields = ["id"]

class RecordDetailsViewSet(CustomModelViewSet):
    """
    list:
    分页查询记录明细对象

    retrieve:
    查询一个记录明细信息

    create:
    新增一个记录明细
    """
    queryset = RecordDetails.objects.all()
    serializer_class = RecordDetailsSerializeyr
