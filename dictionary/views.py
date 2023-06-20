from django.shortcuts import render
from PyDictionary import PyDictionary


# Create your views here.
def index(request):
    return render(request, 'home.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    antonyms = dictionary.antonym(search)  # A word that's opposite
    synonyms = dictionary.synonym(search)  # Similar

    if meaning:
        meanings = {}
        for key, value_list in meaning.items():
            meanings[key] = value_list[0]  # Take the first description for each meaning type

        context = {
            'search': search,
            'meanings': meanings,
            'antonyms': antonyms,
            'synonyms': synonyms
        }
    else:
        context = {
            'search': search,
            'meanings': None,
            'antonyms': antonyms,
            'synonyms': synonyms
        }

    return render(request, 'word.html', context)