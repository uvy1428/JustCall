from django.db import models


class Details(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_contact = models.CharField(max_length=12)
    job_title = models.CharField(max_length=20)
    job_desription = models.CharField(max_length=300)
    publish_date = models.DateField()
    schedule_date = models.DateTimeField()

    def __str__(self):
        return self.job_title


class Price(models.Model):
    detail_job_done = models.CharField(max_length=300)
    price_charge = models.IntegerField()
    job_dd = models.DateTimeField()

    def __str__(self) -> str:
        return self.detail_job_done
