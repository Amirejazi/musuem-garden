from django.http import Http404
from django.views.generic import ListView, DetailView
from .models import WorkShop
from django.conf import settings
import os

class ShowWorkshopList(ListView):
    model = WorkShop
    template_name = 'workshop_app/show_workshops.html'
    context_object_name = 'workshops'
    queryset = WorkShop.objects.order_by('-is_active')
    paginate_by = 2

class ShowWorkshopDetails(DetailView):
    model = WorkShop
    template_name = 'workshop_app/show_workshopDetail.html'
    context_object_name = 'workshop'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        try:
            workshop = WorkShop.objects.get(id=pk)
            workshop.viewNumber += 1
            workshop.save()
            path = settings.MEDIA_ROOT + '/images/workshops/report/' + str(workshop.id)
            if os.path.isdir(path) :
                image_list = os.listdir(path)
                context['image_list'] = image_list
            return context

        except WorkShop.DoesNotExist:
            raise Http404('Workshop not found')

    
