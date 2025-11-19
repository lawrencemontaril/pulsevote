from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def andrew(request):
    return render(request, 'pages/home.html', {
        'message': 'andrew was here'
    })