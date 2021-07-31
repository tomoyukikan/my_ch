from django.db import models

# Create your models here.
class Post(models.Model):

  post = models.TextField(verbose_name="投稿", blank=True, null=True)

  created_at = models.DateTimeField(verbose_name = '作成日時', auto_now_add=True)

  class Meta:
    verbose_name = "Post"
    verbose_name_plural = "Posts"

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse("Post_detail", kwargs={"pk": self.pk})