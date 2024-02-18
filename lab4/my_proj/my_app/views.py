from django.views import View
from django.shortcuts import render, redirect
from . import my_functions,my_objects

def title_name(the_name: str):
    return the_name.title()

class HomePageView(View):
    def get(self, request):
     
        my_name = "lOgAn"
        
        new_name = title_name(my_name)
        
        the_names = ["PRESTON","CHRIS","MIKE"]
        
        new_names = my_functions.title_names(the_names)
        
        car1 = my_objects.car(color="green",sound="honk honk",)
        
        car2 = my_objects.car(color="blue",sound="beep beep")
        
        #titled_names = title_names(the_names)
        
        the_context = {'hi':'Hello, This is my webpage!',
                       'name':new_name,
                       'names_list':new_names,
                       'car1':car1,
                       'car2':car2}
     
        return render(request, 'my_app/index.html',the_context)