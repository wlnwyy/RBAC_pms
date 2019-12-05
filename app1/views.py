from django.contrib import auth
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth import authenticate,login
from .models import *
from .Changes import Change
# django  自带的 分页器  功能
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.

def auth1(func):
    def inner(reqeust):
        # 获取登陆的cookies  信息
        username = reqeust.COOKIES.get('username',None)
        print(username)
        # 判断不存在的话
        if  username == None:
            # 反转到  登录页面
            return render(reqeust, "login.html")
        return func(reqeust)
    return inner

# 登录
class UserLogin(View):
    @method_decorator(auth1)
    def get(self,request):
        return render(request, "login.html")
    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        if not all([username, password]):
            return render(request, "login.html", {"error_msg": "数据不完整"})
        user = authenticate(username=username, password=password)  # 正确返回user对象，不正确返回None
        # print(user.role_id)
        if user is not None:
            # 用户名密码正确
            response = redirect(reverse("index"))

            response.set_cookie("username", username, max_age=7 * 24 * 3600)
            # 重定向到主页
            return response
        else:
        # 用户名或密码错误
            return render(request, "login.html", {"error_msg": "用户名或密码错误"})


quanx ={1:[1,2,3,4],2:[2,3,4],3:[4]}
def index(request):
    """
    获取登录用户的权限 开始做判断
    :param request:
    :return:
    """
    username = request.COOKIES.get('username')
    user = UserAdmin.objects.filter(username=username).values()[0]
    role_id = user.get("role_id")
    role = RoleDefine.objects.filter(role_id=role_id).values()[0]
    # 获取该用户权限  可以访问的  模块
    dengji = quanx.get(role["role_priv_level"])
    modle_dict = {}
    modle_list = []
    lin = 0
    for i in dengji:
        mod = ModuleDefine.objects.filter(modle_id=i).values()[0]
        mdele_name = mod.get("modle_name")
        modele_id = mod.get("modle_id")
        modle_list.append(mdele_name)
        mod_key = ModuleDefine.objects.filter(models_key_id=modele_id).values()
        lin += 1
        name_list = []
        for i in mod_key:
            name  = [i.get("modle_name"),i.get("module_url")]
            name_list.append(name)
        modle_dict[modle_list[lin-1]] = name_list
    # print(type(modle_dict["订单管理"]))
    # print(modle_dict["订单管理"])
    return render(request, 'index.html',{"model_name":modle_dict})

# 注销
def zhu(request):
    response = redirect(reverse("login"))
    response.delete_cookie('username')
    return response


def admin_add(request):
    return render(request, 'admin-add.html')


def admin_cate(request):
    return render(request, 'admin-cate.html')


def admin_edit(request):
    return render(request, 'admin-edit.html')

@auth1
def admin_info(request):
    if request.method == "GET":
        user =  request.COOKIES.get('username')
        user = UserAdmin.objects.get(username=user)
        print(user.email)
        return render(request,"admin-info.html",{'user':user})



def admin_list(request):
    return render(request, 'admin-list.html')


def admin_password(request):

    return render(request, 'admin-password.html')


def admin_role(request):
    return render(request, 'admin-role.html')


def admin_rule(request):
    return render(request, 'admin-rule.html')


def echarts1(request):
    return render(request, 'echarts1.html')


def echarts2(request):
    return render(request, 'echarts2.html')


def echarts3(request):
    return render(request, 'echarts3.html')


def echarts4(request):
    return render(request, 'echarts4.html')


def echarts5(request):
    return render(request, 'echarts5.html')


def echarts6(request):
    return render(request, 'echarts6.html')


def echarts7(request):
    return render(request, 'echarts7.html')


def echarts8(request):
    return render(request, 'echarts8.html')


def member_add(request):
    return render(request, 'member-add.html')


def member_del(request):
    return render(request, 'member-del.html')


def member_edit(request):
    return render(request, 'member-edit.html')

@auth1
def member_list(request):
    username = request.COOKIES.get('username')
    user = UserAdmin.objects.get(username=username)
    mod_id = PormissionDefine.objects.get(module=user.role_priv_level)
    operate_id = [i.operate_id for i in Crup.objects.all()]
    limits = Change(mod_id.crud_opreation, lists=operate_id)
    print(limits)
    staff_all = StallInfo.objects.all().order_by()
    page = Paginator(staff_all,2)
    try:
        number = request.GET.get('index', '1')
        num = page.page(number)
    except PageNotAnInteger:
        num = page.page(1)
    except EmptyPage:
        num = page.page(page.num_pages)
    print(num.object_list)
    return render(request, 'member-list.html', { "all":limits,'page': num, 'paginator': page})

# 修改密码
@auth1
def member_password(request):
    if request.method == 'POST':
        username = request.COOKIES.get('username')
        user = UserAdmin.objects.get(username=username)
        old_password = request.POST.get("oldpass")
        password = request.POST.get("newpass")
        re_password = request.POST.get("repass")
        print(user,old_password,password,re_password)
        if not all ([old_password,password,re_password]):
            return render(request,'admin-password.html',{'error':'请输入完整信息'})
        if password != re_password:
            return render(request, 'admin-password.html', {'error': '两次密码不一致'})
        if check_password(old_password,user.password):
            newpwd = make_password(re_password)
            UserAdmin.objects.filter(id=user.id).update(password=newpwd)
            return render(request,'admin-password.html',{'error':'成功修改'})
    return render(request, 'admin-password.html', {'error': '密码错误'})



def order_add(request):
    return render(request, 'order-add.html')


def order_list(request):
    return render(request, 'order-list.html')


def role_add(request):
    return render(request, 'role-add.html')


def welcome(request):
    return render(request, 'welcome.html')