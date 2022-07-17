import re
import sys

from itertools import permutations

from django.shortcuts import render

def index(request):
    letters = request.POST.get('letters')

    if letters is None:
        perms = set()
    else:    
        letters = letters.lower()
        perms = [''.join(p) for p in permutations(letters)]
        perms = set(perms) 

    matches = []
    result = None

    words = [line.rstrip('\n') for line in open('words_alpha.txt')]
    for word in words:
        if word != letters and word in perms:
            matches.append(word)
            
    if len(matches) == 0:
        result = ""
    else:
        result = "\n".join(matches)
        print(result)

    submit_button = request.POST.get('submit_button')
    
    context= {
     'letters': letters, 
     'matches': result,
     'submit_button': submit_button
    }
        
    return render(request, 'anagramfinder.html', context)
