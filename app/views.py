from langdetect import detect_langs
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        action = request.POST['meaning']
        answer = detect_langs(action)[0].__str__().split(':')[0]
        languages = {'en': 'Англійская', 'de': 'Нямецкая', 'fr': 'Французская',
                'ru': 'Руская', 'uk': 'Украінская', 'pl': 'Польская'
                     }
        detected = languages.get(answer, 'Невядомая мова!')
        context = {"answer": detected}
        return render(request, 'app/index.html', context=context)
    else:
        context = {"answer": ""}
        return render(request, 'app/index.html', context=context)
