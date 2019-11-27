from django.db import models


class UserAccount(models.Model):
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=20,null=True)
    email_id = models.EmailField(max_length=320)
    password = models.CharField(max_length=200)


class BucketList(models.Model):
    bucket_name = models.CharField(max_length=255, null=True)
    user_id = models.ForeignKey(UserAccount, related_name='user_id_bucket', on_delete=models.CASCADE)


class TodoList(models.Model):
    todo_name = models.CharField(max_length=255, null=True)
    is_done = models.BooleanField(default=0)
    bucket_id = models.ForeignKey(BucketList, related_name='bucket_id_todo', on_delete=models.CASCADE)