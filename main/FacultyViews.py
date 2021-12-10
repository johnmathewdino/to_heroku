from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from main.models import Announcement
from proposalgroup.models import Group
from proposalpanelists.models import AdviserAndPanelist
from submissions.models import SubmissionTitle, StudentSubmit
from evaluation.models import Scheduler
from django.utils import timezone


@login_required
def home(response):
    if response.user.userprofile.role == "3":

        name = response.user.get_full_name()
        userrole = response.user.userprofile.role
        now = timezone.now()
        upcoming_submission = SubmissionTitle.objects.all().order_by("duedate")
        upcoming_schedule = Scheduler.objects.all().order_by("-date")
        announcements = Announcement.objects.all().order_by("-timestamp")
        adviserlists = AdviserAndPanelist.objects.filter(adviser=response.user.id)
        panelistlists = AdviserAndPanelist.objects.filter(
            panel1=response.user.id) | AdviserAndPanelist.objects.filter(
            panel2=response.user.id) | AdviserAndPanelist.objects.filter(
            panel3=response.user.id)
        advisercount = adviserlists.count()
        panelistcount = panelistlists.count()

        subtitle = SubmissionTitle.objects.all()

        labels = []
        for title in subtitle:
            labels.append(title.title)
        labels_id = []
        for label in subtitle:
            labels_id.append(label.id)

        data = []
        for label in labels_id:
            var = StudentSubmit.objects.filter(submission_title=label, user__userprofile__group_adviser_id = response.user).count()
            test = StudentSubmit.objects.filter(user__userprofile__group_adviser_id = response.user)
            print(test)
            data.append(var)

        print(labels)
        print(data)

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0

        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)
        



        return render(response, 'main/faculty/home.html',{
            "userrole":userrole,
            "name": name,
            "announcements":announcements,
            "advisercount":advisercount,
            "panelistcount":panelistcount,
            "labels": labels,
            "data": data,
            "groupnum": advisercount,
            "unseen": unseen,
            "resuser": resuser,
            'upcoming_submission':upcoming_submission,
            'now':now,
            'adviser':adviser,
            'upcoming_schedule':upcoming_schedule,

        })
    else:
        return redirect("page404")

@login_required
def facmonitoring(response):
    
    studentsubmit = StudentSubmit.objects.filter(user__userprofile__group_adviser_id = response.user)
    print(studentsubmit)
    groups = []
    for group in studentsubmit:
        if group.user not in groups:
            groups.append(group.user)
    print("groups", groups)

    titles = []
    for title in studentsubmit:
        if title.submission_title not in titles:
            titles.append(title.submission_title)
    print("titles", titles)


    groupnum = Group.objects.all().count()
    subtitle = SubmissionTitle.objects.all()

    labels = []
    for title in subtitle:
        labels.append(title.title)
    labels_id = []
    for label in subtitle:
        labels_id.append(label.id)

    data = []
    for label in labels_id:
        var = StudentSubmit.objects.filter(submission_title=label,user__userprofile__group_adviser_id = response.user).count()
        data.append(var)

    userrole = response.user.userprofile.role
    name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
    resuser = response.user
    unseen = 0
    adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)



    return render(response, 'main/dean/monitoring.html',{
        "userrole": userrole,
        "groups":groups,
        "titles":titles,
        "studentsubmit":studentsubmit,
        "labels": labels,
        "data": data,
        "groupnum": groupnum,
        "name":name,
        "unseen": unseen,
        "resuser": resuser,
        "adviser":adviser,

    })
    



