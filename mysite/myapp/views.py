from django.shortcuts import render
from myapp.models import car
# Create your views here.
def index(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        new = car (speed = data["field1"],color =data["field2"],costs = data["field3"])
        new.save()
        res = car.objects.all()
    
    return render(request,"testsite.html",{"test":res})




def fullCard(request,myid):
    set = car.objects.filter(id = myid)
    return render(request, 'card.html', {"set":set})
