from django.shortcuts import render
from app01 import models

from django.core.paginator import Paginator



def index(request):
    '''
    这个视图的关键是将一个Page对象传给前端页面。
    前端代码，可以对这个Page对象进行for循环，调用其has_next()等方法
    :param request:
    :return:
    '''
    limit = 3
    infos = models.Info.objects
    pagin = Paginator(infos,limit)
    page_num = request.GET.get('page',1)  # 字典操作，第一页没有page=,默认取值 1
    a_page = pagin.page(page_num)  # 分页器对象的page方法，返回一个Page对象
    context = {
        'a_page':a_page,
    }
    return render(request,'index.html',context)