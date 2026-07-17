from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mainreq(request):
    if request.method == "GET":
        return render(request,"routing/home.html")

def calculate_route(request):
    if request.method == "POST":
        destination = request.POST["destination"]
        source = request.POST["source"]
        context = {
        "destination": destination,
        "source": source
        }
        
        return render(request,"routing/results.html",context) 