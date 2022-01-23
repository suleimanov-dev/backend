import json

from django import views
from django.http import HttpResponse

from .models import Project, ProjectTechnology, ProjectInstrument
from ..helpers.serializers import get_serialized_data


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
