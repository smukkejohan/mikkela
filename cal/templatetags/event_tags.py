from django.template import Library, Node
from mikkel.cal.models import Event
     
register = Library()
     
class ComingEventsNode(Node):
    def __init__(self, num):
        self.num = num
    
    def render(self, context):
        context['event_list'] = Event.future.all()[:self.num]
        return ''
    
def get_coming_events(parser, token):
    bits = token.contents.split()
    if len(bits) != 2:
        raise TemplateSyntaxError, "get_coming_events tag takes exactly one argument"
    return ComingEventsNode(bits[1])
get_coming_events = register.tag(get_coming_events)

