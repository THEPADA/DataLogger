from django.shortcuts import render
from .models import WaterLog
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging

logger = logging.getLogger(__name__)

def waterLogList(request):
    logs = WaterLog.objects.all()
    return render(request, 'logger/WaterLogList.html', {'waterLog': logs})


@csrf_exempt
def waterLogReciever(request):
    if request.method == 'POST':
      data = json.loads(request.body) # request.raw_post_data w/ Django < 1.4
      try:
        waterlog = WaterLog()
        waterlog.publish(data["Distance"], data["RTCtemp"], data["Watertemp"], data["Airtemp"])
      except KeyError as e:
          logger.error(str(e))  
          return HttpResponse("Malformed data!")
      return HttpResponse("Got json data")
    else:
        return HttpResponse("Hey man, dont use Get-Request, use POST-Request")



# Create your views here.
