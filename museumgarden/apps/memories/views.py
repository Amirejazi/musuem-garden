from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import View
from .forms import *
from django.forms import modelformset_factory

class ShowMemory(View):
    def get(self, request, *args, **kwargs):
        memories = Memory.objects.filter(is_active=True)
        return render(request, 'memories_app/show_memory.html', {'memories': memories})


@login_required
def add_memory(request):
    imageFormset = modelformset_factory(Memory_Gallery, form=GalleryForm, extra=4 )
    if request.method == 'GET':
        memoryForm = MemoryForm()
        image_formset = imageFormset(queryset=Memory_Gallery.objects.none())
        context ={
            'memoryForm': memoryForm,
            'image_formset': imageFormset
        }
        return render(request, 'memories_app/register_memory.html', context)
    elif request.method == 'POST':
        pass

