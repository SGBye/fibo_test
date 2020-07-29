from typing import List

from django.conf import settings
from django_redis import get_redis_connection
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from api.rest.serializers import FibonachiQuerySerializer

con = get_redis_connection("default")


@api_view()
def get_fibonachi_slice(request):
    serializer = FibonachiQuerySerializer(data=request.query_params)

    if not serializer.is_valid():
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

    from_ = serializer.validated_data['from_'] - 1  # because people count from 1 :)
    to = serializer.validated_data['to']

    # redis works with inclusive right border so make it the same with python lists
    needed_slice = [int(num) for num in con.lrange(settings.FIBONACHI_CACHE_KEY, from_, to - 1)]

    if not needed_slice:
        full_slice = count_fibonachi_sequence()

        # work with redis structures to avoid serialization-deserialization
        con.rpush(settings.FIBONACHI_CACHE_KEY, *full_slice)

        needed_slice = full_slice[from_:to]

    return Response(needed_slice, HTTP_200_OK)


def count_fibonachi_sequence(last_index: int = settings.MAX_FIBONACHI_INDEX) -> List[int]:
    a, b = 0, 1
    fibo_range = [a, b]

    for i in range(last_index):
        a, b = b, a + b
        fibo_range.append(b)

    return fibo_range
