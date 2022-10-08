from gtts import gTTS
from langdetect import detect_langs
from io import BytesIO
from django.shortcuts import render
from django.core.files.base import ContentFile
from .models import Track





def index(request):
    if request.method == 'POST':
        action = request.POST['meaning']
        answer = detect_langs(action)[0].__str__().split(':')[0]
        languages = {'en': 'Англійская', 'de': 'Нямецкая', 'fr': 'Французская',
                'ru': 'Руская', 'uk': 'Украінская', 'pl': 'Польская'
                     }
        detected = languages.get(answer, 'Невядомая мова!')
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

        context = {"answer": detected, "result": action, 'object': object}
        return render(request, 'app/index.html', context=context)
    else:
        context = {"answer": ""}
        return render(request, 'app/index.html', context=context)