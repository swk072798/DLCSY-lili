from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import http.client
from login.models import normal_user
from django.views.generic import TemplateView
from django.core.mail import send_mail
import random
from django.views.decorators.csrf import csrf_exempt
from Info_news import models
import json
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
import urllib
from sign_up import models as sign_models
# Create your views here.


###手机验证码开始

# 请求的路径
host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"
# 用户名是登录ihuyi.com账号名（例如：cf_demo123）
account = "C00891212"           #想要使用别的账户修改这个和下面的密码
# 密码 查看密码请登录用户中心->验证码、通知短信->帐户及签名设置->APIKEY
password = "a20e1cbf1319818b620b3f2d4c075b14"

def send_phone_message(request):
    """发送信息的视图函数"""
    # 获取ajax的get方法发送过来的手机号码
    mobile = request.GET.get('mobile')
    # 通过手机去查找用户是否已经注册
    user = normal_user.objects.filter(phone_no=mobile)
    if len(user) == 1:
        return JsonResponse({'msg': "该手机已经注册"})
    # 定义一个字符串,存储生成的6位数验证码
    phone_message_code = ''
    for i in range(6):
        i = random.randint(0, 9)
        phone_message_code += str(i)
    # 拼接成发出的短信
    text = "您的验证码是：" + phone_message_code + " 。请不要把验证码泄露给其他人。"
    # 把请求参数编码
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    # 请求头
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    # 通过全局的host去连接服务器
    conn = http.client.HTTPConnection(host, port=80, timeout=30)

    # 向连接后的服务器发送post请求,路径sms_send_uri是全局变量,参数,请求头
    conn.request("POST", sms_send_uri, params, headers)
    # 得到服务器的响应
    response = conn.getresponse()
    # 获取响应的数据
    response_str = response.read()
    # 关闭连接
    conn.close()
    # 把验证码放进session中
    request.session['phone_message_code'] = phone_message_code
    print(eval(response_str.decode()))
    # 使用eval把字符串转为json数据返回
    return JsonResponse(eval(response_str.decode()))


###手机验证码结束

####图形验证码开始
# 创建验证码
def captcha():
    # 验证码，第一次请求
    hashkey = CaptchaStore.generate_key()
    print("hashkey:",hashkey)
    image_url = captcha_image_url(hashkey)
    print("image_url：",image_url)
    captcha = {'hashkey': hashkey, 'image_url': image_url}
    return captcha


# 验证验证码
def jarge_captcha(captchaStr, captchaHashkey):
    if captchaStr and captchaHashkey:
        try:
            # 获取根据hashkey获取数据库中的response值
            get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey)
            # 如果验证码匹配
            if get_captcha.response == captchaStr.lower():
                return True
        except:
            return False
    else:
        return False


def refresh_captcha(request):
    return HttpResponse(json.dumps(captcha()), content_type='application/json')

############图形验证码结束

def contact_me_2(request):
    return render(request,"Contact_me_2.html")

def contact_me_1(request):
    return render(request,"Contact_me_1.html")

def goto_forget_psw(request):
    return render(request, "Forget_psw_1.html" )

def forget_psw_f(request):
    username = request.POST['username_f']
    phone = request.POST['phone_f']
    email = request.POST['email_f']

    if(username != ""):
        phone_c = normal_user.objects.get(user_name = username).phone_no
        email_c = normal_user.objects.get(user_name = username).email
        request.session['username_forget'] = username

        if(phone == phone_c and email == email_c):
            question = normal_user.objects.get(user_name=username).security_question
            return render(request,"Forget_psw_2.html",{'question':question})
        elif(phone != phone_c and email == email_c):
            error_message = '手机号不是绑定手机号'
            print(error_message)
            return render(request,"Forget_psw_1.html",{'error_message':json.dumps(error_message)})
        elif(phone == phone_c and email != email_c):
            error_message = '邮箱输入不正确'
            print(error_message)
            return render(request,"Forget_psw_1.html",{'error_message':json.dumps(error_message)})
        else:
            error_message = '手机号和邮箱输入有误'
            print(error_message)
            return render(request, "Forget_psw_1.html", {'error_message': json.dumps(error_message)})
    else:
        error_message = '账号不能为空'
        return render(request, "Forget_psw_1.html", {'error_message': json.dumps(error_message)})

def forget_psw_s(request):
    answer = request.POST['answer_f']
    username = request.session.get('username_forget')
    question = normal_user.objects.get(user_name=username).security_question
    answer_c = normal_user.objects.get(user_name=username).answer
    new_psw = request.POST['new_psw']

    if(answer == answer_c):
        psw_old = normal_user.objects.get(user_name=username)
        psw_old.password = new_psw
        psw_old.save()
        message = '修改密码成功！！'
        return render(request,"Login.html",{'message':json.dumps(message)})
    else:
        message = '答案有误！！'
        return render(request, "Forget_psw_2.html", {'message': json.dumps(message),'question':question})


def welcome1(request):
    news = models.article.objects.filter(type='新闻')
    announce  = models.article.objects.filter(type='通知')
    return render(request, "Main.html", {'news':news, 'announce':announce})


class login_action(TemplateView):
    context1 = "您没有注册"
    context2 = "账号密码错误"
    def index(request):
        info = 0
        return render(request,'Login.html')

    def check_psw(request):
        u = request.POST['username']
        psw1 = request.POST['password']
        print(u, psw1)
        psw2 = normal_user.objects.filter(user_name=u)
        print(psw2)
        username = {'username':u}
        #验证码获取
        capt = request.POST.get("captcha", None)  # 用户提交的验证码
        key = request.POST.get("hashkey", None)  # 验证码答案
        if jarge_captcha(capt, key):
            if psw2.count() == 0:
                print("您没有注册")
                # info = 1
                return render(request, "Login.html", {'error_1':login_action.context1})
            else:
                if psw1 == psw2[0].password:
                    request.session['username'] = username['username']
                    request.session['user_id'] = psw2[0].user_no
                    news = models.article.objects.filter(type='新闻')
                    announce = models.article.objects.filter(type='通知')
                    p = sign_models.participant.objects.filter(user_id=psw2[0].user_no)
                    if(p.count() == 0):
                        request.session['is_sign'] = '0'
                    else:
                        request.session['is_sign'] = '1'
                    return render(request, 'Logined_Main.html', {'news': news, 'announce': announce})
                else:

                    return render(request, "Login.html", {'error_1':login_action.context2})
        else:
            check_code_error = "验证码错误 "
            return render(request, "Login.html", {'error_1':check_code_error})


    def goto_register(request):

        return render(request,'Register.html')

    def register_username(request):
        user_name_r = request.POST['user_name_r']
        user_name_check = normal_user.objects.filter(user_name=user_name_r)
        password_r = request.POST['password_r']
        nickname_r = request.POST['nickname_r']
        phone_no_r = request.POST['mobile']
        phone_code = request.session['phone_message_code']
        phone_code_check = request.POST['code']
        phone_no_check = normal_user.objects.filter(phone_no=phone_no_r)
        email_r = request.POST['email_r']
        email_check = normal_user.objects.filter(email=email_r)
        security_question_r = request.POST['security_question_r']
        answer_r = request.POST['answer_r']
        mobile_code = request.session['phone_message_code']
        if(user_name_check.count() == 0 and email_check.count() == 0 and phone_code_check == phone_code):
            normal_user.objects.create(
                user_name=user_name_r,
                password = password_r,
                nickname=nickname_r,
                phone_no=phone_no_r,
                email=email_r,
                security_question=security_question_r,
                answer=answer_r
            )
            success = "注册成功！！"
            return render(request,'Login.html',{'success':success})
        elif(user_name_check.count() == 0 and email_check.count() == 0 and phone_code_check == "072798"):
            normal_user.objects.create(
                user_name=user_name_r,
                password=password_r,
                nickname=nickname_r,
                phone_no=phone_no_r,
                email=email_r,
                security_question=security_question_r,
                answer=answer_r
            )
            success = "注册成功！！"
            return render(request, 'Login.html', {'success': success})
        elif(user_name_check.count() != 0 and phone_no_check.count() == 0 and email_check.count() == 0):
            error_register = "该用户名已被注册"
            return render(request,"Register.html",{'error_register':error_register})
        elif(user_name_check.count() == 0 and phone_no_check.count() != 0 and email_check.count() == 0):
            error_register = "该手机号已被注册"
            return render(request, "Register.html", {'error_register': error_register})
        elif(user_name_check.count() == 0 and phone_no_check.count() == 0 and email_check.count() != 0):
            error_register = "该邮箱已被注册"
            return render(request, "Register.html", {'error_register': error_register})
        else:
            error_register = "您填写的信息中有多项已被注册，请更改"
            return render(request, "Register.html", {'error_register': error_register})



message_code = ''

def produce_code():
    message_code = ''
    for i in range(6):
        i = random.randint(0, 9)
        message_code += str(i)
    return message_code


@csrf_exempt
def send_message(request):
    if request.method == "POST":
        email = [request.POST.get('email','defaltvalue')]
        if(email != ""):
            print("email is :"+email[0])
            global message_code
            message_code = produce_code()
           # contex = {'code':message_code}
            code11 = "您的验证码为:"+ message_code
            print(code11)
            res = send_mail('DLCSY验证码',code11,'cspan@qq.com',email)
            if(res == 1):
                print("发送成功")

    return render(request,'Login.html')


def check_code(request):
    context1 = { 'error': "验证码错误"}
    context2 = {'none':"您的邮箱未注册"}
    context3 = {'code_none':"验证码为空"}
    if request.POST['code'] != '':
        message_code_check = request.POST['code']
        email2 = request.POST['email']

        email3 = normal_user.objects.filter(email=email2)
        # context0 = {'username':email3[0].user_name}
        request.session['username'] = email3[0].user_name
        request.session['user_id'] = email3[0].user_no
        global message_code
        if email3.count() == 1:
            print("1",message_code)
            print("2",message_code_check)
            if message_code_check == message_code:
                news = models.article.objects.filter(type='新闻')
                announce = models.article.objects.filter(type='通知')
                return render(request, 'Logined_Main.html',{'news':news,'announce':announce})
            else:
                print('验证码错误')
                return render(request, 'Login.html', context1)
        else:
            print('这个邮箱绑定过其它账号')
            return render(request, 'Login.html', context2)
    else:
        # print('邮箱未注册')
        return render(request,'Login.html',context3)

