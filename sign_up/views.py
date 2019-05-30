from django.shortcuts import render,redirect
from sign_up import models
from login import models as Lmodels
from join_team import models as join_team_models
import json
from django.core import serializers
from django.http import JsonResponse,HttpResponse
import os
from Info_news import models as news_models
from django.views.decorators.csrf import csrf_exempt
import time,qrcode
from sign_up.pay import AliPay
import csv
from Info_news import models as info_models


# Create your views here.

def score_list_B(request):
    user_id = request.session['user_id']
    event_id = models.participant.objects.filter(user_id=user_id)[0].event_id
    file_path = "D:\\DLCSY-version\\DLCSY-V0.0.4\\static\\score_record\\"+str(event_id)+"B.csv"
    file_list = list(csv.reader(open(file_path,'r')))
    print(file_list)
    list_1 = []


    for i in range(len(file_list)):
        #p = models.participant.objects.get(id = int(file_list[i][0]))
        t = join_team_models.team_info.objects.get(team_no=file_list[i][0])
        file_list[i].insert(0,str(i+1))
        file_list[i].insert(2,t.team_name)
        #file_list[i].insert(3,p.team_id)
        list_1.append(file_list[i])

    print(file_list)
    return render(request,"topic_details_2.html",{'list_1':list_1})



def change_que(request):
    new_question = request.POST['new_question']
    new_answer = request.POST['new_answer']
    user_id_1 = request.session['user_id']

    print(new_question)
    print(new_answer)
    user = Lmodels.normal_user.objects.get(user_no=user_id_1)
    user.security_question = new_question
    user.answer = new_answer
    user.save()
    info = "账号 "+user.user_name+" 您已经修改了密保问题和答案，请记住！！"
    info_models.system_info.objects.create(
        user_id = user,
        info_content = info
    )
    return render(request,"Personal_page_7.2.html")

def personal_page_7_2(request):
    return render(request,"Personal_page_7.2.html")

def personal_page_7_1(request):
    return render(request,"Personal_page_7.1.html")

def change_psw(request):
    user_id = request.session['user_id']
    new_psw = request.POST['new_psw']
    print("新的密码为 ：",new_psw)
    user = Lmodels.normal_user.objects.get(user_no=user_id)
    user.password = new_psw
    user.save()
    info = "账号 " + user.user_name + " 您已经修改了您的密码，请牢记！！"
    info_models.system_info.objects.create(
        user_id=user,
        info_content=info
    )

    return render(request,"Login.html")

def show_details_2(request,topic_id):
    com_topic = models.competition_topic.objects.get(com_topic_id=topic_id)
    participant_info = models.participant.objects.filter(user_id=request.session['user_id'])
    if(participant_info.count() == 0):
        request.session['is_sign'] = 0
    else:
        request.session['is_sign'] = 1

    user_id = request.session['user_id']
    # event_id = models.participant.objects.filter(user_id=user_id)[0].event_id
    ####TestA成绩单显示
    file_path_A = "D:\\DLCSY-version\\DLCSY-V0.0.4\\static\\score_record\\" + str(topic_id) + "A.csv"
    file_list_A = list(csv.reader(open(file_path_A, 'r')))
    print(file_list_A)
    list_1 = []

    for i in range(len(file_list_A)):
        # p = models.participant.objects.get(id = int(file_list[i][0]))
        t = join_team_models.team_info.objects.get(team_no=file_list_A[i][0])
        file_list_A[i].insert(0, str(i + 1))
        file_list_A[i].insert(2, t.team_name)
        # file_list[i].insert(3,p.team_id)
        list_1.append(file_list_A[i])

    ####TestB成绩单显示

    file_path_B = "D:\\DLCSY-version\\DLCSY-V0.0.4\\static\\score_record\\" + str(topic_id) + "B.csv"
    file_list_B = list(csv.reader(open(file_path_B, 'r')))
    print(file_list_B)
    list_2 = []

    for i in range(len(file_list_B)):
        # p = models.participant.objects.get(id = int(file_list[i][0]))
        t = join_team_models.team_info.objects.get(team_no=file_list_B[i][0])
        file_list_B[i].insert(0, str(i + 1))
        file_list_B[i].insert(2, t.team_name)
        # file_list[i].insert(3,p.team_id)
        list_2.append(file_list_B[i])
    return render(request, "topic_details_2.html", {'com_topic':com_topic,'list_A':list_1,'list_B':list_2})
    # return redirect("../look_score_B")

def show_details_1(request,topic_id):
    com_topic = models.competition_topic.objects.get(com_topic_id=topic_id)
    return render(request, "topic_details_1.html", {'com_topic':com_topic})



def goto_competitions_1(request):
    return render(request, "competitions_1.html")

def goto_competitions_2(request):
    return render(request, "competitions_2.html")

# def show_topic(request):
#     com_name = models.competition_topic.objects.all()
#     print(com_name)
#     return render(request, "../static/junk_file/Com_topic.html", {'com_name': com_name})

    # com_name_ser = serializers.serialize("json",models.competition_topic.objects.all().only("com_name"))
    # return render(request,"Com_topic.html",com_name_ser)

def to_sign_up(request,topic_id):
    user_id = request.session['user_id']
    flag = models.participant.objects.filter(user_id=user_id)
    flag_2 = models.pay_list.objects.filter(user_id=user_id)

    print("是否报过名", flag.count())
    if (flag.count() == 0 and flag_2.count() == 0):
        global money
        money = int(models.competition_topic.objects.get(com_topic_id=topic_id).money_to_pay)
        request.session['topic_id'] = topic_id
        return redirect("../pay_index")
    elif(flag.count() == 0 and flag_2.count() == 1):
        request.session['topic_id'] = topic_id
        return render(request,"before_sign_up.html")
    else:
        sign_up_error = '您已经完成了报名'
        news = news_models.article.objects.filter(type='新闻')
        announce = news_models.article.objects.filter(type='通知')
        return render(request,"Logined_Main.html",{'sign_up_error':sign_up_error,'news':news,'announce':announce})

def to_sign_up_2(request):
    event = request.session['topic_id']
    event_name = models.competition_topic.objects.get(com_topic_id=event).com_name
    return render(request,"Sign_up_page.html",{'event':event_name})

def to_sign_up_3(request):
    user_id = request.session['user_id']
    user = Lmodels.normal_user.objects.get(user_no=user_id)
    info_1 = "账号 " + user.user_name + " 您已完成报名付款，祝您比赛顺利！！"
    info_models.system_info.objects.create(
        user_id=user,
        info_content=info_1
    )

    models.pay_list.objects.create(
        user_id=user,
        pay_money=500
    )
    return render(request,"before_sign_up.html")




def sub_sign_up(request):
    user_id = request.session['user_id']
    print("用户名为： %s",user_id)
    # flag = models.participant.objects.filter(user_id=user_id)
    # print("是否报过名",flag.count())
    # if(flag.count() != 0):
    user_sub = Lmodels.normal_user.objects.get(user_no=user_id)
    real_name_sub = request.POST['real_name']
    sex_sub = request.POST['sex']
    if sex_sub == "1":
        sex_sub = "男"
    elif sex_sub == "2":
        sex_sub = "女"
    id_num_sub = request.POST['id']
    id_check = models.participant.objects.filter(id_num=id_num_sub)
    if(id_check.count() == 0):
        # address_sub = request.POST['address']
        str = request.POST['province'] + request.POST['city'] + request.POST['address_details']
        address_sub = str
        # event = request.POST['event']
        event = request.session['topic_id']
        print(event)
        event_sub = models.competition_topic.objects.get(com_topic_id=event)
        print(id_num_sub)

        models.participant.objects.create(
            user = user_sub,
            real_name = real_name_sub,
            sex = sex_sub,
            id_num = id_num_sub,
            address = address_sub,
            event = event_sub
        )
        news = news_models.article.objects.filter(type='新闻')
        announce = news_models.article.objects.filter(type='通知')
        sign_up_success = "报名成功！！"
        user = Lmodels.normal_user.objects.get(user_no=user_id)
        info = "账号 " + user.user_name + " 您已成功报名，参加队伍后即可正式开始比赛，祝您顺利！！"
        info_models.system_info.objects.create(
            user_id=user,
            info_content=info
        )
        request.session['is_sign'] = '1'
        return render(request, "Logined_Main.html",
                      {'news': news, 'announce': announce,'sign_up_success':sign_up_success})
    else:
        error_id = "该身份证号已经被注册过"
        return render(request,"Sign_up_page.html",{'error_id':error_id})
    # else:
    #     error_message = '您已经完成了报名'
    #     return render(request,"topic_details_1.html",{'error_message':error_message})

def personal_page_1(request):
    participant_info = models.participant.objects.filter(user_id=request.session['user_id'])

    if(participant_info.count() == 0):
        user_info = Lmodels.normal_user.objects.filter(user_no=request.session['user_id'])

        # error_1 = "您没报名，没有相关的个人信息，请先报名！！"
        # print(error_1)
        request.session['is_sign_up'] = "NO"
        return render(request, "Personal_page_1.html", {'user_info':user_info[0]})
    else:
        print(participant_info[0].real_name)
        email_0 = Lmodels.normal_user.objects.filter(user_no=request.session['user_id'])[0].email
        user_info = Lmodels.normal_user.objects.filter(user_no=request.session['user_id'])
        request.session['is_sign_up'] = "YES"
        return render(request, "Personal_page_1.html", {'participant_info':participant_info[0],'email':email_0,'user_info':user_info[0]})

def personal_page_2(request):
    user_id = request.session['user_id']
    participant_info = models.participant.objects.filter(user_id=request.session['user_id'])
    if(participant_info.count() == 0):
        error_2 = "你需要先报名参赛并参加队伍才能查看相关信息"
        news = news_models.article.objects.filter(type='新闻')
        announce = news_models.article.objects.filter(type='通知')
        return render(request, "competitions_2.html", {'news': news, 'announce': announce, 'error_2':error_2})
    else:
        team_no = participant_info[0].team_id
        print("teamno:",team_no)
        if(team_no != None):
            team_info = join_team_models.team_info.objects.get(team_no=team_no)
            person_info = team_info.person_info.all()
            print(person_info)
            topic_no = models.participant.objects.filter(user_id=request.session['user_id'])[0].event_id
            topic = models.competition_topic.objects.get(com_topic_id=topic_no).com_name
            return render(request, "Personal_page_2.html", {'team_info':team_info, 'person_info':person_info,
                                                            'topic_no':topic_no,'topic':topic})
        else:
            error_4 = "你需要先加入一个队伍"
            topic = models.participant.objects.filter(user_id=user_id)[0].event
            topic_no = models.participant.objects.filter(user_id=user_id)
            result = join_team_models.team_info.objects.filter(num_of_troops__lt=5, team_event=topic)
            return render(request,"Team.html",{'team_info': result, 'event_id': topic_no,'error_4':error_4})

def personal_page_3(request):
    user_id = request.session['user_id'];
    participant_info = models.participant.objects.filter(user_id=user_id)

    if(participant_info.count() == 0):
        error_3 = "您需要先报名参赛并参加队伍才能进行此操作"
        return render(request,"competitions_2.html",{'error_3':error_3})
    elif(participant_info[0].team_id == None):
        error_3 = "您需要先参加队伍才能查看队伍信息"
        return render(request, "competitions_2.html", {'error_3': error_3})
    else:
        submission_B = join_team_models.team_info.objects.get(team_no=participant_info[0].team_id).submission_B
        request.session['rest'] = int(3 - int(submission_B))
        return render(request, "Personal_page_3.html")

def personal_page_4(request):
    user_id = request.session['user_id']
    pay_list = models.pay_list.objects.filter(user_id=user_id)
    print(pay_list)
    return render(request, "Personal_page_4.html",{'pay_list':pay_list})

def personal_page_5(request):
    user_id = request.session['user_id']
    system_info = info_models.system_info.objects.filter(user_id=user_id).order_by('now_date')
    return render(request,"Personal_page_5.html",{'system_info':system_info})

def personal_page_6(request):
    user_id = request.session['user_id']
    a = models.participant.objects.filter(user_id=user_id)
    if(a.count() == 0):
        return render(request, "competitions_2.html")
    else:
        return render(request, "Personal_page_6.html",{'a':a[0]})

def save_address(request):
    user_id = request.session['user_id']

    str = request.POST['province'] + request.POST['city'] + request.POST['address_details']

    participant_address = models.participant.objects.get(user_id=user_id)
    participant_address.address = str
    participant_address.save()
    return render(request,"Personal_page_6.html",{'a':participant_address})




# 以下是支付宝的相关接口

def ali():
    # 沙箱环境地址：https://openhome.alipay.com/platform/appDaily.htm?tab=info
    app_id = "2016092500595639"

    # POST请求，用于最后的检测
    notify_url = "http://127.0.0.1:8000/back_urls/"
    # notify_url = "http://www.wupeiqi.com:8804/page2/"

    # GET请求，用于页面的跳转展示
    return_url ="http://127.0.0.1:8000/back_urls/"
    # return_url = "http://www.wupeiqi.com:8804/page2/"

    merchant_private_key_path = "static/RSA_KEY/app_private_2048.txt"
    alipay_public_key_path = "static/RSA_KEY/alipay_public_2048.txt"

    alipay = AliPay(
        appid=app_id,
        app_notify_url=notify_url,
        return_url=return_url,
        app_private_key_path=merchant_private_key_path,
        alipay_public_key_path=alipay_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
        debug=True,  # 默认False,
    )
    return alipay

def index(request):
    return render(request,'index.html')



def page1(request):

    money_pay = money
    print("page1完成_1")
    alipay = ali()
    print("page1完成_2")
    # 生成支付的url
    query_params = alipay.direct_pay(
        subject="深度学习竞赛",  # 商品简单描述
        out_trade_no="DLCSY" + str(time.time()),  # 商户订单号
        total_amount=int(money_pay),  # 交易金额(单位: 元 保留俩位小数)
    )

    pay_url = "https://openapi.alipaydev.com/gateway.do?{0}".format(query_params)
    print("page1完成_3")
    return redirect(pay_url)


def page2(request):
    print("0000000000000000000")
    alipay = ali()
    if request.method == "POST":
        print("11111111111111111")
        # 检测是否支付成功
        # 去请求体中获取所有返回的数据：状态/订单号
        from urllib.parse import parse_qs
        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)

        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]
        print(post_dict)

        sign = post_dict.pop('sign', None)
        status = alipay.verify(post_dict, sign)
        print('POST验证', status)
        return render(request,"Sign_up_page.html")

    else:
        print("222222")
        params = request.GET.dict()
        sign = params.pop('sign', None)
        status = alipay.verify(params, sign)
        print('GET验证', status)

        return redirect("../../goto_sign_up_3")