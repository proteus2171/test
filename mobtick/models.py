from django.db import models

# Create your models here.
class ticket(models.Model):
    timestamp = models.DateField(auto_now_add=True,auto_now=False,)
    tech = models.CharField(max_length=50,)
    site = models.CharField(max_length=50,)
    user = models.CharField(max_length=50,)
    issue = models.CharField(max_length=200,)
    tickid = models.AutoField(primary_key=True)
    complete = models.BooleanField()
    reqact = models.CharField(max_length=200, blank=True,)

    def __unicode__(self):
        return self.site