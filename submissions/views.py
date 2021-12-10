from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from register.models import UserProfile
from .models import SubmissionTitle, StudentSubmit, CommentSubmit
from .forms import SubmissionsForm, SubmitForm, CommentSubmitForm
from django.contrib import messages
from proposalpanelists.models import AdviserAndPanelist




@login_required
def SubmissionTitleViews(response):
    if response.user.userprofile.role == "2" or response.user.userprofile.role == "1" or response.user.userprofile.role == "4" or response.user.userprofile.role == "3":

        form = SubmissionsForm()

        if response.method == 'POST':
            form = SubmissionsForm(response.POST)
            if form.is_valid():
                sform = form.save(commit=False)
                sform.user = response.user
                sform.for_evaluation = response.POST.get('eval')
                sform.type_of_eval_grade = response.POST.get('type')
                sform.save()
                messages.success(response, "Submission Successfully Posted!")
                return HttpResponseRedirect(reverse("submissions"))
            else:
                messages.error(response, "Invalid Input!")
                return HttpResponseRedirect(reverse("submissions"))

        submissiontitle = SubmissionTitle.objects.filter().order_by('timestamp')
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)


        return render (response, 'submissions/submissions.html', {
            'submissions':submissiontitle,
            'form':form,
            "userrole": userrole,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
            "adviser":adviser,
        })
    else:
        return redirect("page404")

@login_required
def Edit_SubmissionTitleViews(response, id):
    if response.user.userprofile.role == "2" or response.user.userprofile.role == "1":

        submissions = SubmissionTitle.objects.filter(id=id)
        stud_sub = StudentSubmit.objects.filter(submission_title=submissions)
        user = response.user
        if id:
            submission = get_object_or_404(SubmissionTitle, id=id)
        if response.method == 'POST':
            form = SubmissionsForm(response.POST, instance=submission)
            submit = response.POST.get('eval')
            print(submit)
            if form.is_valid():
                sform = form.save(commit=False)
                sform.user = user
                print(submit)
                if submit != None:
                    print(submit)
                    sform.for_evaluation = True
                    studentsubmission = StudentSubmit.objects.filter(submission_title=submission)
                    # print(studentsubmission)
                    for subs in studentsubmission:
                        print(subs.user, subs.for_eval_submit)
                        subs.for_eval_submit = True
                        subs.save()
                        messages.success(response, "Submission Successfully Edited!")

                else:
                    sform.for_evaluation = False
                    studentsubmission = StudentSubmit.objects.filter(submission_title=submission)
                    print(studentsubmission)

                    for subs in studentsubmission:
                        print(subs.user, subs.for_eval_submit)
                        subs.for_eval_submit = False
                        subs.save()
                        messages.success(response, "Submission Successfully Edited!")
            else:

                sform.save()
                messages.error(response, "Invalid!")
                return redirect('submissions')

        else:
            form = SubmissionsForm(instance=submission)



        name = response.user.get_full_name()
        userrole = response.user.userprofile.role

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0

        return render (response, 'submissions/edit_submissions/edit_CPsubmission.html', {
            'submissions':submissions,
            'form':form,
            "userrole": userrole,
            "name":name,
            "submission":submission,
            "unseen": unseen,
            "resuser": resuser,
        })
    else:
        return redirect("page404")


@login_required
def Delete_SubmissionTitleViews(response, id):
    submission = SubmissionTitle.objects.filter(id=id)
    submission = get_object_or_404(SubmissionTitle, id=id)
    submission.delete()
    messages.error(response, "Deleted!")
    return redirect('submissions')




@login_required
def StudentSubmitViews(response, id):
    if response.user.userprofile.role == "4":

        postsub = SubmissionTitle.objects.filter(id=id).first()

        if StudentSubmit.objects.filter(submission_title=postsub) & StudentSubmit.objects.filter(user=response.user) :
            submits = StudentSubmit.objects.filter(submission_title=postsub, user=response.user)
        else:
            submits = None

        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0



        return render (response, 'submissions/student-submissions.html', {
            'postsub': postsub,
            'submits':submits,
            "userrole": userrole,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
        })
    else:
        return redirect("page404")




@login_required
def StudentSubmitViewsForm(response, Titleid):
    if response.user.userprofile.role == "4":

        submission_title = SubmissionTitle.objects.filter(id=Titleid).first()
        form = SubmitForm()

        if response.POST.get("sub_content") != '' or response.POST.get("pdf_submit") != "":
            if response.method == 'POST':
                form = SubmitForm(response.POST, response.FILES)
                if form.is_valid():
                    save_form = form.save(commit=False)
                    if response.POST.get("pdf_submit") == None:
                        filename = response.FILES["pdf_submit"].name
                        save_form.filename = filename
                        print(filename)
                    else:
                        print("no file name")

                    save_form.user = response.user
                    save_form.submission_title = submission_title
                    save_form.status = "Submitted"
                    save_form.for_eval_submit = submission_title.for_evaluation
                    save_form.eval_grade_submit = submission_title.type_of_eval_grade
                    save_form.save()
                    messages.success(response, "Successfully Submitted!")
                    return HttpResponseRedirect(reverse("submit", kwargs={'id':Titleid}))
                else:
                    messages.error(response, "Invalid submission! Check Your File Type")
                    return HttpResponseRedirect(reverse("submit", kwargs={'id':Titleid}))
                    
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()
        comments = CommentSubmit.objects.all()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0




        return render (response, 'submissions/submission-form.html', {
            'postsub': submission_title,
            'form':form,
            "userrole": userrole,
            "name": name,
            "comments":comments,
            "unseen": unseen,
            "resuser": resuser,
        })
    else:
        return redirect("page404")


@login_required
def EditStudentSubmitViewsForm(response, id):
    if response.user.userprofile.role == "4":

        obj = get_object_or_404(StudentSubmit,id=id)
        title = SubmissionTitle.objects.filter(title=obj.submission_title).first()
        form = SubmitForm(response.POST or None, instance=obj,)
        delete = response.POST.get("delete")



        if str(delete) == "1":
            obj.delete()
            messages.error(response, "Deleted!")
            return HttpResponseRedirect(reverse("submit", kwargs={'id': title.id}))

        if response.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(response, "Successfully Edited!")
                return HttpResponseRedirect(reverse("submit", kwargs={'id': title.id}))

        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0



        return render(response, 'submissions/edit_submissions/edit_submission.html',{
            "form":form,
            "userrole": userrole,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
        })
    else:
        return redirect("page404")

@login_required
def CPSubmissionsView(response, id):
    if response.user.userprofile.role == "2" or response.user.userprofile.role == "1":

        postsub = SubmissionTitle.objects.filter(id=id).first()
        submits = StudentSubmit.objects.filter(submission_title=id)
        
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0

        return render(response,'submissions/CPsubmissions.html',{
            "name": name,
            "userrole":userrole,
            "postsub":postsub,
            "submits":submits,
            "unseen": unseen,
            "resuser": resuser,
            


        })
    else:
        return redirect("page404")


@login_required
def FacultySubmissionsView(response,id):
    if response.user.userprofile.role == "3":

        user = response.user
        students = UserProfile.objects.filter(group_adviser = user.id)
        postsub = SubmissionTitle.objects.filter(id=id).first()


        submits = []

        for student in students:
            subs = StudentSubmit.objects.filter(user=student.id, submission_title = id)

            for sub in subs:
                print(sub.filename)
                subuser = sub.user.get_full_name()
                sub_title = sub.submission_title
                if  sub.submit_content != "" or  sub.submit_content != None:
                    sub_content = sub.submit_content
                    print(sub_content)
                else:
                    sub_content = ""
                if sub.filename != None:
                    sub_url = sub.pdf_submit.url
                    sub_pdf = sub.pdf_submit
                    sub_filename = sub.filename
                else:
                    sub_url = ""
                    sub_pdf = ""
                    sub_filename = ""
                sub_timestamp = sub.timestamp
                studentsubmissions = [subuser,sub_title,sub_content,sub_url,sub_pdf,sub_filename,sub_timestamp]
                submits.append(studentsubmissions)
                print(studentsubmissions)
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)




        return render(response,'submissions/faculty-view-submissions.html',{
            "userrole":userrole,
            "submits":submits,
            "postsub":postsub,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
            'students':students,
            "adviser":adviser,
        })
    else:
        return redirect("page404")




@login_required
def CPSubmissionComment(response, id):
    if response.user.userprofile.role == "2" or response.user.userprofile.role == "1":
        submissions = StudentSubmit.objects.filter(id=id).first()
        comments = CommentSubmit.objects.filter(submission_content=submissions)
        form = CommentSubmitForm()

        if response.method == 'POST':
            form = CommentSubmitForm(response.POST)
            if form.is_valid():
                save = form.save(commit=False)
                save.user = response.user
                save.submission_content = submissions
                save.save()
                messages.success(response, "Comment submitted!")
            else:
                messages.error(response, "Invalid Comment!")


        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0




        return render(response, "commentsubmit/cp/commentsubmit.html", {
            'submissions':submissions,
            'userrole':userrole,
            'form':form,
            'comments':comments,
            'name':name,
            "unseen": unseen,
            "resuser": resuser,
        })
    else:
        return redirect("page404")


@login_required
def StudentCommentView(response, id):
    if response.user.userprofile.role == "4":

        submit =  StudentSubmit.objects.filter(id=id).first()
        comments = CommentSubmit.objects.filter(submission_content=submit)
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0



        return render(response, 'commentsubmit/student/studentcomment.html', {
            'submit':submit,
            'comments':comments,
            'userrole':userrole,
            'name':name,
            "unseen": unseen,
            "resuser": resuser,
        })
    else:
        return redirect("page404")
