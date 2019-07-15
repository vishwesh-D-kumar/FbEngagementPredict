from django.db import models

# Create your models here.
class Mainsite(models.Model):
	siteurl=models.CharField(max_length=100)
	crawled=models.BooleanField(default=False)
	lastcrawled=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.siteurl
class Subsites(models.Model):
	subsiteurl=models.CharField(max_length=1000)
	mainsite=models.ForeignKey(Mainsite, on_delete=models.CASCADE)

	def __str__(self):
		return self.subsiteurl
