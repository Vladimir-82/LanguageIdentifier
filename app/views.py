from gtts import gTTS
from langdetect import detect_langs
import vlc

from io import BytesIO
from django.shortcuts import render
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent



def index(request):
    if request.method == 'POST':
        action = request.POST['meaning']
        answer = detect_langs(action)[0].__str__().split(':')[0]
        languages = {'en': 'Англійская', 'de': 'Нямецкая', 'fr': 'Французская',
                'ru': 'Руская', 'uk': 'Украінская', 'pl': 'Польская'
                     }
        detected = languages.get(answer, 'Невядомая мова!')

        tts = gTTS(action, lang=answer)
        tts.save('media/hello.mp3')

        path = ''.join(("file://", str(BASE_DIR), '/media', "/file.wav"))
        p = vlc.MediaPlayer(path)
        p.play()



        context = {"answer": detected, "result": action}
        return render(request, 'app/index.html', context=context)
    else:
        context = {"answer": ""}
        return render(request, 'app/index.html', context=context)