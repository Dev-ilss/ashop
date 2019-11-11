from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)
		img = Image.open(self.image.path)
		if img.height > 512 or img.width > 512:
			output_size = (512, 512)
			img.thumbnail(output_size)
			img.save(self.image.path)