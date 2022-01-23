import json

from django import views
from django.http import HttpResponse

from .models import MainInfo, ContactLink, TechnologyBlock, TimelineElement, TimelineElementAttachment
from ..helpers.serializers import get_serialized_data


class SerializedMainInfoView(views.View):
    http_method_names = ['get']

    @staticmethod
    def get(request, *args, **kwargs):  # noqa
        main_info_data = get_serialized_data(MainInfo.load())
        main_info_data['contact_links'] = get_serialized_data(ContactLink.objects.all())
        main_info_data['technology_blocks'] = get_serialized_data(TechnologyBlock.objects.all())
        return HttpResponse(json.dumps(main_info_data), content_type='application/json')


class SerializedTimelineView(views.View):
    http_method_names = ['get']

    @staticmethod
    def get(request, *args, **kwargs):  # noqa
        timeline_elements_data = get_serialized_data(TimelineElement.objects.all())
        for timeline_el in timeline_elements_data:
            timeline_el['attachments'] = get_serialized_data(
                TimelineElementAttachment.objects.filter(element=timeline_el['id'])
            )
        return HttpResponse(json.dumps(timeline_elements_data), content_type='application/json')
