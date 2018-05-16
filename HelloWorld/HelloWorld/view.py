'''from django.http import  HttpResponse

def hello(request):
    return HttpResponse("Hello World!")
'''

#增加一个对象，用于向模板提交数据
#-*- coding:utf-8 -*-#
from django.http import  HttpResponse
from django.shortcuts import  render

def hello(request):
    context = {}
    context['hello'] = 'hello world!'
    #使用render来代替之前使用的HttpResponse,使用字典context作为参数
    return  render(request,'hello.html',context)
