from django.db import models
from django.contrib.auth.models import User


# DEFAULT_USER = User.objects.get(username="default-user")
# DEFAULT_USER_ID = DEFAULT_USER.id


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200, null=False, blank=False)
    link = models.URLField(blank=False, null=False, unique=True)
    date_published = models.DateTimeField(auto_now_add=True)
    upvote = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_published']


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    content = models.TextField(max_length=5000, null=False, blank=False)
    date_published = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-date_published']


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
