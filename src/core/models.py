from django.db import models

# Create your models here.


class FirstScreen(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='locations/first_screen/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "First Screen"


class SecondScreen(models.Model):
    main_title = models.CharField(max_length=250)
    main_description = models.TextField()
    sec_title = models.CharField(max_length=250)
    sec_description = models.TextField()

    class Meta:
        verbose_name_plural = "Second Screen"


class ThirdScreen(models.Model):
    main_title = models.CharField(max_length=250)
    main_description = models.TextField()
    sec_title = models.CharField(max_length=250)
    sec_description = models.TextField()
    thrd_title = models.CharField(max_length=250)
    thrd_description = models.TextField()
    image = models.ImageField(upload_to='cities/third_screen/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Third Screen"