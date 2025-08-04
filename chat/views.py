from django.shortcuts import render

def index(request, group_name):
    return render(request, 'chat/index.html', {'group_name': group_name})