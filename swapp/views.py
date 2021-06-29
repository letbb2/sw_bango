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

def display(request, filename):
    table = Table(filename)
    data = table.print_table()
    context = {
        'data' : data,
    }
    return render(request, 'swapp/display.html', context)

