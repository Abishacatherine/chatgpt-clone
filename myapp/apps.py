from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import openai

# Set your API key here
openai.api_key = 'your-openai-api-key'

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('text')
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        gpt_response = response['choices'][0]['message']['content']
        return JsonResponse({'response': gpt_response})
    elif request.method == 'GET':
        # This will render the chat.html template when you access the view via GET request
        return render(request, 'myapp/chat.html')
