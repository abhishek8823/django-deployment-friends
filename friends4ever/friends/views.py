from django.shortcuts import render





def index(request):

    return render(request,'friends/index.html')

def slide(request):
    return render(request,'friends/slide.html')
