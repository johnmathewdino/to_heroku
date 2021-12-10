from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CP_SchedulerViewForm
from .models import Scheduler, SchedulerEvent, SchedulerDate
from register.models import UserProfile
from proposalpanelists.models import AdviserAndPanelist
from proposaltitle.models import ProposeTitle
from django.contrib import messages



def CP_SchedulerView(response):
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2":

        schedule = Scheduler.objects.all().order_by('time')
        events = SchedulerEvent.objects.all()
        dates = SchedulerDate.objects.all()
        if response.method == 'POST':
            form = CP_SchedulerViewForm(response.POST)
            event = response.POST.get('event')
            date = response.POST.get('date')
            if form.is_valid():
                if SchedulerEvent.objects.filter(scheduler_event=event):
                    event = SchedulerEvent.objects.filter(scheduler_event=event).first()
                else:
                    event_save = SchedulerEvent(scheduler_event=event)
                    event_save.save()
                    event = SchedulerEvent.objects.filter(scheduler_event=event).first()

                if SchedulerDate.objects.filter(date_event=date, event_d=event):
                    date = SchedulerDate.objects.filter(date_event=date, event_d=event).first()
                else:
                    date_save = SchedulerDate(date_event=date, event_d=event)
                    date_save.save()
                    date = SchedulerDate.objects.filter(date_event=date, event_d=event).first()

                form = form.save(commit=False)
                form.user = response.user
                form.event = event
                form.date = date
                form.time = response.POST.get("time")
                form.save()
                messages.success(response, 'Schedule Successfully Added! ')
                return redirect("Scheduler")
            else:
                messages.error(response, 'Invalid Input! ')
                return redirect("Scheduler")

        form = CP_SchedulerViewForm()
        userrole = response.user.userprofile.role
        name = response.user.get_full_name

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)


        return render(response, "scheduler/cp/scheduler.html", {
            'form': form,
            'userrole': userrole,
            'schedule': schedule,
            'events': events,
            'dates': dates,
            'name':name,
            "resuser": resuser,
            'adviser':adviser,
        })
    else:
        return redirect("page404")


def Edit_CPScheduler(response, id):
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2":

        schedule = Scheduler.objects.filter(id=id).first()
        if id:
            schedule = get_object_or_404(Scheduler, id=id)
        if response.method == "POST":
            form = CP_SchedulerViewForm(response.POST, instance=schedule)
            if form.is_valid():
                print("here")
                form = form.save(commit=False)
                form.time = response.POST.get("time")
                form.save()
                
                messages.success(response, 'Successfully Edited! ')
                return redirect("Scheduler")
            else:
                messages.error(response, 'Invalid input! ')
                return redirect("Scheduler")
        else:
            form = CP_SchedulerViewForm(instance=schedule)

        userrole = response.user.userprofile.role
        name = response.user.get_full_name

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user

        return render(response, "scheduler/cp/edit_scheduler.html", {
            'form': form,
            'userrole': userrole,
            'schedule':schedule,
            'name':name,
            "resuser": resuser,
        })
    else:
        return redirect("page404")


def Edit_CPdate(response, id):
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2":

        sched_date = SchedulerDate.objects.filter(id=id).first()
        if id:
            sched = get_object_or_404(SchedulerDate, id=id)
        if response.method == 'POST':
            date = response.POST.get('date')
            sched.date_event = date
            sched.save()
            messages.success(response, 'Successfully Edited! ')
            return redirect("Scheduler")

        userrole = response.user.userprofile.role
        name = response.user.get_full_name

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user

        return render(response, 'scheduler/cp/edit_date.html', {
            'sched_date':sched_date,
            'userrole':userrole,
            'name':name,
            'resuser':resuser,
        })

    else:
        return redirect("page404")

def Delete_SchedDate(response, id):
    schedule = SchedulerDate.objects.filter(id=id).first()
    schedule = get_object_or_404(SchedulerDate, id=id)
    schedule.delete()
    messages.error(response, 'Deleted! ')
    return redirect("Scheduler")



    

def Delete_CPScheduler(response, id ):
    schedule = Scheduler.objects.filter(id=id).first()
    schedule = get_object_or_404(Scheduler, id=id)
    schedule.delete()
    messages.error(response, 'Deleted! ')
    return redirect("Scheduler")




def Faculty_SchedulerView(response):
    if response.user.userprofile.role == "3":

        events = SchedulerEvent.objects.all()
        dates = SchedulerDate.objects.all()
        schedule = Scheduler.objects.all().order_by('time')
        users_s = UserProfile.objects.filter(role=4)
        userrole = response.user.userprofile.role
        print(type(User.objects.get(id = response.user.id).get_full_name))
        name = response.user.get_full_name

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)



        return render(response, "scheduler/faculty/scheduler.html", {
            "schedule":schedule,
            "events":events,
            'dates':dates,
            'userrole':userrole,
            'users_s':users_s,
            'name':name,
            "resuser": resuser,
            'adviser':adviser,
        })
    else:
        return redirect("page404")


def Faculty_SchedulerView_Add(response, id):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "1" or response.user.userprofile.role == "2":

        user = response.user
        schedule = Scheduler.objects.filter(id=id).order_by('time')
        users = AdviserAndPanelist.objects.filter(adviser=response.user.id)


        if id:
            sched = get_object_or_404(Scheduler, id=id)
        if response.method == 'POST':
            form = CP_SchedulerViewForm(response.POST, instance=sched)
            if form.is_valid():
                save = form.save(commit=False)
                save.user = user
                save.adv = response.user
                pro = response.POST.get('proponents')
                save.proponents = UserProfile.objects.get(id=pro)
                save.save()
                messages.success(response, 'Successfully Added')
                return redirect('Schedule')
            else:
                messages.error(response, 'Invalid input!')
                return redirect('Schedule')

        form = CP_SchedulerViewForm(instance=sched)
        userrole = response.user.userprofile.role
        name = response.user.get_full_name

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)



        return render(response, "scheduler/faculty/scheduler_add.html", {
            "schedule":schedule,
            "users":users,
            "form":form,
            'userrole':userrole,
            'user':user,
            'name':name,
            "resuser": resuser,
            'adviser':adviser,
        })
    else:
        return redirect("page404")


def Edit_faculty_scheduler(response, id):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "1" or response.user.userprofile.role == "2":

        user = response.user
        schedule = Scheduler.objects.filter(id=id).order_by('-time')
        users = AdviserAndPanelist.objects.filter(adviser=response.user.id)

        if id:
            sched = get_object_or_404(Scheduler, id=id)
        if response.method == 'POST':
            form = CP_SchedulerViewForm(response.POST, instance=sched)
            if form.is_valid():
                save = form.save(commit=False)
                save.user = user
                save.adv = response.user
                pro = response.POST.get('proponents')
                save.proponents = UserProfile.objects.get(id=pro)
                save.save()
                messages.success(response, 'Successfully Edited')
                return redirect('Schedule')
            else:
                messages.error(response, 'Invalid input!')
                return redirect('Schedule')

        form = CP_SchedulerViewForm(instance=sched)
        userrole = response.user.userprofile.role
        name = response.user.get_full_name

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)


        return render(response, "scheduler/faculty/edit_scheduler.html", {
            "schedule":schedule,
            "users":users,
            "form":form,
            'userrole':userrole,
            'user':user,
            'name':name,
            "resuser": resuser,
            'adviser':adviser,
        })
    else:
        return redirect("page404")


def Delete_Faculty_Scheduler(response, id ):
    schedule = Scheduler.objects.filter(id=id).first()
    sched = get_object_or_404(Scheduler, id=id)
    sched.adv = None
    sched.proponents = None
    sched.save()
    messages.error(response, "Deleted!")

    return redirect('Schedule')


def Student_SchedulerView(response):
    if response.user.userprofile.role == "4":

        schedule = Scheduler.objects.all()
        events = SchedulerEvent.objects.all()
        dates = SchedulerDate.objects.all()
        userrole = response.user.userprofile.role
        name = response.user.get_full_name

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user



        return render(response, "scheduler/student/scheduler.html", {
            "schedule":schedule,
            "events":events,
            'dates':dates,
            'userrole':userrole,
            'name':name,
            "resuser": resuser,
        })
    else:
        return redirect("page404")
