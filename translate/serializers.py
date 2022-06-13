from rest_framework import serializers


class TranslateSerializer(serializers.Serializer):
    original = serializers.CharField()
    translated = serializers.CharField()
