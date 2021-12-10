from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from register.models import UserProfile
from .models import Group
from django.contrib import messages
from proposalpanelists.models import AdviserAndPanelist


#
# @login_required
# def StudentGroupview(response):
#     name1 = response.user
#     groups = Group.objects.filter(user=name1)
#     if response.method == "POST":
#         user = response.user
#         mem1_fn = response.POST.get('m1_fn')
#         mem1_ln = response.POST.get('m1_ln')
#         groupname = str(mem1_fn) + " " + str(mem1_ln)+ "'s Group"
#         mem1_email = response.POST.get('m1_email')
#         mem2_fn = response.POST.get('m2_fn')
#         mem2_ln = response.POST.get('m2_ln')
#         mem2_email = response.POST.get('m2_email')
#         mem3_fn = response.POST.get('m3_fn')
#         mem3_ln = response.POST.get('m3_ln')
#         mem3_email = response.POST.get('m3_email')
#         mem4_fn = response.POST.get('m4_fn')
#         mem4_ln = response.POST.get('m4_ln')
#         mem4_email = response.POST.get('m4_email')
#
#         select = Group(user=user,
#                        mem1_fn=mem1_fn, mem1_ln=mem1_ln, mem1_email=mem1_email,
#                        mem2_fn=mem2_fn, mem2_ln=mem2_ln, mem2_email=mem2_email,
#                        mem3_fn=mem3_fn, mem3_ln=mem3_ln, mem3_email=mem3_email,
#                        mem4_fn=mem4_fn, mem4_ln=mem4_ln, mem4_email=mem4_email,
#                        groupname=groupname)
#         select.save()
#
#         groupprofile = UserProfile.objects.get(user=response.user)
#         groupprofile.group_name = groupname
#         groupprofile.mem1_fn = mem1_fn
#         groupprofile.mem1_ln = mem1_ln
#         groupprofile.mem1_email = mem1_email
#         groupprofile.mem2_fn = mem2_fn
#         groupprofile.mem2_ln = mem2_ln
#         groupprofile.mem2_email = mem2_email
#         groupprofile.mem3_fn = mem3_fn
#         groupprofile.mem3_ln = mem3_ln
#         groupprofile.mem3_email = mem3_email
#         groupprofile.mem4_fn = mem4_fn
#         groupprofile.mem4_ln = mem4_ln
#         groupprofile.mem4_email = mem4_email
#         group_id = Group.objects.get(user=response.user)
#         groupprofile.group_id=group_id.id
#
#
#         groupprofile.save()
#
#
#
#         messages.success(response, 'Group successfully created')
#         return HttpResponseRedirect(response.path)
#
#     userrole = response.user.userprofile.role
#     name = response.user.get_full_name
#
#     # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
#     resuser = response.user
#     unseen = 0
#
#
#
#     return render(response, 'proposalgroup/student/group.html', {
#         'name1':name1,
#         'name': name,
#         'groups': groups,
#         "userrole": userrole,
#         "unseen": unseen,
#         "resuser": resuser,
#     })


@login_required
def StudentGroupview(response):
    if response.user.userprofile.role == "4":    
        # GET THE NAMES OF STUDENTS EXCEPT THE CURRENT USER AND ORDER IT BY LAST NAME
        names = UserProfile.objects.filter(role='4').filter(~Q(user=response.user)).order_by('user__last_name')
        curr_user = response.user

        # GET GROUPS
        groups = Group.objects.filter(user=response.user)



        # POST
        if response.method == "POST":
            # GET INPUTTED INFO
            mem1 = response.user
            mem2 = response.POST.get('groupmem2')
            mem3 = response.POST.get('groupmem3')
            mem4 = response.POST.get('groupmem4')
            groupname = str(curr_user.first_name) +" " + str(curr_user.last_name) + '\'s Group'


            # NO REDUNDANT STUDENT
            if str(mem2) == str(mem3) or str(mem2) == str(mem4) or str(mem3) == str(mem4):
                messages.error(response, "Error: Must not input the same user as group member")
                return HttpResponseRedirect(response.path)

            # GET OBJECT USING ID
            mem2_id = User.objects.get(id=mem2)
            mem3_id = User.objects.get(id=mem3)
            mem4_id = User.objects.get(id=mem4)

            try:
                # SAVE GROUP IN .DB
                group = Group(user=mem1, mem1=mem1, mem2=mem2_id, mem3=mem3_id, mem4=mem4_id, groupname=groupname)
                group.save()
                print("here")
                # SAVE GROUP IN USERPROFILE

                # UPDATE CURRENT USER USERPROFILE
                UPmem1 = UserProfile.objects.get(user=response.user)
                UPmem1.mem1 = curr_user
                UPmem1.mem2 = mem2_id
                UPmem1.mem3 = mem3_id
                UPmem1.mem4 = mem4_id
                UPmem1.group_name = groupname
                UPmem1.save()


                # UPDATE MEM2 USER PROFILE
                UPmem2 = UserProfile.objects.get(user=mem2_id)
                UPmem2.mem1 = curr_user
                UPmem2.mem2 = mem2_id
                UPmem2.mem3 = mem3_id
                UPmem2.mem4 = mem4_id
                UPmem2.group_name = groupname
                Umem2 = User.objects.get(id=mem2_id.id)
                Umem2.is_active = False
                Umem2.save()
                UPmem2.save()


                # UPDATE MEM3 USER PROFILE
                UPmem3 = UserProfile.objects.get(user=mem3_id)
                UPmem3.mem1 = curr_user
                UPmem3.mem2 = mem2_id
                UPmem3.mem3 = mem3_id
                UPmem3.mem4 = mem4_id
                UPmem3.group_name = groupname
                Umem3 = User.objects.get(id=mem3_id.id)
                Umem3.is_active = False
                Umem3.save()
                UPmem3.save()


                # UPDATE MEM4 USER PROFILE
                UPmem4 = UserProfile.objects.get(user=mem4_id)
                UPmem4.mem1 = curr_user
                UPmem4.mem2 = mem2_id
                UPmem4.mem3 = mem3_id
                UPmem4.mem4 = mem4_id
                UPmem4.group_name = groupname
                Umem4 = User.objects.get(id=mem4_id.id)
                Umem4.is_active = False
                Umem4.save()
                UPmem4.save()



                messages.success(response, "Success: Group members added")
            except :
                messages.error(response, "Error: Can't add new members")
            return HttpResponseRedirect(response.path)


        # FOR SIDEBAR
        userrole = response.user.userprofile.role
        name = response.user.get_full_name

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0

        return render(response, 'proposalgroup/student/group.html', {
            'name': name,
            "names": names,
            "userrole": userrole,
            "unseen": unseen,
            "resuser": resuser,
            "groups":groups,
        })
    else:
        return redirect("page404")




@login_required
def Edit_group(response, id):
    if response.user.userprofile.role == "4":
        group = Group.objects.filter(id=id).first()

        # GET THE NAMES OF STUDENTS EXCEPT THE CURRENT USER AND ORDER IT BY LAST NAME
        names = UserProfile.objects.filter(role='4').filter(~Q(user=response.user)).order_by('user__last_name')
        curr_user = response.user

        if id:
            groups = get_object_or_404(Group, id=id)

            # UPDATE CURRENT USER USERPROFILE
            UPmem1 = UserProfile.objects.get(user=groups.mem1)
            UPmem1.mem1 = None
            UPmem1.mem2 = None
            UPmem1.mem3 = None
            UPmem1.mem4 = None
            UPmem1.group_name = None
            UPmem1.save()

            # UPDATE MEM2 USER PROFILE
            UPmem2 = UserProfile.objects.get(user=groups.mem2)
            UPmem2.mem1 = None
            UPmem2.mem2 = None
            UPmem2.mem3 = None
            UPmem2.mem4 = None
            UPmem2.group_name = None
            Umem2 = User.objects.get(id=groups.mem2.id)
            Umem2.is_active = True
            Umem2.save()
            UPmem2.save()

            # UPDATE MEM3 USER PROFILE
            UPmem3 = UserProfile.objects.get(user=groups.mem3)
            UPmem3.mem1 = None
            UPmem3.mem2 = None
            UPmem3.mem3 = None
            UPmem3.mem4 = None
            UPmem3.group_name = None
            Umem3 = User.objects.get(id=groups.mem3.id)
            Umem3.is_active = True
            Umem3.save()
            UPmem3.save()

            # UPDATE MEM4 USER PROFILE
            UPmem4 = UserProfile.objects.get(user=groups.mem4)
            UPmem4.mem1 = None
            UPmem4.mem2 = None
            UPmem4.mem3 = None
            UPmem4.mem4 = None
            UPmem4.group_name = None
            Umem4 = User.objects.get(id=groups.mem4.id)
            Umem4.is_active = True
            Umem4.save()
            UPmem4.save()

        if response.method == "POST":

            # GET INPUTTED INFO
            groups.mem1 = response.user
            
            m2_id = response.POST.get('groupmem2')
            groups.mem2 = User.objects.get(id=m2_id) 

            m3_id = response.POST.get('groupmem3')
            groups.mem3 = User.objects.get(id=m3_id)

            m4_id = response.POST.get('groupmem4')
            groups.mem4 = User.objects.get(id=m4_id)

            groups.groupname = str(curr_user.first_name) + " " + \
                str(curr_user.last_name) + '\'s Group'
            

            # NO REDUNDANT STUDENT
            if str(groups.mem2) == str(groups.mem3) or str(groups.mem2) == str(groups.mem4) or str(groups.mem3) == str(groups.mem4):
                messages.error(
                    response, "Error: Must not input the same user as group member")
                return redirect("Group")
            else:
                groups.save()

            # GET OBJECT USING ID
            mem2_id = User.objects.get(id=m2_id)
            mem3_id = User.objects.get(id=m3_id)
            mem4_id = User.objects.get(id=m4_id)

            try:
                #DELETE ALL MEMBERS EACH USERPROFILE

                # SAVE GROUP IN USERPROFILE

                # UPDATE CURRENT USER USERPROFILE
                UPmem1 = UserProfile.objects.get(user=response.user)
                UPmem1.mem1 = curr_user
                UPmem1.mem2 = mem2_id
                UPmem1.mem3 = mem3_id
                UPmem1.mem4 = mem4_id
                UPmem1.group_name = groups.groupname
                UPmem1.save()

                # UPDATE MEM2 USER PROFILE
                UPmem2 = UserProfile.objects.get(user=mem2_id)
                UPmem2.mem1 = curr_user
                UPmem2.mem2 = mem2_id
                UPmem2.mem3 = mem3_id
                UPmem2.mem4 = mem4_id
                UPmem2.group_name = groups.groupname
                Umem2 = User.objects.get(id=mem2_id.id)
                Umem2.is_active = False
                Umem2.save()
                UPmem2.save()

                # UPDATE MEM3 USER PROFILE
                UPmem3 = UserProfile.objects.get(user=mem3_id)
                UPmem3.mem1 = curr_user
                UPmem3.mem2 = mem2_id
                UPmem3.mem3 = mem3_id
                UPmem3.mem4 = mem4_id
                UPmem3.group_name = groups.groupname
                Umem3 = User.objects.get(id=mem3_id.id)
                Umem3.is_active = False
                Umem3.save()
                UPmem3.save()

                # UPDATE MEM4 USER PROFILE
                UPmem4 = UserProfile.objects.get(user=mem4_id)
                UPmem4.mem1 = curr_user
                UPmem4.mem2 = mem2_id
                UPmem4.mem3 = mem3_id
                UPmem4.mem4 = mem4_id
                UPmem4.group_name = groups.groupname
                Umem4 = User.objects.get(id=mem4_id.id)
                Umem4.is_active = False
                Umem4.save()
                UPmem4.save()

                messages.success(response, "Success: Group members Edited")
            except:
                messages.error(response, "Error: Can't add new members")
            return redirect("Group")

        # FOR SIDEBAR
        userrole = response.user.userprofile.role
        name = response.user.get_full_name

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0

        return render(response, 'proposalgroup/student/edit_group.html', {
            'group': group,
            'userrole': userrole,
            "unseen": unseen,
            "resuser": resuser,
            'curr_user':curr_user,
            'name':name,
            'names':names,
        })
    else:
        return redirect("page404")


@login_required
def FacultyGroupView(response):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "1" or response.user.userprofile.role == "2":
        userrole = response.user.userprofile.role
        groups = Group.objects.all()

        name = response.user.get_full_name()
        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

        return render(response, 'proposalgroup/faculty/faculty.html', {
            "userrole": userrole,
            'groups': groups,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
            "adviser":adviser,
        })
    else:
        return redirect("page404")
