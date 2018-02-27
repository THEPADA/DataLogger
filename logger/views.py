from django.shortcuts import render
from .models import WaterLog
import json

def waterLogList(request):
    logs = WaterLog.objects.all()
    return render(request, 'logger/WaterLogList.html', {'waterLog': logs})

def waterLogReciever(request):
    if request.method == 'POST':
      json_data = json.loads(request.body) # request.raw_post_data w/ Django < 1.4
      try:
        waterLog.publish(data['Distance'], data['RTCtemp'], data['Watertemp'], data['Airtemp'])
        data = json_data['data']
      except KeyError:
        HttpResponseServerError("Malformed data!")
      HttpResponse("Got json data")



# Create your views here.
