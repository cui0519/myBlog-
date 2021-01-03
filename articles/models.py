from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=128,verbose_name="文章标题")
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="文章作者")
    img = models.ImageField(upload_to="", blank=True,null=True,verbose_name="文章配图")
    abstract = models.TextField(verbose_name="文章摘要")
    content = models.TextField(verbose_name="文章内容")
    visited = models.IntegerField(default=0,verbose_name="文章访问量")
    visited = models.IntegerField(default=0,verbose_name="文章访问量")
    modified_at = models.DateTimeField(auto_now=True,verbose_name="修改时间")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ('-created_at',)

def __str__(self):
    return self.title