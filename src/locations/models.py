import uuid

from django.db import models

# Create your models here.
from core.models import FirstScreen, SecondScreen, ThirdScreen
from seo.models import SEOBase


class State(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    slug = models.SlugField(
        max_length=150,
        default=uuid.uuid1,
        editable=False,
    )

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(to=State, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=150, null=True)
    description = models.TextField(null=True)
    zip = models.IntegerField(null=True)
    slug = models.SlugField(
        max_length=150,
        default=uuid.uuid1,
        editable=False,
    )

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class FSCity(FirstScreen):
    city = models.OneToOneField(to=City, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "First Screen"


class SSCity(SecondScreen):
    city = models.OneToOneField(to=City, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Second Screen"


class TSCity(ThirdScreen):
    city = models.OneToOneField(to=City, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Third Screen"


class FSState(FirstScreen):
    state = models.OneToOneField(to=State, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "First Screen"


class SSState(SecondScreen):
    state = models.OneToOneField(to=State, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Second Screen"


class TSState(ThirdScreen):
    state = models.OneToOneField(to=State, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = "Third Screen"


class SEOState(SEOBase):
    state = models.OneToOneField(State, on_delete=models.CASCADE, null=True, related_name='seo')

    class Meta:
        verbose_name_plural = "SEO"


class SEOCity(SEOBase):
    state = models.OneToOneField(City, on_delete=models.CASCADE, null=True, related_name='seo')

    class Meta:
        verbose_name_plural = "SEO"
