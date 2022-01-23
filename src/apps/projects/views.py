import json

from django import views
from django.http import HttpResponse

from .models import Project, ProjectTechnology, ProjectInstrument, Technology, Instrument
from ..helpers.serializers import get_serialized_data


class SerializedProjectFiltersView(views.View):
    http_method_names = ['get']

    @staticmethod
    def get(request, *args, **kwargs):  # noqa
        data = {
            'types': {
                'involvement': [pi[0] for pi in Project.Involvement.choices],
                'designation': [pd[0] for pd in Project.Designation.choices]
            },
            'technologies': get_serialized_data(Technology.objects.all()),
            'instruments': get_serialized_data(Instrument.objects.all()),
            'time_period': {
                'from': str(Project.objects.latest('-month_created').month_created),
                'to': str(Project.objects.latest('month_created').month_created)
            }
        }
        return HttpResponse(json.dumps(data), content_type='application/json')


class SerializedProjectsView(views.View):
    http_method_names = ['get']

    @staticmethod
    def get(request, *args, **kwargs):  # noqa
        data = get_serialized_data(Project.objects.all())
        for project in data:
            project['technologies'] = get_serialized_data(
                [pt.technology for pt in ProjectTechnology.objects.filter(project=project['id']).all()]
            )
            project['instruments'] = get_serialized_data(
                [pi.instrument for pi in ProjectInstrument.objects.filter(project=project['id']).all()]
            )
        return HttpResponse(json.dumps(data), content_type='application/json')
