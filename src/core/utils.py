import datetime
from autoslug.utils import slugify

from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer


class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, ImageFieldFile):
            return str(o)
        else:
            return super().default(o)


def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def add_images_path(request, model, data):
    try:
        if model.fscity.image:
            data['first_screen'].update({'image': request.build_absolute_uri(model.fscity.image.url)})
        if model.tscity.image:
            data['third_screen'].update({'image': request.build_absolute_uri(model.tscity.image.url)})
    except:
        if model.fsstate.image:
            data['first_screen'].update({'image': request.build_absolute_uri(model.fsstate.image.url)})
        if model.tsstate.image:
            data['third_screen'].update({'image': request.build_absolute_uri(model.tsstate.image.url)})

    return data


<<<<<<< HEAD
def queryset_pagination(request, queryset):

    if not request.POST.get('per_page', False):
        return queryset

    try:
        page = int(request.POST.get('page', 0))
        per_page = int(request.POST.get('per_page', 0))
=======
def get_now() -> datetime.datetime:
    return timezone.now()


def queryset_pagination(request, queryset):

    if not request.GET.get('per_page', False):
        return queryset

    try:
        page = int(request.GET.get('page', 0))
        per_page = int(request.GET.get('per_page', 0))
>>>>>>> 1ed7da5f399e20a2b7473c81dc9d369b2b27de94
    except:
        raise ValueError('Int value expected but str given')

    start = page * per_page
    end = start + per_page

    if start > len(queryset) or end > len(queryset):
        return queryset

    return queryset[start:end]
<<<<<<< HEAD
=======


def get_user_by_jwt(request):
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    print(token)
    data = {'token': token}
    try:
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        user = valid_data['user']
        request.user = user
        return user
    except ValidationError as v:
        print("validation error", v)
        return v.args


def change_slug(models):
    for model in models:
        name = model.name
        model.slug = slugify(name)
        model.save()
>>>>>>> 1ed7da5f399e20a2b7473c81dc9d369b2b27de94
