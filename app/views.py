from gtts import gTTS
from langdetect import detect_langs

from django.shortcuts import render
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent



def index(request):
    if request.method == 'POST':
        action = request.POST['meaning']
        print(action)
        answer = detect_langs(action)[0].__str__().split(':')[0]
        languages = {'en': 'Англійская', 'de': 'Нямецкая', 'fr': 'Французская',
                'ru': 'Руская', 'uk': 'Украінская', 'pl': 'Польская'
                     }
        detected = languages.get(answer, 'Невядомая мова!')

        tts = gTTS(action, lang=answer)
        tts.save('media/file.wav')

        domain = request.get_host()
        path = ''.join(("http://", domain, str(BASE_DIR), '/media', "/file.wav"))
        print(path, '$$$$$$$$$$$$$$$$$$')

        src = "file:///C:/.../file.wav"





        context = {"answer": detected, "result": action, 'path': path}
        return render(request, 'app/index.html', context=context)
    else:
        context = {"answer": ""}
        return render(request, 'app/index.html', context=context)