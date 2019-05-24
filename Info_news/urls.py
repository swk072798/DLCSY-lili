from django.urls import path, include
from Info_news import views

urlpatterns = [
    path('goto_news_1',views.goto_news_1),
    path('goto_news_2',views.goto_news_2),
    path('goto_Info_1',views.goto_Info_1),
    path('goto_Info_2',views.goto_Info_2),
    path('goto_details_1/<int:news_id>',views.goto_details_1),
    path('goto_details_2/<int:news_id>',views.goto_details_2),

]