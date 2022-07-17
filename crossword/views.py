import re

from django.shortcuts import render

def index(request):
    pattern = request.POST.get('pattern')
    matches = []
    result = None
    invalid_pattern_msg = ""
    valid_pattern = ""
    if pattern != None:
        pattern = pattern.lower()
        valid_pattern = re.sub("[^A-Za-z\?]", "?", pattern)
        if valid_pattern != pattern:
            invalid_pattern_msg = "Word pattern  must contain only letters or \"?\" -- Instead of " + pattern + ", searching for " + valid_pattern
        regex = re.compile("^" + valid_pattern.replace("?", ".") + "$")
        words = [word.rstrip("\n") for word in open("words_alpha.txt")]
        matches = []
        for word in words:
            match = regex.match(word)
            if match:
                matches.append(word)
        if len(matches) == 0:
            result = ""
        else:
            result = "\n".join(matches)
            print(result)

    submit_button = request.POST.get('submit_button')
    
    context= {
     'pattern': pattern, 
     'valid_pattern': valid_pattern,
     'matches': result,
     'submit_button': submit_button,
     'invalid_pattern_msg': invalid_pattern_msg
    }
        
    return render(request, 'crossword.html', context)
