from django.shortcuts import render,redirect
from join_team import models
from sign_up import models as sign_up_models
import json
from django.http import JsonResponse,HttpResponse
from Info_news import models as news_models
from login.models import normal_user as Lmodels
# Create your views here.

def goto_L_Main(request):
    news = news_models.article.objects.filter(type='新闻')
    announce = news_models.article.objects.filter(type='通知')
    return render(request, "Logined_Main.html", {'news': news, 'announce': announce})

def show_team(request):
    user_id = request.session['user_id']
    sign = sign_up_models.participant.objects.filter(user_id=user_id)
    error_1 = ""
    if(sign.count() != 0):
        my_team = sign[0].team_id
        if(my_team == None):
            topic = sign_up_models.participant.objects.filter(user_id=user_id)[0].event
            topic_no = sign_up_models.participant.objects.filter(user_id=user_id)
            print(topic_no)
            result = models.team_info.objects.filter(num_of_troops__lt=5, team_event=topic)
            return render(request, "Team.html", {'team_info': result, 'event_id': topic_no})
        else:

            error_1 = "您已经有了队伍"
            print("您已经有了队伍",my_team)
            news = news_models.article.objects.filter(type='新闻')
            announce = news_models.article.objects.filter(type='通知')
            return render(request,"Logined_Main.html",{'error_1':error_1,'news': news, 'announce': announce})

    else:
        error_1 = "您需要先报名参赛再选择队伍"
        news = news_models.article.objects.filter(type='新闻')
        announce = news_models.article.objects.filter(type='通知')
        return render(request, "competitions_2.html", {'error_1': error_1, 'news': news, 'announce': announce})



def join_in_team(request,team_no):
    print("team_no:%s",team_no)
    user_id = request.session['user_id']
    if (models.team_info.objects.get(team_no=team_no).num_of_troops < 5):
        print("team_no:%s", team_no)
        participant_id = request.session['user_id']
        print(participant_id)
        p = sign_up_models.participant.objects.get(user_id=participant_id)  #获取参赛者信息
        team_search = models.team_info.objects.get(team_no=team_no)

        p.team_info_set.set([team_search])
        print("team_no:%s", team_no)
        team_search.participant_set.set([p])
        team_search.save()
        p.save()
        print("team_no:%s", team_no)
        people = models.team_info.objects.get(team_no=team_no)
        p1 = people.person_info.all().count()
        print("people:",p1)

        models.team_info.objects.filter(team_no=team_no).update(num_of_troops = p1)
        message = "加入队伍成功！"

        user = Lmodels.normal_user.objects.get(user_no=user_id)
        info = "账号 " + user.user_name + " 您已成功报名，参加队伍后即可正式开始比赛，祝您比赛顺利！！"
        news_models.system_info.objects.create(
            user_id=user,
            info_content=info
        )

        return render(request,"Logined_Main.html",{'join_team_message':message})
    else:
        message =  "出错啦！！"
        return render(request,"Logined_Main.html",{'message':message})

    # team_no = request.team_no

def create_team(request):
    user_id = request.session['user_id']
    team_name = request.POST['team_name']
    #captain_name = request.POST['captain_name']
    participant = sign_up_models.participant.objects.get(user_id=request.session['user_id'])
    participant_event = participant.event
    team = models.team_info.objects.create(team_name=team_name,captain=participant.real_name,num_of_troops=1,team_event=participant_event)
    print("team.team_no:",team.team_no)
    # team_id_time = models.team_info.objects.get(team_name=team_name,captain=captain_name,num_of_troops=1).team_no
    team_search = models.team_info.objects.get(team_no=team.team_no)
    # print("team_search：",team_search)

    # team_search.participant_set.set([participant])
    team_search.person_info.add(participant.id)
    team_search.save()

    p = sign_up_models.participant.objects.get(user_id=user_id)
    print("ppp:",p)
    team_search_1 = models.team_info.objects.filter(team_no=team.team_no)
    p.team = team_search        #修改ForeignKey的值
    p.save()

    user = Lmodels.objects.get(user_no=user_id)
    info = "账号 " + user.user_name + " 您已创建了新的队伍，祝您比赛顺利！！"
    news_models.system_info.objects.create(
        user_id=user,
        info_content=info
    )

    return redirect("../goto_personal_2")

def go_to_create(request):
    real_name = sign_up_models.participant.objects.filter(user_id=request.session['user_id'])[0].real_name
    return render(request,"Create_team.html",{'real_name':real_name})


