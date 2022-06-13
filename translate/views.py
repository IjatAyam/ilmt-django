from google_trans_new import google_translator
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from translate.serializers import TranslateSerializer

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
