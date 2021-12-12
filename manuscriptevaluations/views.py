from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from .models import EvaluationGrade, Evaluations, Evaluator
from register.models import UserProfile
from submissions.models import StudentSubmit
from .forms import EvaluationsForm
from proposalpanelists.models import AdviserAndPanelist
from django.contrib.auth.models import User
from django.contrib import messages 

@login_required
def CPEvaluationView(response):
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2":
        
        users = UserProfile.objects.filter(role="4").exclude(group_adviser=None)
        userrole = response.user.userprofile.role
        name = response.user.get_full_name

        users_for_eval = AdviserAndPanelist.objects.filter(panel1=response.user.id) | AdviserAndPanelist.objects.filter(panel2=response.user.id) | AdviserAndPanelist.objects.filter(panel3=response.user.id) 
        
        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0



        return render(response, 'cp/evaluations.html', {
            'userrole': userrole,
            'users': users,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
            'users_for_eval':users_for_eval,
            
        })
    else:
        return redirect("page404")

@login_required
def CPEvaluateSubmissions(response, id):
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2":
        if AdviserAndPanelist.objects.filter(panel1=response.user.id, user=id) | AdviserAndPanelist.objects.filter(panel2=response.user.id, user=id) | AdviserAndPanelist.objects.filter(panel3=response.user.id, user=id):
            submissions = StudentSubmit.objects.filter(user=id, for_eval_submit="1")

            userrole = response.user.userprofile.role
            name = response.user.get_full_name
            # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
            resuser = response.user
            unseen = 0

            return render(response, 'faculty/evaluatesubmissions.html', {
                'submissions': submissions,
                'userrole': userrole,
                "name": name,
                "unseen": unseen,
                "resuser": resuser,
            })
        else:
          
            submissions = StudentSubmit.objects.filter(user=id, for_eval_submit=1)
            userrole = response.user.userprofile.role
            name = response.user.get_full_name

            # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
            resuser = response.user
            unseen = 0



            return render(response, 'cp/evaluatesubmissions.html', {
                'submissions': submissions,
                'userrole': userrole,
                "name": name,
                "unseen": unseen,
                "resuser": resuser,
            })
            
    else:
        return redirect("page404")

@login_required
def CPEvaluate(response, id):
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2":
        submission = StudentSubmit.objects.filter(id=id).first()
        e_users = Evaluator.objects.filter(submission_user=submission)
        evaluation = Evaluations.objects.filter(submission=submission)
        eval_grade = EvaluationGrade.objects.filter(student_submission=submission)
        userrole = response.user.userprofile.role
        name = response.user.get_full_name

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0


        return render(response, 'cp/evaluate.html', {
            'submission': submission,
            'userrole': userrole,
            'evaluation': evaluation,
            'e_users': e_users,
            'eval_grade': eval_grade,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
        })
    else:
        return redirect("page404")


@login_required
def StudentEvaluationView(response):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "4":
        user = response.user
        submission = StudentSubmit.objects.filter(user=user, for_eval_submit=1)
        evaluation_count = Evaluator.objects.filter(submission_user__user=user).count()
        
        userrole = response.user.userprofile.role
        name = response.user.get_full_name
        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

        return render(response, 'student/evaluations.html', {
            'submission': submission,
            'user': user,
            'userrole': userrole,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
            "adviser":adviser,
            'evaluation_count':evaluation_count,

        })
    else:
        return redirect("page404")


@login_required
def StudentEvaluate(response, id):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "4":
        user = response.user
        submission = StudentSubmit.objects.filter(id=id).first()
        e_users = Evaluator.objects.filter(submission_user=submission)
        evaluation = Evaluations.objects.filter(submission=submission)
        eval_grade = EvaluationGrade.objects.filter(student_submission=submission)
        userrole = response.user.userprofile.role
        name = response.user.get_full_name
        sub = StudentSubmit.objects.get(submission_title=submission.submission_title, user=submission.user)
        sub.if_seen = 0
        sub.save()
        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)



        return render(response, 'student/evaluatedsubmission.html', {
            'submission': submission,
            'user': user,
            'userrole': userrole,
            'evaluation': evaluation,
            'e_users': e_users,
            'eval_grade':eval_grade,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
            "adviser":adviser,
        })
    else:
        return redirect("page404")


@login_required
def FacultyevaluationView(response):
    if response.user.userprofile.role == "3":

        users = AdviserAndPanelist.objects.filter(panel1=response.user.id) | AdviserAndPanelist.objects.filter(
            panel2=response.user.id) | AdviserAndPanelist.objects.filter(panel3=response.user.id)
        print(users)
        user_for_adviser = AdviserAndPanelist.objects.filter(adviser=response.user.id)
        print(user_for_adviser)
        userrole = response.user.userprofile.role
        name = response.user.get_full_name

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)


        return render(response, 'faculty/evaluations.html', {
            'users': users,
            'userrole': userrole,
            "name": name,
            "user_for_adviser": user_for_adviser,
            "unseen": unseen,
            "resuser": resuser,
            "adviser":adviser,
        })
    else:
        return redirect("page404")


@login_required
def FacultyEvaluateSubmissions(response, id):
    if response.user.userprofile.role == "3":

        name = response.user.get_full_name
        if AdviserAndPanelist.objects.filter(adviser=response.user.id, user=id):
            submission = StudentSubmit.objects.filter(user=id, for_eval_submit="1")
            userrole = response.user.userprofile.role

            # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
            resuser = response.user
            unseen = 0
            adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)


            return render(response, 'student/evaluations.html', {
                'submission': submission,
                'userrole': userrole,
                "name": name,
                "unseen": unseen,
                "resuser": resuser,
                "adviser":adviser,
            })
        else:
            submissions = StudentSubmit.objects.filter(user=id, for_eval_submit="1")
            
            
        userrole = response.user.userprofile.role

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)


        return render(response, 'faculty/evaluatesubmissions.html', {
            'submissions': submissions,
            'userrole': userrole,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
            "adviser":adviser,
            

        })
    else:
        return redirect("page404")


@login_required
def FacultyEvaluate(response, id):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "2" or response.user.userprofile.role == "1":
        
        submission = StudentSubmit.objects.filter(id=id).first()
        
        e_users = Evaluator.objects.filter(submission_user=submission)
        evaluation = Evaluations.objects.filter(submission=submission, user=response.user)
        eval_grade = EvaluationGrade.objects.filter(student_submission=submission, evaluator=response.user,)

        form = EvaluationsForm()
        if response.method == 'POST':

            if response.POST.get("evaluatebutton") != "" and response.POST.get("evaluatebutton") != None:

                e_user = response.user
                e_submission = submission
                form = EvaluationsForm(response.POST)
                if form.is_valid():
                    if Evaluator.objects.filter(eval_user=e_user, submission_user=e_submission):
                        e_user = Evaluator.objects.filter(eval_user=e_user, submission_user=e_submission).first()
                        print("me")
                    else:
                        e_user_save = Evaluator(eval_user=e_user, submission_user=e_submission)
                        e_user_save.save()
                        e_user = Evaluator.objects.filter(eval_user=e_user, submission_user=e_submission).first()
                        
                        #add evaluator
                        sub = StudentSubmit.objects.get(submission_title=submission.submission_title, user=submission.user)
                        subs = sub.sub_evaluator + 1
                        s_subs = sub.if_seen + 1
                        sub.sub_evaluator = subs
                        sub.if_seen = s_subs
                        sub.save()

                    save = form.save(commit=False)
                    save.content = response.POST.get("content")
                    save.user = e_user.eval_user
                    save.submission = submission
                    save.save()

                    messages.success(response, "Evaluation Successfully Submitted! ")
                    return HttpResponseRedirect(response.path)
                else:
                    messages.error(response, "Invalid Input! ")
                    return HttpResponseRedirect(response.path)

            elif response.POST.get("gradebutton") != "" and response.POST.get("gradebutton") != None:
                eval_grade.evaluator = response.user
                eval_grade.student_submission = submission

                # IF EVALUATION GRADE TYPE IS PASS/FAIL 
                if submission.eval_grade_submit == "PF":
                    eval_grade.PF = response.POST.get("PF")
                    eval_g = EvaluationGrade(evaluator=eval_grade.evaluator, student_submission=eval_grade.student_submission, PF=eval_grade.PF)
                    eval_g.save()
                    messages.success(response, "Successfully Graded! ")
                    return HttpResponseRedirect(response.path)
                
                # IF EVALUATION GRADE TYPE IS NUMERIC
                elif submission.eval_grade_submit == "N":
                    eval_grade.N = response.POST.get("N")
                    if float(eval_grade.N) > 100 or float(eval_grade.N) < 1:
                        messages.error(response, "Invalid Input: It should be between 0 - 100 only! ")
                        return HttpResponseRedirect(response.path)
                    else:
                        eval_g = EvaluationGrade(evaluator=eval_grade.evaluator, student_submission=eval_grade.student_submission, N=eval_grade.N)
                        eval_g.save()
                        messages.success(response, "Successfully Graded!")
                        return HttpResponseRedirect(response.path)


        userrole = response.user.userprofile.role
        name = response.user.get_full_name
        
        
        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        print(str(eval_grade) +"here")
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)
        


        return render(response, 'faculty/evaluate.html', {
            'submission': submission,
            'userrole': userrole,
            'evaluation': evaluation,
            'form': form,
            'e_users': e_users,
            'name': name,
            "unseen": unseen,
            "resuser": resuser,
            'eval_grade':eval_grade,
            "adviser":adviser,
            
           
        })
    else:
        return redirect("page404")



@login_required
def Edit_FacultyEvaluate(response, id):
    if response.user.userprofile.role == "3":

        evaluation = Evaluations.objects.filter(id=id).first()
        if id:
            evaluation = get_object_or_404(Evaluations, id=id)
        if response.method == "POST":
            form = EvaluationsForm(response.POST, instance=evaluation)
            e_user = response.user
            if form.is_valid():
                if Evaluator.objects.filter(eval_user=e_user):
                    e_user = Evaluator.objects.filter(eval_user=e_user).first()
                else:
                    e_user_save = Evaluator(eval_user=e_user)
                    e_user_save.save()
                    e_user = Evaluator.objects.filter(eval_user=e_user).first()

                save = form.save(commit=False)
                save.content = response.POST.get("content")
                save.user = e_user.eval_user
                save.save()
                messages.success(response, "Evaluation Successfully Edited! ")
                return redirect("Faculty Evaluate", evaluation.submission.id)
            else:
                messages.error(response, "Invalid Input! ")
                return redirect("Faculty Evaluate", evaluation.submission.id)
        else:
            form = EvaluationsForm(instance=evaluation)

        userrole = response.user.userprofile.role
        name = response.user.get_full_name

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)


        return render(response, 'faculty/edit_evaluate.html', {
            'evaluation': evaluation,
            'userrole': userrole,
            'form': form,
            'name': name,
            "unseen": unseen,
            "resuser": resuser,
            "adviser":adviser,

        })
    else:
        return redirect("page404")

@login_required
def Delete_FacultyEvaluate(response, id):
    evaluation = Evaluations.objects.filter(id=id).first()
    evaluation = get_object_or_404(Evaluations, id=id)
    evaluation.delete()
    name = response.user.get_full_name
    messages.error(response, "Deleted!")

    return redirect("Faculty Evaluate", evaluation.submission.id)



@login_required
def Edit_EvaluationGrade(response, id):
    if response.user.userprofile.role == "3":
        eval_grade = EvaluationGrade.objects.filter(id=id).first()
        if id:
            eval_grade = get_object_or_404(EvaluationGrade, id=id)
        if response.method == "POST":

            if eval_grade.student_submission.eval_grade_submit == "PF":
                eval_grade.PF = response.POST.get("PF")
                eval_grade.save()
                messages.success(response, "Successfully Graded! ")
                return redirect("Faculty Evaluate", eval_grade.student_submission.id)

            elif eval_grade.student_submission.eval_grade_submit == "N":
                eval_grade.N = response.POST.get("N")
                if float(eval_grade.N) > 100 or float(eval_grade.N) < 1:
                    messages.error(
                        response, "Invalid Input: It should be between 1 - 100 only! ")
                    return redirect("Faculty Evaluate", eval_grade.student_submission.id)
                else:
                    eval_grade.save()
                    messages.success(response, "Successfully Graded! ")
                    return redirect("Faculty Evaluate", eval_grade.student_submission.id)

        userrole = response.user.userprofile.role
        name = response.user.get_full_name

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

        return render(response, 'faculty/edit_evaluategrade.html', {

            'userrole': userrole,
            'eval_grade': eval_grade,
            'name': name,
            "unseen": unseen,
            "resuser": resuser,
            "adviser":adviser,

        })
    else:
        return redirect("page404")
        

@login_required
def Delete_EvaluationGrade(response, id):
    eval_grade = EvaluationGrade.objects.filter(id=id).first()
    eval_grade = get_object_or_404(EvaluationGrade, id=id)
    eval_grade.delete()
    messages.error(response, "Deleted! ")

    return redirect("Faculty Evaluate", eval_grade.student_submission.id)
