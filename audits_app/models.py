from django.db import models

class Audit(models.Model):
    audit_name = models.CharField(max_length=200)
    sched_date = models.DateTimeField(blank=True, null=True)

# Create your models here.
