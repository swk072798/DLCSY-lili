from django.db import models

# Create your models here.

class team_info(models.Model):
    team_no = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=50,null=True)
    num_of_troops = models.IntegerField(null=True)
    captain = models.CharField(max_length=10,null=True)
    # team_event = models.ManyToManyField("sign_up.competition_topic")
    team_event = models.ForeignKey("sign_up.competition_topic",on_delete=models.CASCADE,default='')
    # person_info = models.ForeignKey("sign_up.participant",on_delete=models.CASCADE,default='')
    person_info = models.ManyToManyField("sign_up.participant")
    submission_B = models.IntegerField( default="0")
    submission_A = models.IntegerField(default="0")

