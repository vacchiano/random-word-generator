from django.shortcuts import render, HttpResponse, redirect
import random

def random_generator():
    charList = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','U','X','Y','Z']
    randWord = ""
    for _ in range (10):
        randNum = random.randint(0, len(charList)-1)
        randWord += str(charList[randNum])
    return randWord

# Create your views here.
def index(request):
    if 'word' not in request.session:
        request.session['word'] = "8DG73F8J3G"
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'index.html')
    
def random_word(request):
    if request.method == "POST":
        request.session['count'] += 1
        randWord = random_generator()
        request.session['word'] = randWord
        return redirect('/')

def reset(request):
    request.session['count'] = 0
    request.session['word'] = "8DG73F8J3G"
    return redirect('/')