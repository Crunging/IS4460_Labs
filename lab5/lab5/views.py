from django.views import View
from django.shortcuts import render, redirect
from .forms import FeedbackForm

class HomePageView(View):

    template_name = 'lab5/index.html'

    def get(self, request):

        form = FeedbackForm()
     
        return render(request, self.template_name,{'form':form})


    def post(self, request):

        form = FeedbackForm(request.POST)

        my_message = ""
        service_selected = False
        
        if form.is_valid():
            my_message = form.cleaned_data['my_message']
            review_area = form.cleaned_data['review_area']
            
            if 'srvc' in review_area:
                service_selected = True
            
            return redirect('thanks/')
        else:          
            return render(request, self.template_name,{
                'form':form,'my_message':my_message,
                'service_selected':service_selected})
        
class ThankYouPageView(View):
    
    template_name = 'lab5/thanks.html'
    
    def get(self, request):
        
        my_name = "Logan Preston"
        
        return render(request, self.template_name,{'my_name':my_name})