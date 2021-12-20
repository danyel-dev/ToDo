from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
