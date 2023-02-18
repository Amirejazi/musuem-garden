from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseNotFound
from .models import *
from django.core.files.storage import FileSystemStorage
from .forms import MessageForm
from django.contrib import messages


def Show_history(request):
    return render(request, 'place_app/_history.html')


def Show_garden_parts(request):
    places = Place.objects.all()
    return render(request, 'place_app/garden_parts.html', {"places": places})


def Show_part_detail(request, id):
    try:
        place = Place.objects.get(id=id)
    except Place.DoesNotExist:
        raise Http404("صفحه مورد نظر یافت نشد")
    return render(request, 'place_app/part_detail.html', {"place": place})


def Download_pathPdf(request):
    fs = FileSystemStorage()
    file_name = 'pdfFiles/path_museumgarden.pdf'
    if fs.exists(file_name):
        with fs.open(file_name) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = "attachment; filename=path_museumgarden.pdf"
            return response
    else:
        return HttpResponseNotFound('فایل مورد نظر یافت نشد')


def time_rules(request):
    places = Place.objects.all()
    ticketPrice = TicketPrice.objects.all()
    context = {
        'places': places,
        'tickets': ticketPrice,
    }
    return render(request, 'place_app/time_rules.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            msg = Message()
            msg.full_name = data['full_name']
            msg.email = data['email']
            msg.subject = data['subject']
            msg.message = data['message']
            msg.save()
            messages.success(request, "پیام شما ارسال شد", "success")
            return redirect('places:contact')
    else:
        form = MessageForm()
    return render(request, 'place_app/contact.html', {"form": form})
