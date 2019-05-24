from django.contrib import admin
from sign_up.models import competition_topic,participant,pay_list
# Register your models here.
admin.site.register(competition_topic)
admin.site.register(participant)
admin.site.register(pay_list)