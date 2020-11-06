from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Category, Options, Paper, Topic,Records, RecordDetails

#用户
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')

#组
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name')

#分类
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'status')

#问卷
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('__all__')

#问题
class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ('__all__')

#选项
class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ('id', 'name', 'desc', 'topic', 'score', 'owener', 'created_time', 'status')

#记录
class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = ('__all__')

# 群增群改辅助类
class RecordListSerializer(serializers.ListSerializer):
    # 重新update方法
    def update(self, queryset, validated_data_list):
        return [
            self.child.update(queryset[index], validated_data) for index, validated_data in enumerate(validated_data_list)
        ]


#记录详情
class RecordDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = RecordListSerializer
        model = RecordDetails
        fields = ('__all__')

#问卷详情
class TopicAndOptionsSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=32)
    options_set = OptionsSerializer(many=True,read_only=True)

    class Meta:
        model = Topic
        fields = ('__all__')

