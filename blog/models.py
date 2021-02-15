from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	


	def __str__(self):
		return self.title
	##Not get_absolute_url i a method inside  models.Model
	def get_absolute_url(self):
		return reverse('create-post')
		# bu kisim  esasinda POst model cagirildiktan sonra geliyor ama 
		return reverse('post-detail',kwargs={'pk':self.pk})
		return reverse('post-update',kwargs={'pk':self.pk})
		
		return reverse('post-delete', kwargs={'pk':self.pk})
