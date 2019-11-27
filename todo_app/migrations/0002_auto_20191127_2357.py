# Generated by Django 2.1.7 on 2019-11-27 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bucketlist',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id_bucket', to='todo_app.UserAccount'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='bucket_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bucket_id_todo', to='todo_app.BucketList'),
        ),
    ]
