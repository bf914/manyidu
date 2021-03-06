# Generated by Django 2.2.16 on 2020-10-29 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='姓名', max_length=50, verbose_name='姓名')),
                ('sex', models.CharField(blank=True, max_length=20, verbose_name='性别')),
                ('age', models.CharField(blank=True, max_length=20, verbose_name='年龄')),
                ('id_no', models.CharField(blank=True, max_length=18, verbose_name='身份证号')),
                ('address', models.CharField(blank=True, max_length=100, verbose_name='详细地址')),
                ('tel', models.CharField(max_length=20, verbose_name='电话号码')),
                ('types', models.CharField(max_length=50, verbose_name='就诊类别')),
                ('hospital', models.CharField(max_length=10, verbose_name='院区')),
                ('dept', models.CharField(max_length=100, verbose_name='就诊科室')),
                ('doctor', models.CharField(max_length=20, verbose_name='医生')),
                ('times', models.IntegerField(blank=True, verbose_name='就诊次数')),
                ('cost', models.DecimalField(blank=True, decimal_places=4, max_digits=20, verbose_name='总费用')),
                ('pat_type', models.CharField(blank=True, max_length=4, verbose_name='门诊住院')),
                ('visit_time', models.DateTimeField(blank=True, verbose_name='就诊时间')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '调查记录',
                'verbose_name_plural': '调查记录',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['-id'], 'verbose_name': '问题', 'verbose_name_plural': '问题'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='名称', max_length=50, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, help_text='状态', verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='options',
            name='score',
            field=models.IntegerField(verbose_name='分值'),
        ),
        migrations.CreateModel(
            name='RecordDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('options', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myd.Options', verbose_name='问题结果')),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myd.Records', verbose_name='调查记录')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myd.Topic', verbose_name='所属问题')),
            ],
            options={
                'verbose_name': '调查详情',
                'verbose_name_plural': '调查详情',
                'ordering': ['-id'],
            },
        ),
    ]
