from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class ArticlePost(models.Model):
    # on_delete 用于指定数据删除的方式，CASCADE为级联删除，即删除作者，对应的文章也会随着一起删除
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # CharField 为字符串字段，用于保存较短的字符串
    title = models.CharField(max_length=100)
    # 保存大量文本用 TextField
    body = models.TextField()
    # default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)
    # auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
