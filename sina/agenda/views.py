from django.shortcuts import render
from agenda.models import List, Task
# Create your views here.


def main(request):
    lists = List.objects.all()
    return render(request, "main.html", {'lists': lists})


def each(request, list_name):
    mylist = List.objects.get(name=list_name)
    tasks = Task.objects.filter(list=mylist, isDone=False)
    return render(request, "list.html", {'list_name': list_name, 'tasks': tasks})


def done(request):
    mydone = Task.objects.filter(isDone=True)
    return render(request, "done.html", {'mydone': mydone})


def remove(request, task_name):
    task = Task.objects.get(name=task_name)
    task.delete()
    return render(request, "list.html")


def add_task(request, list_name):
    myname = request.POST.get('tname')
    task = Task.objects.create(name=myname, list=List.objects.create(name=list_name))
    task.save()
    return render(request, "list.html")


def add_list(request):
    myname = request.POST.get('lname')
    mylist = List.objects.create(name=myname)
    mylist.save()
    return render(request, "main.html")


def doer(request, list_name):
    mydones = request.POST.getlist('done_state')
    for i in mydones:
        print(i)
        task = Task.objects.get(id=i)
        task.isDone = True
        task.save()
    return render(request, "list.html")
