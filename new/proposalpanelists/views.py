from django.shortcuts import render
from register.models import  UserProfile
from django.contrib.auth.models import User
from proposaltitle.models import ProposeTitle
from .models import AdviserAndPanelist


def AdviserAndPanelistView(response):
    if response.user.userprofile.role == "4":
        name = response.user
        titles = ProposeTitle.objects.filter(user=name)
        users = UserProfile.objects.filter(role = "2")
        if response.method == "POST":
            user = response.user
            adviser = response.POST.get('adviser')
            adviser_id = UserProfile.objects.get(id=adviser)
            title = response.POST.get('title')
            title_id = ProposeTitle.objects.get(title=title)
            panel1 = response.POST.get('panel1')
            panel1_id = UserProfile.objects.get(id=panel1)
            panel2 = response.POST.get('panel2')
            panel2_id = UserProfile.objects.get(id=panel2)
            panel3 = response.POST.get('panel3')
            panel3_id = UserProfile.objects.get(id=panel3)
            panel4 = response.POST.get('panel4')
            panel4_id = UserProfile.objects.get(id=panel4)

            list = AdviserAndPanelist(user=user, adviser=adviser_id, title=title_id, panel1=panel1_id, panel2=panel2_id, panel3=panel3_id, panel4=panel4_id)
            list.save()

        list = AdviserAndPanelist.objects.filter(user=name)

        return render(response,'main/student/proposals/adviserandpanelist/adpa.html', {'users':users, 'name':name, 'list':list, 'titles':titles})

    elif response.user.userprofile.role == "2" or response.user.userprofile.role == "3":

         list = AdviserAndPanelist.objects.filter(adviser=response.user.id) | AdviserAndPanelist.objects.filter(panel1=response.user.id) | AdviserAndPanelist.objects.filter(panel2=response.user.id) | AdviserAndPanelist.objects.filter(panel3=response.user.id) | AdviserAndPanelist.objects.filter(panel4=response.user.id)


         return render(response,'main/cp/proposals/adviserandpanelist/adpa.html', {'list':list})

def delete_adviserandpanelist(response, myid):

    delete = AdviserAndPanelist.objects.get(id=myid)
    delete.delete()

    return rendirect('AdviserAndPanelist')
