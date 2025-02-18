from django.shortcuts import render
from django.http import HttpResponseServerError
import time
import sys

def members(request):
    time.sleep(1)
    sys.exit("Forcibly shutting down Django server!")
    # return HttpResponseServerError("Hello world!")