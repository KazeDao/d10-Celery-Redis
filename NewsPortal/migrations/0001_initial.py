# Generated by Django 4.1.1 on 2022-09-15 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('sport', 'спорт'), ('politics', 'политика'), ('education', 'образование'), ('economics', 'экономика')], default='economics', max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(choices=[('news', 'Новости'), ('articles', 'Статьи')], default='news', max_length=20)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('post_title', models.CharField(max_length=50)),
                ('post_text', models.TextField(blank=True)),
                ('post_rating', models.IntegerField(default=0)),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPortal.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_name', models.CharField(max_length=20)),
                ('pc_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPortal.category')),
                ('pc_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPortal.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='post_categories',
            field=models.ManyToManyField(through='NewsPortal.PostCategory', to='NewsPortal.category'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm_text', models.TextField(blank=True)),
                ('comm_time', models.DateTimeField(auto_now_add=True)),
                ('comm_rating', models.FloatField(default=0.0)),
                ('comm_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPortal.post')),
            ],
        ),
    ]