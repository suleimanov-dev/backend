import json

from django import views
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from .models import Project, ProjectTechnology, ProjectInstrument, Technology, Instrument, ProjectLink, ProjectArticle
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


class SerializedProjectView(views.View):
    http_method_names = ['get']

    @staticmethod
    def get(request, name, *args, **kwargs):  # noqa
        try:
            project_data = get_serialized_data(Project.objects.get(name=name))

            project_links = ProjectLink.objects.filter(project=project_data['id']).select_related('link_type')
            project_data['links'] = []
            for pl in project_links:
                to_append = get_serialized_data(pl)
                to_append['link_type'] = get_serialized_data(pl.link_type)
                project_data['links'].append(to_append)

            project_data['articles'] = get_serialized_data(ProjectArticle.objects.filter(project=project_data['id']))

            project_technologies = ProjectTechnology.objects.filter(
                project=project_data['id']
            ).select_related('technology')
            project_data['technologies'] = []
            for pt in project_technologies:
                to_append = get_serialized_data(pt)
                to_append['technology'] = get_serialized_data(pt.technology)
                project_data['technologies'].append(to_append)

            project_instruments = ProjectInstrument.objects.filter(
                project=project_data['id']
            ).select_related('instrument')
            project_data['instruments'] = []
            for pi in project_instruments:
                to_append = get_serialized_data(pi)
                to_append['instrument'] = get_serialized_data(pi.instrument)
                project_data['instruments'].append(to_append)

            return HttpResponse(json.dumps(project_data), content_type='application/json')

        except ObjectDoesNotExist:
            return HttpResponse('Project with the given name does not exist', status=404)
