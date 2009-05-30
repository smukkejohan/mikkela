from django.shortcuts import render_to_response
from django.template import RequestContext
from mikkel.testimonials.models import Testimonial
#from forms import EventForm

def index(request):
    """
    Testimonials 
    """
    
    return render_to_response('testimonials/index.html', {
        'q_list': Testimonial.objects.all(), 
        #'form': EventForm()
    }, context_instance=RequestContext(request))
