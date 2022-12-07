from django.shortcuts import render
from django.http import HttpResponse
from PyDictionary import PyDictionary

def home_view(request):

    return render(request, 'dictionary.html')

def search_view(request):
    if request.method == 'POST':
        return render(request, 'dictionary.html')
    word = request.GET.get('search')
    dictionary = PyDictionary()
    meanings = dictionary.meaning(word)
    if meanings != None:
        return HttpResponse(f"{word} means {meanings}")
    else:
        return HttpResponse(f"Sorry we have no meaning for the word '{word}' please use a better dictionary :)")







