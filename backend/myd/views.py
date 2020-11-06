from django.contrib.auth.models import User, Group
from myd.models import Category, Options, Paper, Topic, Records, RecordDetails
from rest_framework import viewsets, filters,status
from myd.serializers import UserSerializer, GroupSerializer, CategorySerializer, OptionsSerializer, PaperSerializer, TopicSerializer,RecordsSerializer, RecordDetailsSerializer,TopicAndOptionsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .custom_model_view_set import CustomModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .filters import OptionsFilter
from .custom_json_response import JsonResponse


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
    serializer_class = CategorySerializer


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
    serializer_class = OptionsSerializer
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
    serializer_class = PaperSerializer

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
    serializer_class = TopicSerializer

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
    serializer_class = RecordsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    ordering_fields = ["id"]

class RecordDetailsAPIView(APIView):
    # 单查群查
    """
    单查：接口：/RecordDetails/(pk)/
    群查：接口：/RecordDetails/
    """
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            obj = RecordDetails.objects.filter(is_delete=False, pk=pk).first()
            serializer = RecordDetailsSerializer(instance=obj)
            return Response(data=serializer.data)
        else:
            queryset = RecordDetails.objects.filter(is_delete=False).all()
            serializer = RecordDetailsSerializer(instance=queryset, many=True)
            return Response(data=serializer.data)

    # 单增群增
    """
    单增：接口：/RecordDetails/   数据：dict
    群增：接口：/RecordDetails/   数据：list
    """
    def post(self, request, *args, **kwargs):
        # 区别单增群增：request.data是{}还是[]
        if not isinstance(request.data, list):
            # 单增
            serializer = RecordDetailsSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)  # 如果校验失败，会直接抛异常，返回给前台
            obj = serializer.save()
            # 为什么要将新增的对象重新序列化给前台：序列化与反序列化数据不对等
            return Response(data=RecordDetailsSerializer(obj).data, status=200)
        else:
            # 群增
            serializer = RecordDetailsSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)  # 如果校验失败，会直接抛异常，返回给前台
            objs = serializer.save()
            # 为什么要将新增的对象重新序列化给前台：序列化与反序列化数据不对等
            #return Response(data=RecordDetailsSerializer(objs, many=True).data, status=200)
            return JsonResponse(data=RecordDetailsSerializer(objs, many=True).data, code=200, msg="success", status=status.HTTP_200_OK)

class ZyList(APIView):
    def get(self, request):
        data = Topic.objects.all()
        info = TopicAndOptionsSerializer(data,many=True)
        return Response({
            'code': 200,
            'zy_list': info.data
        })
