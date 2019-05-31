from django.shortcuts import render
from Info_news import models
from sign_up import models as sign_up_models
# Create your views here.

def goto_news_1(request):
    news_obj = models.article.objects.filter(type='新闻').order_by('ar_time')
    return render(request, "Com_news_1.html", {'news_obj':news_obj})

def goto_news_2(request):
    news_obj = models.article.objects.filter(type='新闻').order_by('ar_time')
    return render(request, "Com_news_2.html", {'news_obj':news_obj})

def goto_Info_1(request):
    Info_obj = models.article.objects.filter(type='通知').order_by('ar_time')
    return render(request, "Com_Info_1.html", {'Info_obj':Info_obj})

def goto_Info_2(request):
    Info_obj = models.article.objects.filter(type='通知').order_by('ar_time')
    return render(request, "Com_Info_2.html", {'Info_obj':Info_obj})

def goto_details_1(request,news_id):
    print(news_id)
    id = news_id
    title = models.article.objects.get(id=id).title
    content = models.article.objects.get(id=id).content
    print(content)
    date = models.article.objects.get(id=id).ar_time
    return render(request, "Consititution_details_1.html", {'title':title, 'content':content, 'date':date})

def goto_details_2(request,news_id):
    print(news_id)
    id = news_id
    title = models.article.objects.get(id=id).title
    content = models.article.objects.get(id=id).content
    print(content)
    date = models.article.objects.get(id=id).ar_time
    TestA_open_date = ""
    TestB_open_date = ""
    if(news_id == 625):
        TestA_open_date = sign_up_models.competition_topic.objects.get(com_topic_id=1).TestA_open_time
        TestB_open_date = sign_up_models.competition_topic.objects.get(com_topic_id=1).TestB_open_time
    return render(request, "Consititution_details_2.html", {'title':title, 'content':content, 'date':date,
                                                            'TestA_open_date':TestA_open_date,'TestB_open_date':TestB_open_date})