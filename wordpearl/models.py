from django.db import models

class Oyster(models.Model):
  oyster_id = models.AutoField
  points = models.IntegerField()
  password = models.CharField(max_length=50)
  username = models.CharField(max_length=50)
  avatar_url = models.CharField(max_length=500)
  def __str__(self):
        return self.username

class Pearl(models.Model):
  pearl_id = models.AutoField
  username = models.ForeignKey(Oyster, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  body = models.CharField(max_length=1000)    ##  added a max-length because it didnt show otherwise
  created_at = models.DateField()
  votes = models.IntegerField()
  def __str__(self):
        return self.title

class Comment(models.Model):
  comment_id = models.AutoField
  body = models.CharField(max_length=1000)    ##  added a max-length because it didnt show otherwise
  pearl_id = models.ForeignKey(Pearl, on_delete=models.CASCADE)
  username = models.ForeignKey(Oyster, on_delete=models.CASCADE)
  created_at = models.DateField()
  votes = models.IntegerField()