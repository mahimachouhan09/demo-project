# Generated by Django 3.0.2 on 2020-02-05 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('quora_app', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('U', 'Up Vote'), ('D', 'Down Vote')], max_length=1)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quora_app.Profile')),
            ],
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='question',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='user',
        ),
        migrations.DeleteModel(
            name='DownVote',
        ),
        migrations.DeleteModel(
            name='UpVote',
        ),
    ]
