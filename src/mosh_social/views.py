from django.http import HttpResponse
from django.utils.translation import gettext as __


def index(request):
    return HttpResponse(__('mosh_social!'))
