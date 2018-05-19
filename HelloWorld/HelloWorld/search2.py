# -*- coding:utf-8 -*-
from django.shortcuts import  render
from django.views.decorators import csrf

#接收POST请求数据
#使用 search_post 函数来处理 POST 请求
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt']=request.POST['q']
    return render(request,'post.html',ctx)

