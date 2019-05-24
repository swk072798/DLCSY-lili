"""DLCSY URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path
from sign_up import views

urlpatterns = [
    # path('show_topic', views.show_topic),
    path('goto_sign_up/<int:topic_id>',views.to_sign_up),
    path('goto_sign_up_2',views.to_sign_up_2),
    path('goto_sign_up_3',views.to_sign_up_3),
    path('sub_sign_up',views.sub_sign_up),
    path('goto_competitions_1',views.goto_competitions_1),
    path('goto_competitions_2',views.goto_competitions_2),
    path('show_details_1/<int:topic_id>',views.show_details_1),
    path('show_details_2/<int:topic_id>', views.show_details_2),
    path('goto_personal_1',views.personal_page_1),
    path('goto_personal_2',views.personal_page_2),
    path('goto_personal_3',views.personal_page_3),
    path('goto_personal_4',views.personal_page_4),
    path('goto_personal_5',views.personal_page_5),
    path('goto_personal_6',views.personal_page_6),
    path('save_address',views.save_address),
    path('pay_index',views.page1),
    path('back_urls/',views.page2),
    path('goto_personal_7_1',views.personal_page_7_1),
    path('goto_personal_7_2',views.personal_page_7_2),
    path('change_psw',views.change_psw),
    path('change_que',views.change_que),
    path('look_score_B',views.score_list_B),
    # path('update_order',views.update_order),


]
