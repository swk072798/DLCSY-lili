from django.urls import path
from download_res import views

urlpatterns = [
    path('go_to_download',views.go_to_download),
    path('download_file/<int:com_topic_id>/<int:set_no>',views.download_file),
    path('uploadfile_A',views.upload_file_A),
    path('uploadfile_B',views.upload_file_B),
    path('goto_download_study_1',views.goto_down_study_resource_1),
    path('goto_download_study_2', views.goto_down_study_resource_2),
    path('get_score_A',views.run_file_A),
    path('get_score_B',views.run_file_B),
    path('goto_watch_video',views.goto_watch_study_viedo),
    path('change_video/<int:id>',views.change_video),
]