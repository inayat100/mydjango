from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def wabwork(request):
    djtext=request.GET.get('text','no type')
    removeoun=request.GET.get('Removepunc','off')
    upper=request.GET.get('uppercase','off')
    removespace=request.GET.get('removespace','off')
    print(djtext)
    print(removeoun)
    print(upper)
    print(removespace)

    if removeoun == 'on':
        punch = '''{}[]()?/"':;<>,.!@#$%^&\*|='''
        finish = ""
        for char in djtext:
            if char  not in punch:
                finish=finish+char
        dic={'working':'it is working','complted':finish}
        return render(request,'tl.html',dic)
    elif upper =='on':
        finish=""
        for char in djtext:
            finish=finish+char.upper()
        dic = {'working': 'it is working on uppercase', 'complted': finish}
        return render(request, 'tl.html', dic)
    elif removespace == 'on':
        finish=""
        for index ,char in enumerate(djtext):
            if  djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                finish= finish + char
                print(finish)
        dic = {'working': 'it is working on removespace', 'complted': finish}
        return render(request, 'tl.html', dic)


