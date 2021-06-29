from django.shortcuts import render
from django.utils import timezone

from .models import DownlodedFile
from .sw_api.fetch import fetch_to_file
from .sw_api.table_driver import Table


def index(request):
    # click to fetch
    if(request.GET.get('fetchButton')):
        filename = fetch_to_file()
        timestamp = timezone.now()
        
        # save to database filename, timestamp
        db_data = DownlodedFile(filename = filename, download_time = timestamp)
        db_data.save()

    files_list = DownlodedFile.objects.all()
    context = {
        'files_list': files_list,
    }
    return render(request, 'swapp/index.html', context)

def display(request, counter, filename):
    counter = counter +1
    table = Table(filename)
    data = table.print_table()
    to_show = 10 * counter
    if to_show > len(data):
        to_show = len(data)
    output = data[:to_show]
    context = {
        'data' : output,
        'link' : f'http://localhost:8000/swapp/display/{counter}/{filename}',
    }
    return render(request, 'swapp/display.html', context)

