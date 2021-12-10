from datetime import datetime
import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from register.models import UserProfile
from proposalgroup.models import Group
from submissions.models import StudentSubmit, SubmissionTitle
from evaluation.models import Scheduler
from .models import Announcement
from .forms import AnnouncementForm
from django.utils import timezone



@login_required
def home(response):
    if response.user.userprofile.role == "4":

        now = timezone.now()
        date = datetime.now()
        upcoming_submission = SubmissionTitle.objects.all().order_by("duedate")
        upcoming_schedule = Scheduler.objects.all().order_by("-date")
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()
        announcements = Announcement.objects.all().order_by("-timestamp")
        subtitle = SubmissionTitle.objects.all()
        submissions = StudentSubmit.objects.filter(user=response.user)
        subjson = []

        try:
            progress = int((submissions.count() / subtitle.count())*100)
        except:
            progress = 0
        # print(progress)

    # #
        progressjsonlist = []
        for title in subtitle:
            tempdict = {}
            tempdict["title"] = title.title

            for submission in submissions:
                # print("title", title.title, "sub",submission.submission_title)
                if title == submission.submission_title:
                    tempdict["status"] = "submitted"
            progressjsonlist.append(tempdict)


        progressjsondumps = json.dumps(progressjsonlist)
        progressjson = json.loads(progressjsondumps)
        # print(progressjson)

        details = UserProfile.objects.filter(user = response.user)


        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0



        return render(response, 'main/student/home.html',{
            "userrole":userrole,
            "name": name,
            "announcements":announcements,
            "progressjson":progressjson,
            "progress":progress,
            "details":details,
            "unseen": unseen,
            "resuser": resuser,
            'upcoming_submission':upcoming_submission,
            'now':now,
            'upcoming_schedule':upcoming_schedule,
        })
    else:
        return redirect("page404")




