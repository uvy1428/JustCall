from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from just.models import Details
from .serializers import JustSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


# extra
@csrf_exempt
def get_details(request):
    if request.method == 'GET':
        detail = Details.objects.all()
        detailserializer = JustSerializer(detail, many=True)
        return JsonResponse(detailserializer.data, safe=False)
    elif request.method == 'POST':
        detailserializer_data = JSONParser().parse(request)
        detailserializer = JustSerializer(data=detailserializer)
        if detailserializer.is_valid:
            detailserializer.save()
            return JsonResponse('added sucessfully', safe=False)
        return JsonResponse('failed to add', safe=False)

    elif request.method == 'PUT':
        detailserializer = JSONParser().parse(request)
        detail = Details.objects.all(ToDoId=detailserializer['ToDoId'])
        detailserializer_data = JustSerializer(detail, data=detailserializer)
        if detailserializer_data.is_valid:
            detailserializer.save()
            return JsonResponse('Updated sucessfully', safe=False)
        return JsonResponse('failed to add', safe=False)

    elif request.method == 'DELETE':
        detail = Details.objects.all(ToDoId=id)
        detail.delete()
        return JsonResponse('DElete successfully', safe=False)
