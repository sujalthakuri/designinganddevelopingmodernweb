from django.db import models

# Create your models here.

class Users(models.Model):
	user_id = models.AutoField(primary_key = True)
	fname = models.CharField(max_length = 25)
	lname = models.CharField(max_length = 25)
	username = models.CharField(max_length = 50)
	email = models.CharField(max_length = 50)
	password = models.CharField(max_length = 32)
	bio = models.TextField(max_length = 500)
	image = models.ImageField(default = 'profile.jpg')
	class Meta:
		db_table = "Users"
	def __str__(self):
		return self.username


class image(models.Model):
	image_id = models.AutoField(primary_key = True)
	image = models.ImageField(upload_to='images/', default = 'profile.jpg')
	user_id = models.IntegerField()
	class Meta:
		db_table = "Image"
	def __str__(self):
		return self.image_id

class admin(models.Model):
	admin_id = models.AutoField(primary_key = True)
	fname = models.CharField(max_length = 25)
	lname = models.CharField(max_length = 25)
	adminname = models.CharField(max_length = 25)
	password = models.CharField(max_length = 32)
	class Meta:
		db_table = "admin"
	def __str__(self):
		return self.admin_id

class follow(models.Model):
	follow_id = models.AutoField(primary_key = True)
	user_id = models.IntegerField()
	profile_id = models.IntegerField()
	class Meta:
		db_table = "follow"
	def __str__(self):
		return self.follow_id


