# Generated by Django 2.2.2 on 2019-07-02 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('private', 'private'), ('group', 'group'), ('supergroup', 'supergroup'), ('channel', 'channel')], max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_id', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('text', models.CharField(blank=True, max_length=4096)),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='heroku.Chat')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('is_bot', models.BooleanField()),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(blank=True, max_length=64)),
                ('username', models.CharField(blank=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_id', models.IntegerField()),
                ('message', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='update', to='heroku.Message')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='from_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='heroku.User'),
        ),
    ]