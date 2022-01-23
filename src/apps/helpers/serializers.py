import json

from django.core.serializers import serialize
from django.db.models import QuerySet


def get_serialized_data(data):
    is_queryset = isinstance(data, (QuerySet, list, tuple))
    serialized_data = json.loads(serialize('json', data if is_queryset else [data]))
    processed_data = list(map(lambda x: {'id': x['pk'], **x['fields']}, serialized_data))
    return processed_data if is_queryset else processed_data[0]
