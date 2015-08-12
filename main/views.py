from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

# Create your views here.

from main.models import State

def first_view(request):

    states = State.objects.all()

    state_list = ""

    for state in states:
        print state
        print state_list
        for city in state.city_set.filter(name__startswith="A"):
            state_list += "State: %s, City: %s, Zip: %s </br>" % (state.name, city.name, city.zip_code)
            print city
            print state_list


    return HttpResponse(state_list)

def city_search(request, city, state):
    states = State.objects.filter(name__istartswith=state)

    city_string = ""

    for state in states:
        cities = state.city_set.filter(name__istartswith=city)
        for city in cities:
            city_string += "State:%s , City:%s</br>" % (state.name, city.name)

        return HttpResponse(city_string)




def get_view(request):

    get_var1 = request.GET.get ('var1', None)
    get_var2 = request.GET.get ('var2', None)
    get_var3 = request.GET.get ('var3', None)

    get_vars = "%s , %s , %s" % (get_var1, get_vars, get_var3)

    request = "<pre> %s </pre>" % request

    return HttpResponse(get_vars)

def get_city_state(request):

    state = request.GET.get('state', None)
    city = request.GET.get('city', None)

    #city_state = "%s , %s" % (city, state)


@csrf_exempt
def post_city_state(request):

    city_state = """
    <form action='/get_city_state/' method='POST'>

    State:
    </br>
    <input type="text" name ="state" >
    </br>

    City:
    </br>
    <input type="text" name ="city" >

    <input type="submit" value ="Submit Me" >

 


    </form>
    </br>
    </br>


"""

    if request.method == 'GET':

        return HttpResponse(city_state)

    if request.method == 'POST':

        state = request.POST.get('state', None)
        city = request.POST.get('city', None)


        if state != None and city != None:
            states = State.objects.filter(name__istartswith=state)

        for state in states:
            cities = state.city_set.filter(name__istartswith=city)
            for city in cities:
                city_state+="%s , %s </br> - - - - - </br>" % (city.name, state.name)

        return HttpResponse(city_state)

class GetPost(View):
    def get(self, request, *args, **kwargs):
        get_string = "This is a Get String"

        return HttpResponse(get_string)

    def post(self, request, *args, **kwargs):
        post_string = "This is a post String"

        return HttpResponse(post_string)



