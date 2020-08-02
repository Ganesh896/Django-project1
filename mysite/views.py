from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def second(request):
    my_name = (request.POST.get('text', 'default'))
    removepunc = (request.POST.get('removepunc', 'off'))
    capitalize = (request.POST.get('capitalize', 'off'))
    line_remover = (request.POST.get('line_remover', 'off'))
    space_remover = (request.POST.get('space_remover', 'off'))
    char_count = (request.POST.get('char_count', 'off'))
    if removepunc == 'on':
        punctuations = '''!,./'":;'''
        combine = ""
        for char in my_name:
            if char not in punctuations:
                combine += char
        parameters = {'purpose': 'Remove Punctuation', 'analyze_text': combine}
        return render(request, 'analyze.html', parameters)
    elif capitalize == 'on':
        caps = ""
        for char in my_name:
            caps += char.upper()

        parameters = {'purpose': 'Capitalize your Text', 'analyze_text': caps}
        return render(request, 'analyze.html', parameters)
    elif line_remover == 'on':
        caps = ""
        for char in my_name:
            if char != "/n":
                caps += char

        parameters = {'purpose': 'Remove new Lines', 'analyze_text': caps}
        return render(request, 'analyze.html', parameters)
    elif space_remover == 'on':
        caps = ""
        for index, char in enumerate(my_name):
            if not (my_name[index] == " " and my_name[index+1] == " "):
                caps += char

        parameters = {'purpose': 'Remove extra Spaces', 'analyze_text': caps}
        return render(request, 'analyze.html', parameters)
    elif char_count == 'on':
        count = len(my_name)
        print("The total number of character is: ", count)

        parameters = {'purpose': 'Character counter', 'analyze_text': count}
        return render(request, 'analyze.html', parameters)
    else:
        return HttpResponse('Error')
