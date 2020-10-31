from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Category, Options, Paper, Topic,Records, RecordDetails

#用户
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

#组
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

#分类
class CategorySerializeyr(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'id', 'name', 'status')

#问卷
class TopicSerializeyr(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('__all__')

#问题
class PaperSerializeyr(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ('__all__')

#选项
class OptionsSerializeyr(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ('url', 'id', 'name', 'desc', 'topic', 'score', 'owener', 'created_time', 'status')

#记录
class RecordsSerializeyr(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = ('__all__')

#记录详情
class RecordDetailsSerializeyr(serializers.ModelSerializer):
    class Meta:
        model = RecordDetails
        fields = ('__all__')