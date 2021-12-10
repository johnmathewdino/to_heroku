import json

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from proposalpanelists.models import AdviserAndPanelist
from register.forms import RegisterForm, UserProfileForm
from register.models import UserProfile
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Announcement, Code, UserBatchUpload
from .forms import AnnouncementForm
from submissions.models import SubmissionTitle, StudentSubmit
from proposalgroup.models import Group
from collections import defaultdict
from django.utils.crypto import get_random_string
from django.utils import timezone
from evaluation.models import Scheduler


@login_required
def home(response):
    if response.user.userprofile.role == "1":
        now = timezone.now()
        upcoming_submission = SubmissionTitle.objects.all().order_by("duedate")
        upcoming_schedule = Scheduler.objects.all().order_by("-date")
        cpnum = UserProfile.objects.filter(
            role="2").count()  # count all students
        facnum = UserProfile.objects.filter(
            role="3").count()  # count all instructor

        studentnum = UserProfile.objects.filter(
            role="4").count()  # count all students
        groupnum = Group.objects.all().count()
        maxgroup = groupnum + 5

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
        userrole = response.user.userprofile.role
        subtitle = SubmissionTitle.objects.all()
        submits = StudentSubmit.objects.all()
        groupnum = Group.objects.all().count()

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
        adviserlists = AdviserAndPanelist.objects.filter(
            adviser=response.user.id)
        panelistlists = AdviserAndPanelist.objects.filter(
            panel1=response.user.id) | AdviserAndPanelist.objects.filter(
            panel2=response.user.id) | AdviserAndPanelist.objects.filter(
            panel3=response.user.id)
        advisercount = adviserlists.count()
        panelistcount = panelistlists.count()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user

        return render(response, 'main/dean/home.html', {
            "name": name,
            "resuser": resuser,
            "cpnum": cpnum,
            "facnum": facnum,
            "studentnum": studentnum,
            "groupnum": groupnum,
            "announcements": announcements,
            "form": form,
            "userrole": userrole,
            "subtitle": subtitle,
            "maxgroup": maxgroup,
            "labels": labels,
            "data": data,
            "advisercount": advisercount,
            "panelistcount": panelistcount,
            'now': now,
            'upcoming_submission': upcoming_submission,
            'upcoming_schedule': upcoming_schedule,


        })

    else:
        return redirect("page404")


@login_required
def monitoring(response):
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2" :

        studentsubmit = StudentSubmit.objects.all()
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
            var = StudentSubmit.objects.filter(submission_title=label).count()
            data.append(var)

        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user

        return render(response, 'main/dean/monitoring.html', {
            "userrole": userrole,
            "groups": groups,
            "titles": titles,
            "studentsubmit": studentsubmit,
            "labels": labels,
            "data": data,
            "groupnum": groupnum,
            "name": name,
        })
    else:
        return redirect("page404")


@login_required
def edit_announcement(response, id):
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2":

        update = response.POST.get("update")
        delete = response.POST.get("delete")
        back = response.POST.get("back")

        print("update" + str(update))
        print("delete" + str(delete))

        obj = get_object_or_404(Announcement, id=id)
        form = AnnouncementForm(response.POST or None, instance=obj)
        if str(update) == "1":
            if form.is_valid():
                form.save()
                # return redirect("home")
                # return HttpResponseRedirect('/')
                return HttpResponseRedirect(reverse("home"))

        elif str(delete) == "1":
            obj.delete()
            return HttpResponseRedirect(reverse("home"))
        elif str(back) == "1":
            return HttpResponseRedirect(reverse("home"))
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user

        return render(response, 'main/dean/announcement/edit_announcement.html', {
            "form": form,
            "userrole": userrole,
            "name": name,
            "resuser": resuser,

        })
    else:
        return redirect("page404")


@login_required
def add_cp(response):
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2":

        cp = User.objects.filter(Q(userprofile__role="2")).order_by('date_joined')
        faculty = User.objects.filter(Q(userprofile__role="3"))

        facultylist = []
        for names in faculty:
            facultylist.append(names.get_full_name())
        print(facultylist)

        if response.method == "POST":
            if response.POST.get('remove') != None:
                userid = response.POST.get('remove')
                # print(userid)
                facuser = UserProfile.objects.get(user=userid)
                facuser.role = "3"
                facuser.save()
                messages.error(response, "Removed as Capstone Professor!")
            else:
                facid = response.POST.get("name")
                facuser = UserProfile.objects.get(user=facid)
                facuser.role = "2"
                facuser.save()
                messages.success(response, "Added as Capstone Professor!")


        # user = User.objects.get(user)

        # first_name = response.POST.get("first_name")
        # last_name = response.POST.get("last_name")
        # username = response.POST.get("username")
        # email = response.POST.get("email")
        # password = "!@#Default"
        # role = "2"
        #
        # try:
        #     user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username,
        #                                     password=password)
        #     profile = UserProfile.objects.create(user=user, role=role)
        #     user.save()
        #     profile.save()
        #     return HttpResponseRedirect(reverse("add_cp"))
        #
        #     # return redirect('add_cp')
        # except:
        #     messages.error(response, "Failed to ADD Staff!")
        #     return HttpResponseRedirect(reverse("add_cp"))
        #
        #     # return redirect('add_cp')

        userrole = response.user.userprofile.role
        name = response.user.get_full_name()
        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0

        return render(response, 'main/dean/add/add_cp.html', {
            "cp": cp,
            "faculty": faculty,
            "userrole": userrole,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
       })
    
    else:
        return redirect("page404")

def process_csv(response, filename):
    # INPUT - Filaname
    # OUTPUT - Rows of the csv (except header)

    with open(filename, 'r') as file:

        header = next(file)

        # print(header.lower().replace(" ", "").strip())

        if header.lower().replace(" ", "").strip() == "firstname,lastname,username,emailaddress":
            rows = []

            for row in file:
                rows.append(row)
                # messages.success(response, "Successfully Uploaded!")
            return rows
        else:
            
            return "error"


def process_names(namelist):

    # INPUT = string of unprocessed name ('Jonel,Prado,jprado,jprado@gmail.com\n')
    # OUTPUT = DICT = first name, last name, username, email
    info = namelist.replace("\n", "").split(',')
    # print(info)

    tempdict = {}

    tempdict['firstname'] = info[0]
    tempdict['lastname'] = info[1]
    tempdict['username'] = info[2]
    tempdict['email'] = info[3]

    return tempdict


@login_required
def add_faculty(response):
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2":

        faculty = User.objects.filter(
            Q(userprofile__role="3")).order_by('date_joined')
        if len(Code.objects.filter(role="Faculty")) == 0:
            newcode = Code(role="Faculty", code=get_random_string(6).upper())
            newcode.save()
        code = Code.objects.get(role="Faculty")

        if response.method == "POST":

            if response.POST.get('deactivate') != None:
                userID = response.POST.get('deactivate')
                deactuser = User.objects.get(id=userID)
                print(deactuser.get_full_name())
                deactuser.is_active = False
                deactuser.save()
                messages.success(response, deactuser.get_full_name() +
                                '\'s account successfully deactived!')

            elif response.POST.get('activate') != None:
                userID = response.POST.get('activate')
                activuser = User.objects.get(id=userID)
                activuser.is_active = True
                activuser.save()
                messages.success(response, activuser.get_full_name() +
                                '\'s account successfully activated!')

            elif response.POST.get('delete') != None:
                userID = response.POST.get('delete')
                deluser = User.objects.get(id=userID)
                deluser.delete()
                messages.error(response, deluser.get_full_name() +
                               '\'s account successfully deleted!')

                print(userID)
            elif response.POST.get('generate') != None:
                newcode = get_random_string(6).upper()
                code.code = newcode
                code.save()
                messages.success(response, "Code succesfully generated! ")

            else:
                if response.FILES.get('csvfile') != None:
                    file = response.FILES.get('csvfile')
                    savefile = UserBatchUpload(name=file)
                    savefile.save()
                    messages.success(response, "File successfully uploaded!")
                # file = response.FILES.get('csvfile')
                # print(file.name())

                    processed_csv = process_csv(response, savefile.name.path)
                    if processed_csv != "error":
                        for infos in processed_csv:
                            dictinfo = process_names(infos)
                            password = "!@#Default"
                            role = "3"

                            try:
                                user = User.objects.create_user(first_name=dictinfo['firstname'], last_name=dictinfo['lastname'], email=dictinfo['email'],
                                                                username=dictinfo['username'],
                                                                password=password)
                                profile = UserProfile.objects.create(
                                    user=user, role=role)
                                user.save()
                                profile.save()
                                messages.success(
                                    response, "Faculty Successfully Added!")

                            except:
                                messages.error(response, "Failed to ADD Staff!")
                                return HttpResponseRedirect(response.path_info)
                        messages.success(response, 'Success: New Faculty Added!')
                        return HttpResponseRedirect(response.path_info)

                    else:
                        messages.error(response,
                                    "Failed to Add User/s: Csv File should follow the following headings: First Name, Last Name, Username, Email Address")
                        return HttpResponseRedirect(response.path_info)

                else:
                    first_name = response.POST.get("first_name")
                    last_name = response.POST.get("last_name")
                    username = response.POST.get("username")
                    email = response.POST.get("email")
                    password = "!@#Default"
                    role = "3"

                    try:
                        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username,
                                                    password=password)
                        profile = UserProfile.objects.create(user=user, role=role)
                        user.save()
                        profile.save()
                        # return redirect('add_faculty')
                        messages.success(response, "SUCCESS: New Faculty added")
                        return HttpResponseRedirect(reverse("add_faculty"))

                    except:

                        # return redirect('add_faculty')
                        messages.error(
                            response, "Error: Invalid User! ")
                        return HttpResponseRedirect(reverse("add_faculty"))

        userrole = response.user.userprofile.role
        name = response.user.get_full_name()
        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0

        return render(response, 'main/dean/add/add_faculty.html', {
            "faculty": faculty,
            "userrole": userrole,
            "name": name,
            "code": code,
            "unseen": unseen,
            "resuser": resuser,
        })
    else:
        return redirect('page404')



@login_required
def add_student(response):
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2":

        student = User.objects.filter(
            Q(userprofile__role="4")).order_by('date_joined')
        if len(Code.objects.filter(role="Student")) == 0:
            newcode = Code(role="Student", code=get_random_string(6).upper())
            newcode.save()
        code = Code.objects.get(role="Student")

        if response.method == "POST":
            if response.POST.get('deactivate') != None:
                userID = response.POST.get('deactivate')
                deactuser = User.objects.get(id=userID)
                print(deactuser)
                deactuser.is_active = False
                messages.success(response, 'Success: User is Deactivated!')
                deactuser.save()
            elif response.POST.get('activate') != None:
                userID = response.POST.get('activate')
                activuser = User.objects.get(id=userID)
                activuser.is_active = True
                messages.success(response, 'Success: User is Activated!')
                activuser.save()

            elif response.POST.get('delete') != None:
                userID = response.POST.get('delete')
                deluser = User.objects.get(id=userID)
                messages.error(response, 'Success: User is Deleted!')
                deluser.delete()

                print(userID)
            elif response.POST.get('generate') != None:
                newcode = get_random_string(6).upper()
                code.code = newcode
                messages.success(response, "Code Successfully Generated")
                code.save()

            else:

                if response.FILES.get('csvfile') != None:
                    file = response.FILES.get('csvfile')
                    savefile = UserBatchUpload(name=file)
                    savefile.save()
                    # messages.success(response, "File Successfully Uploaded!")
                    # file = response.FILES.get('csvfile')
                    # print(file.name())

                    processed_csv = process_csv(response, savefile.name.path)
                    if processed_csv != "error":
                        for infos in processed_csv:
                            dictinfo = process_names(infos)
                            password = "!@#Default"
                            role = "4"

                            try:
                                user = User.objects.create_user(first_name=dictinfo['firstname'],
                                                                last_name=dictinfo['lastname'], email=dictinfo['email'],
                                                                username=dictinfo['username'],
                                                                password=password)
                                profile = UserProfile.objects.create(
                                    user=user, role=role)
                                user.save()
                                messages.success(response, "File Successfully Uploaded")
                                profile.save()

                            except:
                                messages.error(response, "Failed to ADD Staff!")
                                return HttpResponseRedirect(response.path_info)
                        messages.success(response, 'Success: New Faculty Added!')
                        return HttpResponseRedirect(response.path_info)

                    else:
                        messages.error(response,
                                    "Failed to Add User/s: Csv File should follow the following headings: First Name, Last Name, Username, Email Address")
                        return HttpResponseRedirect(response.path_info)
                else:
                    first_name = response.POST.get("first_name")
                    last_name = response.POST.get("last_name")
                    username = response.POST.get("username")
                    email = response.POST.get("email")
                    password = "!@#Default"
                    role = "4"
                    try:
                        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username,
                                                        password=password)

                        profile = UserProfile.objects.create(user=user, role=role)
                        user.save()
                        profile.save()
                        # return redirect('add_student')
                        messages.success(response, "SUCCESS! Student Added")
                        return HttpResponseRedirect(reverse("add_student"))

                    except:
                        messages.error(response, "Failed to ADD Student!")
                        # return redirect('add_student')
                        return HttpResponseRedirect(reverse("add_student"))

        userrole = response.user.userprofile.role
        name = response.user.get_full_name()
        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0

        return render(response, 'main/dean/add/add_student.html', {
            "student": student,
            "userrole": userrole,
            "name": name,
            "code": code,
            "unseen": unseen,
            "resuser": resuser,
        })
    else:
        return redirect("page404")




@login_required
def add_group(response):
    # GET GROUPS
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2":

        groups = Group.objects.all()

        # SIDEBAR
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()
        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user

        return render(response, 'main/dean/add/group.html', {
            'groups': groups,
            "userrole": userrole,
            "name": name,
            "resuser": resuser,
        })
    else:
        return redirect("page404")
