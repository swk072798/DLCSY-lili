from django.urls import path
from join_team import views

urlpatterns = [
    path('show_team',views.show_team),
    path('join_in_team/<int:team_no>',views.join_in_team),
    # path('back',views.back_main),
    path('create_team',views.create_team),
    path('go_to_create',views.go_to_create),
    path('goto_L_Main',views.goto_L_Main),
]