"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#默认代码
#urlpatterns = [
#    path('admin/', admin.site.urls),
#]


#第二种改法
#url配置
#from django.conf.urls import  url
#from . import  view

#访问地址http://127.0.0.1:8000
#urlpatterns = [ url(r'^$',view.hello),]

#访问地址http://127.0.0.1:8000/hello
#urlpatterns = [ url(r'^hello$',view.hello),]



#第3种改法
from django.conf.urls import  *
from . import  view,testdb
urlpatterns = [url(r'^hello$',view.hello),url(r'^testdb$',testdb.testdb),]

