from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from proposalpanelists.models import AdviserAndPanelist

#WILL REDIRECT TO DASHBOARD DEPENDING ON ROLE
@login_required
def directto(response):

    if response.user.userprofile.role == "1":
        return redirect("dean_home")
    elif response.user.userprofile.role == "2":
        return redirect("cp_home")
    elif response.user.userprofile.role == "3":
        
        return redirect("faculty_home")
    elif response.user.userprofile.role == "4":
        return redirect("student_home")

    else:
        return redirect("test")

# TEST ONLY INCASE NO ROLE
def test(response):
    return render(response,'main/test.html')


def page404(response, exception):
    
    return render(response, 'main/page404.html')

    
def page500(response):
    return render(response, 'main/page404.html')

# def for_activities(response):
#     if_adviser = AdviserAndPanelist.objects.filter(adviser=response.user.id).count()
#     print(if_adviser)
#     return render(response, "main/base.html", {
#         'if_adviser':if_adviser,
#     })