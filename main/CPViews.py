from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from proposalpanelists.models import AdviserAndPanelist
from register.forms import RegisterForm, UserProfileForm
from register.models import UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from proposalgroup.models import Group
from .models import Announcement
from .forms import AnnouncementForm
from submissions.models import SubmissionTitle, StudentSubmit
from proposalgroup.models import Group
from django.utils import timezone
from evaluation.models import Scheduler



@login_required
def home(response):
    if response.user.userprofile.role == '2':

        now = timezone.now()
        cpnum = UserProfile.objects.filter(role="2").count()  # count all students
        facnum = UserProfile.objects.filter(role="3").count()  # count all instructor
        studentnum = UserProfile.objects.filter(role="4").count()  # count all students
        groupnum = Group.objects.all().count()
        maxgroup= groupnum + 5
        userrole = response.user.userprofile.role
        upcoming_submission = SubmissionTitle.objects.all().order_by("duedate")
        upcoming_schedule = Scheduler.objects.all().order_by("-date")
        name = None
        if response.user.is_authenticated:
            name = response.user.get_full_name()

            announcements = Announcement.objects.all().order_by("-timestamp")

            if response.method == "POST":
                form = AnnouncementForm(response.POST)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(response.path)

            form = AnnouncementForm()
            subtitle = SubmissionTitle.objects.all()
            labels = []
            for title in subtitle:
                labels.append(title.title)

            labels_id = []
            for label in subtitle:
                labels_id.append(label.id)

            data = []
            for label in labels_id:
                var = StudentSubmit.objects.filter(submission_title=label).count()
                data.append(var)
            print(labels)
            print(data)
            adviserlists = AdviserAndPanelist.objects.filter(adviser=response.user.id)
            panelistlists = AdviserAndPanelist.objects.filter(
                panel1=response.user.id) | AdviserAndPanelist.objects.filter(
                panel2=response.user.id) | AdviserAndPanelist.objects.filter(
                panel3=response.user.id)
            advisercount = adviserlists.count()
            panelistcount = panelistlists.count()
            # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
            resuser = response.user

        
            return render(response, 'main/cp/home.html',{
                "name":name,
                "cpnum":cpnum,
                "facnum":facnum,
                "studentnum":studentnum,
                "groupnum":groupnum,
                "announcements": announcements,
                "form":form,
                "userrole":userrole,
                "subtitle":subtitle,
                "labels": labels,
                "data": data,
                "maxgroup":maxgroup,
                "advisercount":advisercount,
                "panelistcount":panelistcount,
                "resuser": resuser,
                'upcoming_submission':upcoming_submission,
                'now':now,
                "upcoming_schedule":upcoming_schedule,

            })
    else:
        return redirect("page404")
