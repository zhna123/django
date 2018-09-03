from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    wordDict = {}
    for word in words:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    sortedDict = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', 
        {'fulltext':fulltext, 'count':len(words), 'wordcountlist':sortedDict})