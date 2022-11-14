from django.urls import path

from . import views

app_name = 'translate'

urlpatterns = [
    path('', views.get_translated, name="get-translated"),
    path('sentence/create/', views.SentenceCreateAPIView.as_view(), name="sentence-create"),
    path('sentence/<int:pk>/', views.SentenceRetrieveAPIView.as_view(), name="sentence-retrieve"),
    path('sentence/random/', views.SentenceRetrieveRandomAPIView.as_view(), name="sentence-random"),
    path('translation/create/', views.TranslationCreateAPIView.as_view(), name="translation-create"),
]
