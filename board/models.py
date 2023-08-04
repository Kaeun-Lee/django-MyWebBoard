from django.db import models


class Boards(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="date published"
    )
    updated_date = models.DateTimeField(auto_now=True, verbose_name="date updated")
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comments(models.Model):
    writer = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name="date published"
    )
    board = models.ForeignKey(Boards, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
