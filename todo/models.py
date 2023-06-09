from django.db import models
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(max_length=500, verbose_name='Description')
    completed = models.BooleanField(default=False, verbose_name='Complete ?')
    created_at = models.DateField(auto_now_add=True)
    user =  models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['completed', 'created_at']
