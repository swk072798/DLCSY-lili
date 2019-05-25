from django.shortcuts import render,redirect
from django.http import StreamingHttpResponse, HttpResponse
from sign_up import models as sign_up_models
import os
import static.score_1 as score
import csv
import operator
from Info_news.models import study_resource as sr
from login.models import normal_user as Lmodels
from Info_news.models import system_info
from download_res import models
from join_team import models as join_team_models

# Create your views here.

def change_video(request,id):
    video_list_1 = models.video.objects.filter(video_type="python")
    video_list_2 = models.video.objects.filter(video_type="深度学习")
    video_list_3 = models.video.objects.filter(video_type="图像处理")
    video_list = models.video.objects.all()
    now_video = str(models.video.objects.filter(id=id)[0].video_urls)
    print(now_video)
    return render(request,"study_video.html",{'video_list':video_list,'now_play':now_video,
                                              'video_list_1':video_list_1,'video_list_2':video_list_2,
                                              'video_list_3':video_list_3})

def goto_watch_study_viedo(request):
    video_list_1 = models.video.objects.filter(video_type="python")
    video_list_2 = models.video.objects.filter(video_type="深度学习")
    video_list_3 = models.video.objects.filter(video_type="图像处理")
    return render(request,"study_video.html",{'video_list_1':video_list_1,'video_list_2':video_list_2,
                                              'video_list_3':video_list_3})

def goto_down_study_resource_2(request):
    study_info_1 = sr.objects.filter(type='学习')
    study_info_2 = sr.objects.filter(type='论文')

    return render(request, "Tutorials_2.html", {"study_info_1": study_info_1, "study_info_2": study_info_2})


def goto_down_study_resource_1(request):
    study_info_1 = sr.objects.filter(type='学习')
    study_info_2 = sr.objects.filter(type='论文')

    return render(request, "Tutorials_1.html",{"study_info_1":study_info_1,"study_info_2":study_info_2})


def go_to_download(request):
    # result = sign_up_models.competition_topic.objects.all()
    participant = sign_up_models.participant.objects.filter(user_id=request.session['user_id'])
    print(participant)

    if(participant.count() == 0):
        return render(request, "competitions_2.html",{'data_donload_error':"您需要先报名才能查看数据集"})
    else:
        urls = "../../show_details_2/"+str(participant[0].event_id)
        return redirect(urls)



def download_file(request,com_topic_id,set_no):
    # do something
    # try:
    the_file_name = 'data_set.txt'  # 显示在弹出对话框中的默认的下载文件名
    print(the_file_name)
    if(set_no == 1):
        the_file_name = 'data_set_Train.txt'
        filename = sign_up_models.competition_topic.objects.get(com_topic_id=com_topic_id).data_set_file_trainnig  # 要下载的文件路径
        print(filename)
        response = StreamingHttpResponse(open(filename,'rb'))
        response['Content-Type'] = 'text/html'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    elif(set_no == 2):
        the_file_name = 'data_set_A.txt'
        filename = sign_up_models.competition_topic.objects.get(com_topic_id=com_topic_id).data_set_file_A  # 要下载的文件路径
        print(filename)
        response = StreamingHttpResponse(open(filename, 'rb'))
        response['Content-Type'] = 'text/html'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    elif(set_no == 3):
        the_file_name = 'data_set_B.txt'
        filename = sign_up_models.competition_topic.objects.get(com_topic_id=com_topic_id).data_set_file_B  # 要下载的文件路径
        print(filename)
        response = StreamingHttpResponse(open(filename, 'rb'))
        response['Content-Type'] = 'text/html'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response

def upload_file_A(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        user_id = request.session['user_id']
        par_no = sign_up_models.participant.objects.get(user_id=user_id)
        submission = join_team_models.team_info.objects.get(team_no=int(par_no.team_id))
        upload_path= "static\\participants\\"+str(par_no.event_id)+"\\A\\"+str(par_no.team_id)
        if(os.path.exists(upload_path)):
            # print("111")
            destination = open(os.path.join(upload_path,myFile.name),'wb+')
            print(myFile.name)
            # 打开特定的文件进行二进制的写操作
            for chunk in myFile.chunks():      # 分块写入文件
                destination.write(chunk)
            destination.close()
            submission.submission_A += 1
            submission.save()
            # return render(request,"Personal_page_3.html")
            return redirect("../get_score_A")
        else:
            # print("222")
            os.mkdir(upload_path)
            destination = open(os.path.join(upload_path, myFile.name), 'wb+')
            print(myFile.name)
            # 打开特定的文件进行二进制的写操作
            for chunk in myFile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            submission.submission_A += 1
            submission.save()
            # return render(request, "Personal_page_3.html")
            return redirect("../get_score_A")

def upload_file_B(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        user_id = request.session['user_id']
        par_no = sign_up_models.participant.objects.get(user_id=user_id)
        print(par_no)
        upload_path= "static\\participants\\"+str(par_no.event_id)+"\\B\\"+str(par_no.team_id)
        # print(par_no.user_id)
        #判断文件是否上传过，如果无，则上传，如果有，则提醒用户不能重复上传
        submission = join_team_models.team_info.objects.get(team_no=int(par_no.team_id))
        print("submission")
        if(os.path.exists(upload_path) and int(submission.submission_B)<3):
            # return render(request,"Personal_page_3.html",{'error':"禁止重复上传"})
            destination = open(os.path.join(upload_path, myFile.name), 'wb+')
            print(myFile.name)
            # 打开特定的文件进行二进制的写操作
            for chunk in myFile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            submission.submission_B += 1
            submission.save()
            rest = 3-submission.submission_B
            user = Lmodels.objects.get(user_no=user_id)
            info = "账号 " + user.user_name + " 您已提交TestB程序，点击下方查看成绩和排名可以查看小队成绩，或者在官网" \
                                            "首页的成绩榜单中查询！！"
            system_info.objects.create(
                user_id=user,
                info_content=info
            )
            # return render(request, "Personal_page_3.html",{"rest":rest})
            request.session['rest'] = rest
            return redirect("../get_score_B")
        elif(os.path.exists(upload_path) == False and int(submission.submission_B)<3):

            os.mkdir(upload_path)
            destination = open(os.path.join(upload_path,myFile.name),'wb')
            print(myFile.name)
            # 打开特定的文件进行二进制的写操作
            for chunk in myFile.chunks():      # 分块写入文件
                destination.write(chunk)
            destination.close()
            user = Lmodels.objects.get(user_no=user_id)
            info = "账号 " + user.user_name + " 您已提交TestB程序，点击下方查看成绩和排名可以查看小队成绩，或者在官网" \
                                            "首页的成绩榜单中查询！！"
            system_info.objects.create(
                user_id=user,
                info_content=info
            )
            submission.submission_B += 1
            submission.save()
            rest = 3-submission.submission_B
            request.session['rest'] = rest
            return redirect("../get_score_B")
        elif(int(submission.submission_B)>=3):
            return render(request,"Personal_page_3.html",{'error':"无法继续提交"})


def run_file_A(request):
    user_id = request.session['user_id']
    par_no = sign_up_models.participant.objects.get(user_id=user_id)
    max_submission_A = sign_up_models.competition_topic.objects.get(com_topic_id=par_no.event_id).TestA_max_upload_times
    team_info = join_team_models.team_info.objects.get(team_no=par_no.team_id)
    submitfile = "D:\\DLCSY-version\\DLCSY-V0.0.4\\static\\participants\\"+str(par_no.event_id)+"\\A\\"+str(par_no.team_id)+"\\submit.csv"
    listfile = "D:\\DLCSY-version\\DLCSY-V0.0.4\\static\\standard_answer\\"+str(par_no.event_id) +"\\list.csv"

    your_score = score.caculate_score(submitfile,listfile)
    print("我的成绩是：",your_score)

    file_path = "./static/score_record/" + str(par_no.event_id) + "A.csv"
    file_list = list(csv.reader(open(file_path,'r')))

    if(your_score == "file not exist"):
        return render(request,"Personal_page_3.html",{'error':"file not exist"})
    else:
       if(max_submission_A == 0):
        your_score_percent = str(your_score * 100) + "%"
        # file_path = "./static/score_record/" + str(par_no.event_id) + "A.csv"
        info = [str(par_no.team_id), str(your_score)]
        csv_file = open(file_path, 'w+', newline='')

        if (info in file_list):
            pass
        else:
            file_list.append(info)
        file_list.sort(key=operator.itemgetter(1), reverse=True)
        csv_writer = csv.writer(csv_file, dialect='excel')
        print(file_list)
        print(len(file_list))

        for i in range(0, len(file_list)):
            csv_writer.writerow(file_list[i])

        index = 0
        for j in range(0, len(file_list)):
            if (file_list[j][0] == str(par_no.team_id)):
                index = j + 1
        print(index)
        csv_file.close()

        return render(request, "Personal_page_3.html", {'your_score_A': your_score_percent, 'index_A': index})

       elif(int(team_info.submission_A) <int(max_submission_A)):
           your_score_percent = str(your_score * 100) + "%"
           # file_path = "./static/score_record/" + str(par_no.event_id) + "A.csv"
           info = [str(par_no.team_id), str(your_score)]
           csv_file = open(file_path, 'w+', newline='')

           if (info in file_list):
               pass
           else:
               file_list.append(info)
           file_list.sort(key=operator.itemgetter(1), reverse=True)
           csv_writer = csv.writer(csv_file, dialect='excel')
           print(file_list)
           print(len(file_list))

           for i in range(0, len(file_list)):
               csv_writer.writerow(file_list[i])

           index = 0
           for j in range(0, len(file_list)):
               if (file_list[j][0] == str(par_no.team_id)):
                   index = j + 1
           print(index)
           csv_file.close()
           return render(request, "Personal_page_3.html", {'your_score_A': your_score_percent, 'index_A': index})
       else:
           error = "您的TestA提交次数不足"
           return render(request,"Personal_page_3.html",{'error_message_A':error})


def run_file_B(request):
    user_id = request.session['user_id']
    par_no = sign_up_models.participant.objects.get(user_id=user_id)

    submitfile = "D:\\DLCSY-version\\DLCSY-V0.0.4\\static\\participants\\"+str(par_no.event_id)+"\\B\\" + str(par_no.team_id) + "\\submit.csv"
    # listfile = "D:\\DLCSY-version\\DLCSY-V0.0.4\\static\\standard_answer\\" + str(par_no.event_id) + "\\list.csv"
    listfile = "D:\\DLCSY-version\\DLCSY-V0.0.4\\static\\standard_answer\\1\\list.csv"#标准答案和算法全都采用题目一的规则进行计算

    your_score = score.caculate_score(submitfile, listfile)
    print("我的成绩是：", your_score)

    file_path = "./static/score_record/" + str(par_no.event_id) + "B.csv"
    file_list = list(csv.reader(open(file_path, 'r')))

    if (your_score == "file not exist"):
        return render(request, "Personal_page_3.html", {'error': "file not exist"})
        # return {'your_score_B':your_score}
    else:
        # submission = join_team_models.team_info.objects.get(team_no=par_no.team_id).submission
        # if(int(submission)<3):
        your_score_percent = str(your_score * 100) + "%"
        file_path = "./static/score_record/" + str(par_no.event_id) + "B.csv"
        info = [str(par_no.team_id), str(your_score)]
        csv_file = open(file_path,'w+',newline='')
        if(info in file_list):
            pass
        else:
            file_list.append(info)
        file_list.sort(key=operator.itemgetter(1),reverse=True)
        csv_writer = csv.writer(csv_file,dialect='excel')
        print(file_list)
        print(len(file_list))

        for i in range(0,len(file_list)):

            csv_writer.writerow(file_list[i])

        index = 0
        for j in range(0,len(file_list)):
            if(file_list[j][0] == str(par_no.team_id)):
                index = j+1
        print(index)
        csv_file.close()
        # result_list = {'your_score_B': your_score_percent, 'index_B': index}
        # return result_list
        return render(request, "Personal_page_3.html", {'your_score_B': your_score_percent,'index_B':index})
        # else:
        #     return render(request,"Personal_page_3.html",{'error_message'})