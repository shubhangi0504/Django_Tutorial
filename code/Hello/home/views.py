from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context={
        'variable':"this is variable to send"
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
