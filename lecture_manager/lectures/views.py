import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Lecture
from datetime import datetime


def lecture_list(request):
    data = []
    for lecture in Lecture.objects.all():
        data.append({
            "id": lecture.id,
            "name_lecture": lecture.name_lecture,
            "start_time": lecture.start_time.isoformat(),
            "end_time": lecture.end_time.isoformat(),
        })

    return JsonResponse(data, safe=False)

def today_lecture_list(request):

    data = []
    for lecture in Lecture.objects.filter(start_time__date = datetime.now().date()):
        data.append({
            "id": lecture.id,
            "name_lecture": lecture.name_lecture,
            "start_time": lecture.start_time.isoformat(),
            "end_time": lecture.end_time.isoformat(),
        })
    return JsonResponse({"data": data}, safe=False)


def lecture_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        start_time = datetime_converter(data["start_time"])
        end_time = datetime_converter(data["end_time"])

        Lecture.objects.create(
            start_time = start_time,
            end_time = end_time,
            name_lecture = data["name_lecture"]
        )

    return JsonResponse({"success": True})

def lecture_form(request):
    return render(request, "lectures/form.html")

def lecture_main(request):
    return render(request, "lectures/main.html")

def lecture_callendar(request):
    return render(request, "lectures/callendar.html")


def datetime_converter(o):
    if isinstance(o, str):
        return datetime.strptime(o, '%Y-%m-%dT%H:%M')


