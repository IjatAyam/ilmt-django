from random import choice

from google_trans_new import google_translator
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from translate.models import Sentence, Translation
from translate.serializers import TranslateSerializer, SentenceSerializer, TranslationSerializer

# translator = Translator()
translator = google_translator()


@api_view(['POST'])
def get_translated(request):
    data = JSONParser().parse(request)
    original = data['text']
    # translate = 'Tested text'
    # translated_sentence = translator.translate(original, src="ms", dest="ar")
    translated = translator.translate(original, lang_src='ms', lang_tgt='ar')

    main_data = {
        'original': original,
        'translated': translated,
    }

    serializer = TranslateSerializer(data=main_data)

    if serializer.is_valid():
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)


class SentenceCreateAPIView(CreateAPIView):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer

    # check if the sentence already exists
    def perform_create(self, serializer):
        sentence = serializer.validated_data['sentence']
        if Sentence.objects.filter(sentence=sentence).exists():
            raise serializers.ValidationError("Sentence already exists")
        else:
            serializer.save()


class SentenceRetrieveAPIView(RetrieveAPIView):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer


class SentenceRetrieveRandomAPIView(RetrieveAPIView):
    serializer_class = SentenceSerializer

    def get_object(self):
        pks = Sentence.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        return Sentence.objects.get(pk=random_pk)


class TranslationCreateAPIView(CreateAPIView):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer

    def perform_create(self, serializer):
        sentence = serializer.validated_data['sentence']
        translated = serializer.validated_data['translated']
        if Translation.objects.filter(sentence=sentence, translated=translated).exists():
            raise serializers.ValidationError("Translation already exists")
        else:
            serializer.save()
