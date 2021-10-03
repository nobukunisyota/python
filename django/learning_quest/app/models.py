from django.db import models
from django.contrib.auth import get_user_model


class RewardTable(models.Model):
    class Meta:
        db_table = 'rewards'

    reward = models.CharField(max_length=100)
    reward_required_time = models.IntegerField()
    username = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.reward


class StudyTime(models.Model):
    class Meta:
        db_table = 'study_time'

    total_time = models.IntegerField(default=0)
    username = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
    )

