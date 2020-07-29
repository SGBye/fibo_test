from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class FibonachiQuerySerializer(serializers.Serializer):
    from_ = serializers.IntegerField(min_value=1, max_value=settings.MAX_FIBONACHI_INDEX)
    to = serializers.IntegerField(min_value=1, max_value=settings.MAX_FIBONACHI_INDEX)

    def validate(self, attrs):
        from_ = attrs['from_']
        to = attrs['to']
        if from_ > to:
            raise ValidationError("from must be smaller or equal than to")
        return attrs
