from django.db import models

# Create your models here.
class toDo(models.Model):
  title=models.CharField( max_length=50)
  description=models.CharField( max_length=50)
  created_at=models.DateTimeField(auto_now=True)
  updated_at=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  class Meta:
    verbose_name_plural="Title"