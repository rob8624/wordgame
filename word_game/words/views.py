from django.shortcuts import render
from django.http import HttpResponse
from PyDictionary import PyDictionary
import pyperclip


def home_view(request):
    return render(request, 'dictionary.html')

def search_view(request):
    if request.method == 'POST':
        return render(request, 'dictionary.html')
    word = request.GET.get('search')
    dictionary = PyDictionary()
    meanings = dictionary.meaning(word)
    context = {'meanings': meanings, 'word': word}


    # if meanings is not None:
    #     for k, v in meanings.items():
    #
    #        context = {'k': k, 'v': v, 'word': word}

    if meanings != None:
        return render(request, 'test.html', context)
    else:
        return HttpResponse(f"Sorry we have no meaning for the word '{word}' please use a better dictionary :)")


def clipboard_view(request):
    checked_meaning = request.POST.get('meaning')
    pyperclip.copy(checked_meaning)
    print(checked_meaning)

    return HttpResponse(f"copied word meaning to your clipboard")


def about_view(request):

    return render(request, "about.html")


