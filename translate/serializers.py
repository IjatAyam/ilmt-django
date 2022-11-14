from rest_framework import serializers

from translate.models import Sentence, Translation


class TranslateSerializer(serializers.Serializer):
    original = serializers.CharField()
    translated = serializers.CharField()


class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = '__all__'


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = '__all__'
