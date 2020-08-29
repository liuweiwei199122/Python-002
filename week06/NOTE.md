学习笔记

创建项目
django-admin startproject MyDjango

创建应用程序
python manage.py help
python manage.py startapp index

运行，默认8000端口
python manage.py runserver

python manage.py runserver 0.0.0.0:80

默认sql引擎是sqlite
改成mysql的方法：
安装pymysql
添加mysql路径的环境变量


from django.urls import path, re_path, register_converter

from . import views, converters



register_converter(converters.IntConverter,'myint')

register_converter(converters.FourDigitYearConverter, 'yyyy')



urlpatterns = [

    path('', views.index),



    ### 带变量的URL

    # path('<int:year>', views.year),  # 只接收整数，其他类型返回404

    path('<int:year>/<str:name>', views.name),



    ### 正则匹配，year变量会传递给views

    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),



    ### 自定义过滤器

    path('<yyyy:year>', views.year), 



]

数据表的读写

$ python manage.py  shell

>>> from index.models import *

>>> n = Name()

>>> n.name='红楼梦'

>>> n.author='曹雪芹'

>>> n.stars=9.6

>>> n.save()



使用ORM框架api实现

增

>>> from index.models import *

>>> Name.objects.create(name='红楼梦', author='曹雪芹', stars='9.6')

>>> Name.objects.create(name='活着', author='余华', stars='9.4')





查

>>> Name.objects.get(id=2).name



改

>>> Name.objects.filter(name='红楼梦').update(name='石头记')



删 

单条数据

>>> Name.objects.filter(name='红楼梦').delete()

全部数据

>>> Name.objects.all().delete()



其他常用查询

>>> Name.objects.create(name='红楼梦', author='曹雪芹', stars='9.6')

>>> Name.objects.create(name='活着', author='余华', stars='9.4')

>>> Name.objects.all()[0].name

>>> n = Name.objects.all()

>>> n[0].name

>>> n[1].name



>>> Name.objects.values_list('name')

<QuerySet [('红楼梦',), ('活着',)]>

>>> Name.objects.values_list('name')[0]

('红楼梦’,)

filter支持更多查询条件

filter(name=xxx, id=yyy)



可以引入python的函数

>>> Name.objects.values_list('name').count()

2



views编写
from django.shortcuts import render



# Create your views here.

from .models import T1

from django.db.models import Avg



def books_short(request):

    ###  从models取数据传给template  ###

    shorts = T1.objects.all()

    # 评论数量

    counter = T1.objects.all().count()



    # 平均星级

    # star_value = T1.objects.values('n_star')

    star_avg =f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "

    # 情感倾向

    sent_avg =f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "



    # 正向数量

    queryset = T1.objects.values('sentiment')

    condtions = {'sentiment__gte': 0.5}

    plus = queryset.filter(**condtions).count()



    # 负向数量

    queryset = T1.objects.values('sentiment')

    condtions = {'sentiment__lt': 0.5}

    minus = queryset.filter(**condtions).count()



    # return render(request, 'douban.html', locals())

    return render(request, 'result.html', locals())

限制 QuerySet 条目数
返回前 5 个对象 (LIMIT 5):
Entry.objects.all()[:5]

Entry.objects.filter(pub_date__lte='2006-01-01')
转换为 SQL 语句大致如下：
SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';

comment = T1.objects.filter(n_star__gt=3)[:20]
