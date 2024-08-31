from django.shortcuts import render

# Create your views here.

# views.py
from django.http import JsonResponse
from .tasks import process_user_request

def user_task_view(request):
    #if request.method == 'POST':
    print("REqust recived")
    # Example: Extract some data from the user's request
    data = ['data']#request.POST.get('data')
    print(process_user_request)
    # Trigger the Celery task
    
    task = process_user_request.delay()
    print("Tasked completed")
    # Return a response to the user while the task runs in the background
    return JsonResponse({"status": "Task initiated", "task_id": task.id})

    return JsonResponse({"status": "Invalid request method"}, status=400)
