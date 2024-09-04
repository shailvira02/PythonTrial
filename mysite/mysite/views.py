# virashai

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse(''' <h1> List of Fav Sites </h1>
    # <a href="https://www.youtube.com/watch?v=YZvRrldjf1Y"> Django tutorial </a>
    # ''')
    params = {"Name":"Shail", "place": "Bharat"}
    return render(request, 'index.html', params)


def analyze(request):

    djtext = request.GET.get('text', 'default')
    removepunc_marker = request.GET.get('removepunc', 'off')
    full_caps_market = request.GET.get('fullcaps', 'off')
    new_line_marker = request.GET.get('newlineremover', 'off')
    space_remover_marker = request.GET.get('spaceremover', 'off')

    if removepunc_marker == "on":
        punctuation_list='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation_list:
                analyzed=analyzed+char
        params = {
            'purpose': 'remove punctuations',
            'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)

    elif full_caps_market == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {
            'purpose': 'Capitalize whole String',
            'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)

    elif new_line_marker == "on":
        analyzed = ""
        for char in djtext:
            if char != "/n":
                analyzed += char
        params = {
            'purpose': 'Removed New lines',
            'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)

    elif space_remover_marker == "on":
        analyzed = ""
        for i, char in enumerate(djtext):
            if djtext[i] == " " and djtext[i+1] == " ":
                pass
            else:
                analyzed += char
        params = {
            'purpose': 'Removed Spaces',
            'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)

    else:
        params = {
            'purpose': 'Have not received any inputs!!!',
            'analyzed_text': djtext
        }
        return render(request, 'analyze.html', params)


    # return render(request, 'analyze.html', params)