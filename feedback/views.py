from django.shortcuts import render, redirect, get_object_or_404

from .models import StudentFeedback
from .forms import StudentFeebackForm
from django.contrib import messages
from proposalpanelists.models import AdviserAndPanelist


def student_feedback(response):
    if response.user.userprofile.role == "4":

        userrole = response.user.userprofile.role
        print(userrole)
        feedback = StudentFeedback.objects.filter(user=response.user).order_by("-created_at")
        if response.method == 'POST':
            form = StudentFeebackForm(response.POST)
            if form.is_valid():
                save = form.save(commit=False)
                save.user = response.user
                save.role = response.user.userprofile
                save.save()
                messages.success(response, "Feedback Successfully Sent!, Wait for the Admin to Answer your Concern..")
                return redirect('StudentFeedback')
            else:
                messages.error(response, "Invalid Input! ")
                return redirect('StudentFeedback')


        form = StudentFeebackForm()
        print(feedback)
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user



        return render(response, 'student/feedback.html', {
            'feedback':feedback,
            'form':form,
            'userrole':userrole,
            'name':name,
            "resuser": resuser,
        })
    else:
        return redirect("page404")



def faculty_feedback(response):
    if response.user.userprofile.role == "3":

        userrole = response.user.userprofile.role

        feedback = StudentFeedback.objects.filter(user=response.user).order_by("-created_at")
        if response.method == 'POST':
            form = StudentFeebackForm(response.POST)
            if form.is_valid():
                save = form.save(commit=False)
                save.user = response.user
                save.role = response.user.userprofile
                save.save()
                messages.success(response, "Feedback Successfully Sent!, Wait for the Admin to Answer your Concern..")
                return redirect('FacultyFeedback')
            else:
                messages.error(response, "Invalid Input! ")
                return redirect('FacultyFeedback')

        form = StudentFeebackForm()
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)



        return render(response, 'faculty/feedback.html', {
            'feedback':feedback,
            'form':form,
            'userrole':userrole,
            'name':name,
            "resuser": resuser,
            'adviser':adviser,
        })
    else:
        return redirect("page404")


def CP_feedback(response):
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2":

        feedback = StudentFeedback.objects.all().order_by("-created_at")
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user


        return render(response, 'cp/feedback.html', {
            'feedback':feedback,
            'userrole':userrole,
            'name':name,
            "resuser": resuser,
        })
    else:
        return redirect("page404")



def CP_feedback_reply(response, id):
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2":

        feedbacks = StudentFeedback.objects.filter(id=id)
        if id:
            feed = get_object_or_404(StudentFeedback, id=id)
        if response.method == 'POST':
            form = StudentFeebackForm(response.POST, instance=feed)
            if form.is_valid():
                save = form.save(commit=False)
                save.save()
                messages.success(response, "Successfully Sent! ")
                return redirect('CPFeedback')
            else:
                messages.error(response, "Invalid Input! ")
                return redirect('CPFeedback')
            
        else:
            form = StudentFeebackForm(instance=feed)

        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user



        return render(response, 'cp/reply.html', {
            'feedbacks':feedbacks,
            'userrole':userrole,
            'form':form,
            'name':name,
            "resuser": resuser,
        })
    else:
        return redirect("page404")
