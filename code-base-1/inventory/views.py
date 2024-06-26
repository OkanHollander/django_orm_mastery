from django.db.utils import IntegrityError
from django.http import HttpResponse

from .models import Brand


def new(request):
    try:
        Brand.objects.create(brand_id=100, name="nike100")
    except IntegrityError:
        return HttpResponse("Error")
    return HttpResponse("Hello World!")
