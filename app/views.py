from langdetect import detect_langs
from googletrans import Translator
from django.shortcuts import render
from django.core.files.base import ContentFile
from django.http import HttpResponse
from .models import Track
from .utils import record_track


LANGUAGES = {'en': 'English', 'de': 'Deutsch', 'fr': 'Français',
                'ru': 'Русский', 'uk': 'Українська', 'pl': 'Polski',
                     }
TRANSLATE = {'English': 'en', 'Deutsch': 'de', 'Français': 'fr',
                'Русский': 'ru', 'Українська': 'uk', 'Polski': 'pl',

}

def index(request):
    '''main function to define, translate and write text'''
    if request.method == 'POST':
        action = request.POST['meaning']
        try:
            answer = detect_langs(action)[0].__str__().split(':')[0]
        except Exception:
            return HttpResponse('Incorrect or insufficient information!')
        else:
            detected = LANGUAGES.get(answer, 'Unknown language!')
            language = request.POST['languages']
            translate_to = TRANSLATE.get(language, 'en')
            translator = Translator()
            translate = translator.translate(action, src=answer, dest=translate_to)
            translate_text = translate.text

            object = Track.objects.create()
            name = ''.join(('track', '-', str(object.pk)))
            object.title = name

            mp3_file_1 = record_track(text=action, lang=answer)
            object.file_one.save(name=name + '_1',
                             content=ContentFile(mp3_file_1.getvalue()),
                             save=False
                                )
            mp3_file_2 = record_track(text=translate_text, lang=translate_to)
            object.file_two.save(name=name + '_2',
                                 content=ContentFile(mp3_file_2.getvalue()),
                                 save=False
                                 )
            object.save()

            language_output = LANGUAGES.get(translate_to)
            context = {"answer": detected, "result": action,
                       "object": object, "translate_text": translate_text,
                       "language_output": language_output}
            return render(request, "app/index.html", context=context)
    else:
        context = {"answer": ""}
        return render(request, 'app/index.html', context=context)