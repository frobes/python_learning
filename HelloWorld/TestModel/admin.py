from django.contrib import admin
from TestModel.models import  Test,Contact,Tag

# Register your models here.
#为了让 admin 界面管理某个数据模型，我们需要先注册该数据模型到 admin。比如，我们之前在 TestModel 中已经创建了模型 Test
#admin.site.register(Test)

#注册多个模型并显示：
admin.site.register( [ Test, Contact , Tag] )


