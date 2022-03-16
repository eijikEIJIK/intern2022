from email.policy import default
from django.conf import settings
from django.db import models

# Create your models here.


class Work(models.Model):
    title = models.CharField('タイトル', max_length=128)
    company = models.ForeignKey(settings.AUTH_USER_MODEL,
                                verbose_name='企業',
                                on_delete=models.CASCADE)
    salary_max = models.IntegerField()
    salary_min = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    user= models.ForeignKey(settings.AUTH_USER_MODEL,
                                verbose_name='応募者',
                                on_delete=models.CASCADE)
    work= models.ForeignKey(Work,
                                verbose_name='求人',
                                on_delete=models.SET_NULL,
                                null=True)
    is_passed=models.BooleanField(verbose_name='合否',
                                            null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields=["user","work"],
                name="application_unique"
            ),
        ]