# Generated by Django 3.2.7 on 2021-09-21 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default-picture.png', null=True, upload_to='articles/')),
                ('title', models.CharField(max_length=100)),
                ('excerpt', models.TextField(max_length=250, null=True)),
                ('slug', models.SlugField(editable=False, max_length=100, unique=True)),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='poster', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(editable=False, related_name='article_like', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraphs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='articles/par/')),
                ('quote', models.TextField(blank=True, max_length=250, null=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='articles.article', verbose_name='Абзацы:')),
            ],
            options={
                'verbose_name_plural': 'Paragraphs',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Moderation'), (1, 'Published'), (2, 'Archived')], default=0)),
                ('text', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='articles.article')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcomments', to='articles.comment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IPAddress', models.GenericIPAddressField(default='45.243.82.169')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Normal'), (4, 'Good'), (5, 'Excellent')], default=(1, 'Very bad'), null=True)),
                ('IPAddress', models.GenericIPAddressField(default='45.243.82.169')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_rating', to='articles.article')),
            ],
        ),
    ]