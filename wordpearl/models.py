from django.db import models

class Oyster(models.Model):
  oyster_id = models.AutoField
  username = models.CharField(max_length=50)
  avatar_url = models.CharField(max_length=500)

class Pearl(models.Model):
  pearl_id = models.AutoField
  username = models.ForeignKey(Oyster, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  body = models.CharField
  created_at = models.DateField()
  votes = models.IntegerField()

class Comment(models.Model):
  comment_id = models.AutoField
  body = models.CharField
  pearl_id = models.ForeignKey(Pearl, on_delete=models.CASCADE)
  username = models.ForeignKey(Oyster, on_delete=models.CASCADE)
  created_at = models.DateField()
  votes = models.IntegerField()