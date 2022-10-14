from gtts import gTTS
from langdetect import detect_langs
from googletrans import Translator
from io import BytesIO
from django.shortcuts import render
from django.core.files.base import ContentFile
from .models import Track


LANGUAGES = {'en': 'Англійская', 'de': 'Нямецкая', 'fr': 'Французская',
                'ru': 'Руская', 'uk': 'Украінская', 'pl': 'Польская',
                     }
TRANSLATE = {'Англійская': 'en', 'Нямецкая': 'de', 'Французская': 'fr',
                'Руская': 'ru', 'Украінская': 'uk', 'Польская': 'pl',

}

def index(request):
    if request.method == 'POST':
        action = request.POST['meaning']
        answer = detect_langs(action)[0].__str__().split(':')[0]
        detected = LANGUAGES.get(answer, 'Невядомая мова!')
        mp3_fp = BytesIO()
        tts = gTTS(action, lang=answer)
        tts.write_to_fp(mp3_fp)
        object = Track.objects.create(title='name')
        name = ''.join(('track', '-', str(object.pk)))
        object.title = name
        object.file.save(name=name,
                         content=ContentFile(mp3_fp.getvalue()),
                         save=False
                        )
        object.save()
        language = request.POST['languages']
        if language:
            translate_to = TRANSLATE[language]
        else:
            translate_to = 'en'
        translator = Translator()
        translate = translator.translate(action, src=answer, dest=translate_to)
        translate_text = translate.text
        context = {"answer": detected, "result": action,
                   'object': object, "translate_text": translate_text}
        return render(request, 'app/index.html', context=context)
    else:
        context = {"answer": ""}
        return render(request, 'app/index.html', context=context)