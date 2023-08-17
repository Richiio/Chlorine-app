# Create your views here.
from django.http import HttpResponse
from .sensor import write_data


def write_success(requests):
    # write data
    write_data()
    return HttpResponse('<h1>Writing data to InfluxDB was successful.</h1>')