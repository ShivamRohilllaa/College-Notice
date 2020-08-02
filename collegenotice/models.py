from django.db import models

# Create your models here.
class branch(models.Model):
    name = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class notice(models.Model):
    notice_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    msg = models.TextField(max_length=1000)
    cr_date = models.DateTimeField(auto_now_add=True)
    branch = models.ForeignKey(branch, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.subject

    


    