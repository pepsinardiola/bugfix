from django.shortcuts import render, redirect
from agenda.models import List, Task
'''Showing Functions'''


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
'''Functionality Functions'''


def add_list(request):
    myname = request.POST.get('lname')
    mylist = List.objects.create(name=myname)
    mylist.save()
    return redirect("/main/")


def add_task(request, list_name):
    myname = request.POST.get('tname')
    task = Task.objects.create(name=myname, list=List.objects.get(name=list_name))
    task.save()
    return redirect("/main/"+str(list_name))


def remove(request, task_name):
    task = Task.objects.get(name=task_name)
    name1 = task.list.name
    task.delete()
    return redirect("/main/"+str(name1))


def doer(request, list_name):
    mylist = List.objects.get(name=list_name)
    tasks = Task.objects.filter(list=mylist)
    print(request.POST)
    for task in tasks:
        if task.name in request.POST:
            task.isDone=True
            task.save()
    return redirect("/main/"+str(list_name))
