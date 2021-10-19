from django.contrib import admin

# Register your models here.
from locations.models import City, FSCity, SSCity, TSCity, FSState, SSState, TSState, State, SEOCity


class FirstScreenInlines(admin.TabularInline):
    model = FSCity


class SecondScreenInlines(admin.TabularInline):
    model = SSCity


class ThirdScreenInlines(admin.TabularInline):
    model = TSCity


class SEOCityInlines(admin.StackedInline):
    model = SEOCity


class RegionModelAdmin(admin.ModelAdmin):
    inlines = (FirstScreenInlines, SecondScreenInlines, ThirdScreenInlines, SEOCityInlines)


class FirstScreenStateInlines(admin.TabularInline):
    model = FSState


class SecondScreenStateInlines(admin.TabularInline):
    model = SSState


class ThirdScreenStateInlines(admin.TabularInline):
    model = TSState


class StateModelAdmin(admin.ModelAdmin):
    inlines = (FirstScreenStateInlines, SecondScreenStateInlines, ThirdScreenStateInlines)


admin.site.register(City, RegionModelAdmin)
admin.site.register(State, StateModelAdmin)
