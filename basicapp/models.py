from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    ssn = models.IntegerField(max_length=9)
    dob = models.DateField()
    address = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username
