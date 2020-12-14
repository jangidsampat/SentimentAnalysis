from django.shortcuts import render, redirect
from subprocess import run, PIPE
from sys import executable, argv
from .printResult import ClassificationModel

model = ClassificationModel()

def getResult(text):
    return "Output : " + str(text)

def home(request):
    return render(request, 'sihModel/index.html', {'text': 'None', 'tag': 'None', 'rating': 'None', 'confidence': 'None'})

def printResult(request):
    text = request.POST.get('text')
    modelResults = model.getResult(text)
    print(modelResults)
    return render(request, 'sihModel/index.html', {'text': getResult(text), 'tag': 'Positive', 'rating': '11111', 'confidence': '93.7 %'})