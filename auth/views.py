from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello Sameer")
