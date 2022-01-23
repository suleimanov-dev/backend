import json

from django import views
from django.http import HttpResponse

from .models import MainInfo, ContactLink, TechnologyBlock
from ..helpers.serializers import get_serialized_data


class SerializedMainInfoView(views.View):
    http_method_names = ['get']

    @staticmethod
    def get(request, *args, **kwargs):  # noqa
        data = get_serialized_data(MainInfo.load())
        data['contact_links'] = get_serialized_data(ContactLink.objects.all())
        data['technology_blocks'] = get_serialized_data(TechnologyBlock.objects.all())
        return HttpResponse(json.dumps(data), content_type='application/json')
