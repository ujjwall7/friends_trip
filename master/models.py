from django.db import models
from django.contrib.auth.models import AbstractUser


def webp(instance, filename):
    if filename.find('.') >= 0:
        dot_index = (len(filename) - filename.rfind('.', 1)) * (-1)
        filename = filename[0:dot_index]
    filename = '{}.{}'.format(filename, 'webp')
    return filename

USER_ROLES = (('Admin','Admin'),('User','User'))

class User(AbstractUser):
    identity    = models.UUIDField(null=True)
    mobile      = models.CharField(max_length=15,null=True,unique = True)
    profile     = models.ImageField(upload_to=webp,blank=True)
    role        = models.CharField(max_length=50, choices=USER_ROLES,default='User')

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if not self.pk and not self.is_password_hashed(self.password):
            self.set_password(self.password)
        elif self.pk and not self.check_password(self.password):
            if not self.is_password_hashed(self.password):
                self.set_password(self.password)
        super().save(*args, **kwargs)

    def is_password_hashed(self, password):
        return password.startswith('pbkdf2_')

class Trip(models.Model):
    name       = models.CharField(max_length=250)
    start_date = models.DateField(auto_now_add=False)
    end_date   = models.DateField(auto_now_add=False)
    user       = models.ManyToManyField(User, related_name='user')
    trip_complete = models.BooleanField(default=False)  

    def __str__(self):
        return self.name
    

class Expense(models.Model):
    trip                = models.ForeignKey(Trip, related_name='trip', on_delete=models.CASCADE)
    pay_user            = models.ForeignKey(User, related_name='pay_user', on_delete=models.CASCADE)
    user_distributed    = models.ManyToManyField(User, related_name='user_distributed')
    price               = models.IntegerField()
    price_distibuted    = models.IntegerField()
    image               = models.ImageField(upload_to=webp,blank=True)
    description         = models.TextField(blank=True)

class PersonalExpense(models.Model):
    user        = models.ForeignKey(User, related_name='self_user',on_delete=models.CASCADE)
    image       = models.ImageField(upload_to=webp)
    description = models.TextField()  
    price       = models.IntegerField()

# class UserPaid(models.Model):
#     user = models.ForeignKey(User, related_name='self_user',on_delete=models.CASCADE)
