from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from register.models import UserProfile
from django.contrib.auth.models import User
from proposaltitle.models import ProposeTitle
from .models import AdviserAndPanelist, Adviserrequest, Limitation, Panel1request, Panel2request, Panel3request
from django.contrib import messages


#
# @login_required
# def StudentAdviserAndPanelistView(response):
#     name = response.user
#
#     titles = ProposeTitle.objects.filter(user=name, status="Accepted")
#     users = UserProfile.objects.filter(role="3")
#
#     if response.method == "POST":
#         user = response.user
#
#         adviser = response.POST.get('adviser')
#         adviser_id = UserProfile.objects.get(id=adviser)
#
#         title = response.POST.get('title')
#         title_id = ProposeTitle.objects.get(title=title)
#
#         panel1 = response.POST.get('panel1')
#         panel1_id = UserProfile.objects.get(id=panel1)
#
#         panel2 = response.POST.get('panel2')
#         panel2_id = UserProfile.objects.get(id=panel2)
#
#         panel3 = response.POST.get('panel3')
#         panel3_id = UserProfile.objects.get(id=panel3)
#
#         print(response.POST.get('newtitle'))
#
#         if response.POST.get('newtitle') != "":
#             newtitle = response.POST.get("newtitle")
#             list = AdviserAndPanelist(user=user, adviser=adviser_id, final_title=newtitle,
#                                       proposed_title=title_id, panel1=panel1_id, panel2=panel2_id, panel3=panel3_id)
#
#             adviser_limits = AdviserAndPanelist.objects.filter(adviser=adviser_id)
#             count_adviser = adviser_limits.count()
#             print(count_adviser)
#
#             # FILTER ID IN EVERY PANELIST FIELD
#             panel1_limits_1 = AdviserAndPanelist.objects.filter(panel1=panel1_id)
#             panel1_limits_2 = AdviserAndPanelist.objects.filter(panel2=panel1_id)
#             panel1_limits_3 = AdviserAndPanelist.objects.filter(panel3=panel1_id)
#
#             # ADD ALL COLLECTED ID OF PANEL1
#             p1count1 = panel1_limits_1.count()
#             p1count2 = panel1_limits_2.count()
#             p1count3 = panel1_limits_3.count()
#             count_panel1 = p1count1 + p1count2 + p1count3
#             print(count_panel1)
#
#             # FILTER ID IN EVERY PANELIST FIELD
#             panel2_limits_1 = AdviserAndPanelist.objects.filter(panel1=panel2_id)
#             panel2_limits_2 = AdviserAndPanelist.objects.filter(panel2=panel2_id)
#             panel2_limits_3 = AdviserAndPanelist.objects.filter(panel3=panel2_id)
#
#             # ADD ALL COLLECTED ID OF PANEL2
#             p2count1 = panel2_limits_1.count()
#             p2count2 = panel2_limits_2.count()
#             p2count3 = panel2_limits_3.count()
#             count_panel2 = p2count1 + p2count2 + p2count3
#             print(count_panel2)
#
#             # FILTER ID IN EVERY PANELIST FIELD
#             panel3_limits_1 = AdviserAndPanelist.objects.filter(panel1=panel3_id)
#             panel3_limits_2 = AdviserAndPanelist.objects.filter(panel2=panel3_id)
#             panel3_limits_3 = AdviserAndPanelist.objects.filter(panel3=panel3_id)
#
#             # ADD ALL COLLECTED ID OF PANEL3
#             p3count1 = panel3_limits_1.count()
#             p3count2 = panel3_limits_2.count()
#             p3count3 = panel3_limits_3.count()
#             count_panel3 = p3count1 + p3count2 + p3count3
#             print(count_panel3)
#
#             if count_adviser > 10:
#                 messages.error(response, "Invalid Input: " + str(
#                     adviser_id.user.get_full_name()) + " Reach Maximum Capacity as Adviser")
#             elif count_panel1 > 10:
#                 messages.error(response, "Invalid Input: " + str(
#                     panel1_id.user.get_full_name()) + " Reach Maximum Capacity as Panel")
#             elif count_panel2 > 10:
#                 messages.error(response, "Invalid Input: " + str(
#                     panel2_id.user.get_full_name()) + " Reach Maximum Capacity as Panel")
#             elif count_panel3 > 10:
#                 messages.error(response, "Invalid Input: " + str(
#                     panel3_id.user.get_full_name()) + " Reach Maximum Capacity as Panel")
#             else:
#                 list.save()
#
#             profile = UserProfile.objects.get(user=response.user)
#             print("!here")
#
#             profile.group_adviser = User.objects.get(id=adviser)
#             profile.group_title = newtitle
#             profile.group_panel_1 = User.objects.get(id=panel1)
#             profile.group_panel_2 = User.objects.get(id=panel2)
#             profile.group_panel_3 = User.objects.get(id=panel3)
#             profile.save()
#             return HttpResponseRedirect(response.path)
#
#         else:
#             list = AdviserAndPanelist(user=user, adviser=adviser_id, proposed_title=title_id,
#                                       panel1=panel1_id, panel2=panel2_id, panel3=panel3_id)
#
#             adviser_limits = AdviserAndPanelist.objects.filter(adviser=adviser_id)
#             count_adviser = adviser_limits.count()
#             print(count_adviser)
#
#             # FILTER ID IN EVERY PANELIST FIELD
#             panel1_limits_1 = AdviserAndPanelist.objects.filter(panel1=panel1_id)
#             panel1_limits_2 = AdviserAndPanelist.objects.filter(panel2=panel1_id)
#             panel1_limits_3 = AdviserAndPanelist.objects.filter(panel3=panel1_id)
#
#             # ADD ALL COLLECTED ID OF PANEL1
#             p1count1 = panel1_limits_1.count()
#             p1count2 = panel1_limits_2.count()
#             p1count3 = panel1_limits_3.count()
#             count_panel1 = p1count1 + p1count2 + p1count3
#             print(count_panel1)
#
#             # FILTER ID IN EVERY PANELIST FIELD
#             panel2_limits_1 = AdviserAndPanelist.objects.filter(panel1=panel2_id)
#             panel2_limits_2 = AdviserAndPanelist.objects.filter(panel2=panel2_id)
#             panel2_limits_3 = AdviserAndPanelist.objects.filter(panel3=panel2_id)
#
#             # ADD ALL COLLECTED ID OF PANEL2
#             p2count1 = panel2_limits_1.count()
#             p2count2 = panel2_limits_2.count()
#             p2count3 = panel2_limits_3.count()
#             count_panel2 = p2count1 + p2count2 + p2count3
#             print(count_panel2)
#
#             # FILTER ID IN EVERY PANELIST FIELD
#             panel3_limits_1 = AdviserAndPanelist.objects.filter(panel1=panel3_id)
#             panel3_limits_2 = AdviserAndPanelist.objects.filter(panel2=panel3_id)
#             panel3_limits_3 = AdviserAndPanelist.objects.filter(panel3=panel3_id)
#
#             # ADD ALL COLLECTED ID OF PANEL3
#             p3count1 = panel3_limits_1.count()
#             p3count2 = panel3_limits_2.count()
#             p3count3 = panel3_limits_3.count()
#             count_panel3 = p3count1 + p3count2 + p3count3
#             print(count_panel3)
#
#             # LIMIT VALIDATIONS
#             if count_adviser > 10:
#                 messages.error(response, "Invalid Input: " + str(
#                     adviser_id.user.get_full_name()) + " Reach Maximum Capacity as Adviser")
#             elif count_panel1 > 10:
#                 messages.error(response, "Invalid Input: " + str(
#                     panel1_id.user.get_full_name()) + " Reach Maximum Capacity as Panel")
#             elif count_panel2 > 10:
#                 messages.error(response, "Invalid Input: " + str(
#                     panel2_id.user.get_full_name()) + " Reach Maximum Capacity as Panel")
#             elif count_panel3 > 10:
#                 messages.error(response, "Invalid Input: " + str(
#                     panel3_id.user.get_full_name()) + " Reach Maximum Capacity as Panel")
#             else:
#                 list.save()
#
#             profile = UserProfile.objects.get(user=response.user)
#
#             profile.group_adviser = User.objects.get(id=adviser)
#             profile.group_title = title
#             profile.group_panel_1 = User.objects.get(id=panel1)
#             profile.group_panel_2 = User.objects.get(id=panel2)
#             profile.group_panel_3 = User.objects.get(id=panel3)
#             profile.save()
#             return HttpResponseRedirect(response.path)
#
#     list = AdviserAndPanelist.objects.filter(user=name)
#     userrole = response.user.userprofile.role
#     profile = UserProfile.objects.get(user=response.user)
#     name = response.user.get_full_name()
#
#     # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
#     resuser = response.user
#     unseen = 0
#
#
#     return render(response, 'adviserpanelistproposal/student_adpa.html', {
#         'users': users,
#         'name': name,
#         'list': list,
#         'titles': titles,
#         "userrole": userrole,
#         "unseen": unseen,
#         "resuser": resuser,
#     })


@login_required
def StudentAdviserAndPanelistView(response):
    if response.user.userprofile.role == "4":

        # REQUIRED FOR SIDEBAR AND NAVBAR
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()
        resuser = response.user
        limit = Limitation.objects.all()

        for l in limit:
            print(l)

        # GETTING THE FINAL INFO OF STUDENTS IF NOT NONE
        UserInfo = UserProfile.objects.get(user=response.user)

        # GET ACCEPTED TITLES
        titles = ProposeTitle.objects.filter(user=response.user, status="Accepted")

        # GET FACULTY NAMES
        users = UserProfile.objects.filter(role="3") | UserProfile.objects.filter(role="2") | UserProfile.objects.filter(role="1")

        # POST METHOD
        if response.method == "POST":
        
            # REQUEST FOR ADVISER
            if response.POST.get('adviserbutton') != "" and response.POST.get('adviserbutton') != None:

                # GETTING THE INPUT OF STUDENTS
                advisername = response.POST.get('advisername')
                advisername = User.objects.get(id=advisername)

                if Adviserrequest.objects.filter(user=response.user, name=advisername).exclude(status="decline"):
                    messages.error(response, "You already Choose " +
                                   str(advisername.get_full_name()) + " as Adviser")
                    return HttpResponseRedirect(response.path)
                
                #LIMITATION AS ADVISER
                adviser_limits = AdviserAndPanelist.objects.filter(adviser=advisername.userprofile)
                count_adviser = adviser_limits.count()
                print(count_adviser)
                if count_adviser >= l.limit:
                    messages.error(response, "Invalid Input: " + str(
                        advisername.userprofile.user.get_full_name()) + " Reach Maximum Capacity as Adviser")
                    return HttpResponseRedirect(response.path)


                proposedtitle = response.POST.get('title')
                if response.POST.get('edittitle') != None:
                    finaltitle = response.POST.get('newtitle')
                    if finaltitle == "" or finaltitle == None:
                        finaltitle = proposedtitle
                else:
                    finaltitle = proposedtitle
                description = response.POST.get('description')

                # SAVING THE INPUT TO DATABASE
                try:
                    saverequest = Adviserrequest(user=response.user, name=advisername, proposedtitle=proposedtitle,
                                                finaltitle=finaltitle,
                                                titledescription=description)
                    saverequest.save()
                    messages.success(response, 'Success! Request was sent. Await for Acceptance')
                except:
                    messages.error(response, 'Error! Cannot process your request')
                return HttpResponseRedirect(response.path)

            # REQUEST AS PANEL1
            elif response.POST.get('panel1button') != "" and response.POST.get('panel1button') != None:
                print("Panel 1")

                # GETTING THE INPUT OF STUDENTS
                panel1name = response.POST.get('panel1name')
                panel1name = User.objects.get(id=panel1name)

                if Panel2request.objects.filter(user=response.user, name=panel1name).exclude(status="decline"):
                    messages.error(response, "You already Choose " + str(panel1name.get_full_name()) + " as panelist No.2")
                    return HttpResponseRedirect(response.path)
                elif Panel3request.objects.filter(user=response.user, name=panel1name).exclude(status="decline"):
                    messages.error(response, "You already Choose " + str(panel1name.get_full_name()) + " as panelist No.3 ")
                    return HttpResponseRedirect(response.path)
                elif Panel3request.objects.filter(user=response.user, name=panel1name).exclude(status="decline"):
                    messages.error(response, "You already Choose " + str(panel1name.get_full_name()) + " as panelist No.1 ")
                    return HttpResponseRedirect(response.path)
                else:
                    #LIMITATION AS PANELIST 1
                    # FILTER ID IN EVERY PANELIST FIELD
                    panel1_limits_1 = AdviserAndPanelist.objects.filter(panel1=panel1name.userprofile)
                    panel1_limits_2 = AdviserAndPanelist.objects.filter(panel2=panel1name.userprofile)
                    panel1_limits_3 = AdviserAndPanelist.objects.filter(panel3=panel1name.userprofile)

                    # ADD ALL COLLECTED ID OF PANEL1
                    p1count1 = panel1_limits_1.count()
                    p1count2 = panel1_limits_2.count()
                    p1count3 = panel1_limits_3.count()
                    count_panel1 = p1count1 + p1count2 + p1count3
                    print(count_panel1)

                    if count_panel1 >= l.limit:
                        messages.error(response, "Invalid Input: " + str(
                            panel1name.userprofile.user.get_full_name()) + " Reach Maximum Capacity as Panelist")
                        return HttpResponseRedirect(response.path)

                    if UserInfo.group_adviser == "" or UserInfo.group_adviser == None:
                        messages.error(response, "ERROR: You Should request first or accepted by the adviser!")
                        return HttpResponseRedirect(response.path)
                    else: 
                        # SAVING THE INPUT TO DATABASE
                        try:
                            saverequest = Panel1request(user=response.user, name=panel1name)
                            saverequest.save()
                            messages.success(response, 'Success! Request was sent. Await for Acceptance')
                        except:
                            messages.error(response, 'Error! Cannot process your request')
                        return HttpResponseRedirect(response.path)


            # REQUEST AS PANEL2
            elif response.POST.get('panel2button') != "" and response.POST.get('panel2button') != None:

                print("Panel 2")

                # GETTING THE INPUT OF STUDENTS
                panel2name = response.POST.get('panel2name')
                panel2name = User.objects.get(id=panel2name)

                if Panel1request.objects.filter(user=response.user, name=panel2name).exclude(status="decline"):
                    messages.error(response, "You already Choose " +
                                   str(panel2name.get_full_name()) + " as panelist No.1 ")
                    return HttpResponseRedirect(response.path)
                elif Panel2request.objects.filter(user=response.user, name=panel2name).exclude(status="decline"):
                    messages.error(response, "You already Choose " +
                                   str(panel2name.get_full_name()) + " as panelist No.2")
                    return HttpResponseRedirect(response.path)
                elif Panel3request.objects.filter(user=response.user, name=panel2name).exclude(status="decline"):
                    messages.error(response, "You already Choose " +
                                   str(panel2name.get_full_name()) + " as panelist No.3")
                    return HttpResponseRedirect(response.path)
                else:

                    #LIMITATION AS PANELIST 2
                    # FILTER ID IN EVERY PANELIST FIELD
                    panel2_limits_1 = AdviserAndPanelist.objects.filter(panel1=panel2name.userprofile)
                    panel2_limits_2 = AdviserAndPanelist.objects.filter(panel2=panel2name.userprofile)
                    panel2_limits_3 = AdviserAndPanelist.objects.filter(panel3=panel2name.userprofile)

                    # ADD ALL COLLECTED ID OF PANEL1
                    p2count1 = panel2_limits_1.count()
                    p2count2 = panel2_limits_2.count()
                    p2count3 = panel2_limits_3.count()
                    count_panel2 = p2count1 + p2count2 + p2count3
                    print(count_panel2)

                    if count_panel2 >= l.limit:
                        messages.error(response, "Invalid Input: " + str(
                            panel2name.userprofile.user.get_full_name()) + " Reach Maximum Capacity as Panelist")
                        return HttpResponseRedirect(response.path)

                    if UserInfo.group_adviser == "" or UserInfo.group_adviser == None:
                        messages.error(
                            response, "ERROR: You Should request first or accepted by the adviser!")
                        return HttpResponseRedirect(response.path)
                    else:
                    # SAVING THE INPUT TO DATABASE
                        try:
                            saverequest = Panel2request(user=response.user, name=panel2name)
                            saverequest.save()
                            messages.success(response, 'Success! Request was sent. Await for Acceptance')
                        except:
                            messages.error(response, 'Error! Cannot process your request')
                        return HttpResponseRedirect(response.path)

            # REQUEST AS PANEL3
            elif response.POST.get('panel3button') != "" and response.POST.get('panel3button') != None:
                print("Panel 3")

                # GETTING THE INPUT OF STUDENTS
                panel3name = response.POST.get('panel3name')
                panel3name = User.objects.get(id=panel3name)

                if Panel1request.objects.filter(user=response.user, name=panel3name).exclude(status="decline"):
                    messages.error(response, "You already Choose " +
                                   str(panel3name.get_full_name()) + " as panelist No.1 ")
                    return HttpResponseRedirect(response.path)
                elif Panel2request.objects.filter(user=response.user, name=panel3name).exclude(status="decline"):
                    messages.error(response, "You already Choose " +
                                   str(panel3name.get_full_name()) + " as panelist No.2")
                    return HttpResponseRedirect(response.path)
                elif Panel3request.objects.filter(user=response.user, name=panel3name).exclude(status="decline"):
                    messages.error(response, "You already Choose " +
                                   str(panel3name.get_full_name()) + " as panelist No.3")
                    return HttpResponseRedirect(response.path)
                else:

                    #LIMITATION AS PANELIST 3
                    # FILTER ID IN EVERY PANELIST FIELD
                    panel3_limits_1 = AdviserAndPanelist.objects.filter(panel1=panel3name.userprofile)
                    panel3_limits_2 = AdviserAndPanelist.objects.filter(panel2=panel3name.userprofile)
                    panel3_limits_3 = AdviserAndPanelist.objects.filter(
                        panel3=panel3name.userprofile)

                    # ADD ALL COLLECTED ID OF PANEL1
                    p3count1 = panel3_limits_1.count()
                    p3count2 = panel3_limits_2.count()
                    p3count3 = panel3_limits_3.count()
                    count_panel3 = p3count1 + p3count2 + p3count3
                    print(count_panel3)

                    if count_panel3 >= l.limit:
                        messages.error(response, "Invalid Input: " + str(
                            panel3name.userprofile.user.get_full_name()) + " Reach Maximum Capacity as Panelist")
                        return HttpResponseRedirect(response.path)
                    
                    if UserInfo.group_adviser == "" or UserInfo.group_adviser == None:
                        messages.error(
                            response, "ERROR: You Should request first or accepted by the adviser!")
                        return HttpResponseRedirect(response.path)
                    else:
                        # SAVING THE INPUT TO DATABASE
                        try:
                            saverequest = Panel3request(user=response.user, name=panel3name)
                            saverequest.save()
                            messages.success(response, 'Success! Request was sent. Await for Acceptance')
                        except:
                            messages.error(response, 'Error! Cannot process your request')
                        return HttpResponseRedirect(response.path)
        

        # GET ADVISER REQUEST LIST
        adviserrequests = Adviserrequest.objects.filter(user=response.user)

        # SEE IF THERE IS AN ADVISER ACCEPTED REQUEST - IF YES - STUDENTS CAN'T REQUEST ANYMORE
        reqaccepted = Adviserrequest.objects.filter(user=response.user).filter(status='accepted')
        if reqaccepted:
            adviser_accepted = True
        else:
            adviser_accepted = False

        # GET PANEL1 REQUEST LIST
        panel1requests = Panel1request.objects.filter(user=response.user)

        # SEE IF THERE IS AN PANEL1 ACCEPTED REQUEST - IF YES - STUDENTS CAN'T REQUEST ANYMORE
        reqpanel1accepted = Panel1request.objects.filter(user=response.user).filter(status='accepted')
        if reqpanel1accepted:
            panel1_accepted = True
        else:
            panel1_accepted = False

        # GET PANEL2 REQUEST LIST
        panel2requests = Panel2request.objects.filter(user=response.user)

        # SEE IF THERE IS AN PANEL1 ACCEPTED REQUEST - IF YES - STUDENTS CAN'T REQUEST ANYMORE
        reqpanel2accepted = Panel2request.objects.filter(user=response.user).filter(status='accepted')
        if reqpanel2accepted:
            panel2_accepted = True
        else:
            panel2_accepted = False


        # GET PANEL3 REQUEST LIST
        panel3requests = Panel3request.objects.filter(user=response.user)

        # SEE IF THERE IS AN PANEL1 ACCEPTED REQUEST - IF YES - STUDENTS CAN'T REQUEST ANYMORE
        reqpanel3accepted = Panel3request.objects.filter(user=response.user).filter(status='accepted')
        if reqpanel3accepted:
            panel3_accepted = True
        else:
            panel3_accepted = False

        return render(response, 'adviserpanelistproposal/student_adpa.html', {
            "UserInfo": UserInfo,
            "name": name,
            "userrole": userrole,
            "resuser": resuser,
            "titles": titles,
            "users": users,
            "adviserrequests": adviserrequests,
            "adviser_accepted": adviser_accepted,
            "panel1requests": panel1requests,
            "panel1_accepted": panel1_accepted,
            'panel2requests': panel2requests,
            'panel2_accepted': panel2_accepted,
            'panel3requests': panel3requests,
            'panel3_accepted': panel3_accepted,


        })
    else:
        return redirect("page404")


@login_required
def faculty_student_request(response):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "2" or response.user.userprofile.role == "1":

        # REQUIRED FOR SIDEBAR AND NAVBAR
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()
        resuser = response.user
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

        #LIMIT
        limit = Limitation.objects.all()
        for l in limit:
            print(l)

        # GET ADVISER REQUEST
        adviserrequests = Adviserrequest.objects.filter(name=response.user).filter(user__userprofile__group_adviser=None)

        # GET PANEL1 REQUEST
        panel1requests = Panel1request.objects.filter(name=response.user).filter(user__userprofile__group_panel_1=None)

        # GET PANEL2 REQUEST
        panel2requests = Panel2request.objects.filter(name=response.user).filter(user__userprofile__group_panel_2=None)
        print(panel2requests)

        # GET PANEL3 REQUEST
        panel3requests = Panel3request.objects.filter(name=response.user).filter(user__userprofile__group_panel_3=None)
        print(panel3requests)


        # POST
        if response.method == 'POST':

            # IF FACULTY  PRESSED ACCEPT as ADVISER
            if response.POST.get('adviseraccept') != None:
                id = response.POST.get('adviseraccept')
                
                adviser_limits = AdviserAndPanelist.objects.filter(adviser=response.user.id)
                count_adviser = adviser_limits.count()
                print(count_adviser)
                if count_adviser >= l.limit:
                    messages.error(response, "Error: You reach the limitation as a adviser!")
                    return HttpResponseRedirect(response.path)
                else:
                    # GET OBJECT
                    studreq = Adviserrequest.objects.get(id=id)

                    if AdviserAndPanelist.objects.filter(panel1=response.user.id, user=studreq.user) | AdviserAndPanelist.objects.filter(panel2=response.user.id, user=studreq.user) | AdviserAndPanelist.objects.filter(panel3=response.user.id, user=studreq.user):
                        messages.error(response, "You are already panelist in this group!")
                        return HttpResponseRedirect(response.path)
                    
                    else:
                        studreq.status = 'accepted'
                        studreq.save()

                        # EDIT STUDENT USERPROFILE
                        user = studreq.user.userprofile
                        user.group_adviser = response.user
                        user.group_title = studreq.finaltitle
                        user.save()

                        print(user.group_adviser, user.group_title)

                        # EDIT AAP MODEL
                        title = ProposeTitle.objects.get(title=studreq.proposedtitle)
                        print(title)
                        aap = AdviserAndPanelist(user=studreq.user, adviser=response.user.userprofile, proposed_title=title,
                                                final_title=studreq.finaltitle)
                        aap.save()

                        messages.success(response, "Accepted! ")
                        return HttpResponseRedirect(response.path)
                




            # IF FACULTY PRESSED DECLINE as ADVISER
            elif response.POST.get('adviserdecline') != None:
                id = response.POST.get('adviserdecline')
                studreq = Adviserrequest.objects.get(id=id)
                studreq.status = 'decline'
                studreq.save()
                return HttpResponseRedirect(response.path)


            # IF FACULTY PRESSED ACCEPT as PANEL1
            elif response.POST.get('panel1accept') != None:
                print("panel1accept")

                id = response.POST.get('panel1accept')
                #LIMITATION AS PANELIST 1

                # FILTER ID IN EVERY PANELIST FIELD
                panel1_limits_1 = AdviserAndPanelist.objects.filter(
                    panel1=response.user.id)
                panel1_limits_2 = AdviserAndPanelist.objects.filter(
                    panel2=response.user.id)
                panel1_limits_3 = AdviserAndPanelist.objects.filter(
                    panel3=response.user.id)

                # ADD ALL COLLECTED ID OF PANEL1
                p1count1 = panel1_limits_1.count()
                p1count2 = panel1_limits_2.count()
                p1count3 = panel1_limits_3.count()
                count_panel1 = p1count1 + p1count2 + p1count3
                print(count_panel1)

                if count_panel1 >= l.limit:
                    messages.error(response, "Error: You reach the limitation as a panelist")
                    return HttpResponseRedirect(response.path)
                else:

                    # GET OBJECT
                    studreq = Panel1request.objects.get(id=id)

                    if AdviserAndPanelist.objects.filter(panel2=response.user.id, user=studreq.user) | AdviserAndPanelist.objects.filter(panel3=response.user.id, user=studreq.user):
                    
                        
                        
                        messages.error(response, "You are already panelist in this group!")
                        return HttpResponseRedirect(response.path)
                    elif AdviserAndPanelist.objects.filter(adviser=response.user.id, user=studreq.user):
                        messages.error(response, "You are already Adviser in this group!")
                        return HttpResponseRedirect(response.path)
                    else:
                        
                        studreq.status = 'accepted'
                        studreq.save()

                        # EDIT STUDENT USERPROFILE
                        user = studreq.user.userprofile
                        user.group_panel_1 = response.user
                        user.save()

                        # EDIT AAP MODEL
                        aap = AdviserAndPanelist.objects.get(user=studreq.user)
                        aap.panel1 = response.user.userprofile
                        aap.save()

                        pend_panel2 = Panel2request.objects.filter(name=response.user, user=studreq.user)
                        for p_p2 in pend_panel2:
                            p_p2.user = None
                            p_p2.name = None
                            p_p2.timestamp = None
                            p_p2.status = ""
                            p_p2.save() 

                        pend_panel3 = Panel3request.objects.filter(
                            name=response.user, user=studreq.user)
                        for p_p3 in pend_panel3:
                            p_p3.user = None
                            p_p3.name = None
                            p_p3.timestamp = None
                            p_p3.status = ""
                            p_p3.save()

                        # pend_adviser = Adviserrequest.objects.filter(
                        #     name=response.user, user=studreq.user)
                        # for p_a in pend_adviser:
                        #     p_a.user = None
                        #     p_a.name = None
                        #     p_a.proposedtitle = None
                        #     p_a.finaltitle = None
                        #     p_a.titledescription = None
                        #     p_a.timestamp = None
                        #     p_a.status = ""
                        #     p_a.save()

                        messages.success(response, "Accepted! ")
                        return HttpResponseRedirect(response.path)

                        


            # IF FACULTY PRESSED DECLINE as PANEL1
            elif response.POST.get('panel1decline') != None:
                print('panel1decline')

                id = response.POST.get('panel1decline')

                studreq = Panel1request.objects.get(id=id)
                studreq.status = 'decline'
                studreq.save()
                return HttpResponseRedirect(response.path)


            # IF FACULTY PRESSED ACCEPT as PANEL2
            elif response.POST.get('panel2accept') != None:

                print("panel2accept")

                id = response.POST.get('panel2accept')

                #LIMITATION AS PANELIST 2
                # FILTER ID IN EVERY PANELIST FIELD
                panel2_limits_1 = AdviserAndPanelist.objects.filter(panel1=response.user.id)
                panel2_limits_2 = AdviserAndPanelist.objects.filter(panel2=response.user.id)
                panel2_limits_3 = AdviserAndPanelist.objects.filter(panel3=response.user.id)

                # ADD ALL COLLECTED ID OF PANEL1
                p2count1 = panel2_limits_1.count()
                p2count2 = panel2_limits_2.count()
                p2count3 = panel2_limits_3.count()
                count_panel2 = p2count1 + p2count2 + p2count3
                print(count_panel2)

                if count_panel2 >= l.limit:
                    messages.error(response, "Error: You reach the limition as a panelist!")
                    return HttpResponseRedirect(response.path)

                else:
                    # GET OBJECT
                    studreq = Panel2request.objects.get(id=id)

                    if AdviserAndPanelist.objects.filter(panel1=response.user.id, user=studreq.user) | AdviserAndPanelist.objects.filter(panel3=response.user.id, user=studreq.user):
                        messages.error(response, "You are already panelist in this group!")
                        return HttpResponseRedirect(response.path)
                    elif AdviserAndPanelist.objects.filter(adviser=response.user.id, user=studreq.user):
                        messages.error(response, "You are already Adviser in this group!")
                        return HttpResponseRedirect(response.path)
                    else:
                        studreq.status = 'accepted'
                        studreq.save()

                        # EDIT STUDENT USERPROFILE
                        user = studreq.user.userprofile
                        user.group_panel_2 = response.user
                        user.save()

                        # EDIT AAP MODEL
                        aap = AdviserAndPanelist.objects.get(user=studreq.user)
                        aap.panel2 = response.user.userprofile
                        aap.save()

                        pend_panel1 = Panel1request.objects.filter(
                            name=response.user, user=studreq.user)
                        for p_p1 in pend_panel1:
                            p_p1.user = None
                            p_p1.name = None
                            p_p1.timestamp = None
                            p_p1.status = ""
                            p_p1.save()

                        pend_panel3 = Panel3request.objects.filter(
                            name=response.user, user=studreq.user)
                        for p_p3 in pend_panel3:
                            p_p3.user = None
                            p_p3.name = None
                            p_p3.timestamp = None
                            p_p3.status = ""
                            p_p3.save()

                        # pend_adviser = Adviserrequest.objects.filter(
                        #         name=response.user, user=studreq.user)
                        # for p_a in pend_adviser:
                        #     p_a.user = None
                        #     p_a.name = None
                        #     p_a.proposedtitle = None
                        #     p_a.finaltitle = None
                        #     p_a.titledescription = None
                        #     p_a.timestamp = None
                        #     p_a.status = ""
                        #     p_a.save()

                        messages.success(response, "Accepted! ")
                        return HttpResponseRedirect(response.path)

            # IF FACULTY PRESSED DECLINE as PANEL2
            elif response.POST.get('panel2decline') != None:
                print('panel2decline')
                id = response.POST.get('panel2decline')
                studreq = Panel2request.objects.get(id=id)
                studreq.status = 'decline'
                studreq.save()
                return HttpResponseRedirect(response.path)


            # IF FACULTY PRESSED ACCEPT as PANEL3
            elif response.POST.get('panel3accept') != None:

                print("panel3accept")

                id = response.POST.get('panel3accept')
                #LIMITATION AS PANELIST 3
                # FILTER ID IN EVERY PANELIST FIELD
                panel3_limits_1 = AdviserAndPanelist.objects.filter(panel1=response.user.id)
                panel3_limits_2 = AdviserAndPanelist.objects.filter(panel2=response.user.id)
                panel3_limits_3 = AdviserAndPanelist.objects.filter(panel3=response.user.id)

                # ADD ALL COLLECTED ID OF PANEL1
                p3count1 = panel3_limits_1.count()
                p3count2 = panel3_limits_2.count()
                p3count3 = panel3_limits_3.count()
                count_panel3 = p3count1 + p3count2 + p3count3
                print(count_panel3)

                if count_panel3 >= l.limit:
                    messages.error(response, "Error: You reach the limitation as panelist" )
                    return HttpResponseRedirect(response.path)
                else:
                    # GET OBJECT
                    studreq = Panel3request.objects.get(id=id)
                    if AdviserAndPanelist.objects.filter(panel2=response.user.id, user=studreq.user) | AdviserAndPanelist.objects.filter(panel1=response.user.id, user=studreq.user):
                        messages.error(response, "You are already panelist in this group!")
                        return HttpResponseRedirect(response.path)
                    elif AdviserAndPanelist.objects.filter(adviser=response.user.id, user=studreq.user):
                        messages.error(response, "You are already Adviser in this group!")
                        return HttpResponseRedirect(response.path)
                    else:
                        studreq.status = 'accepted'
                        studreq.save()

                        # EDIT STUDENT USERPROFILE
                        user = studreq.user.userprofile
                        user.group_panel_3 = response.user
                        user.save()

                        # EDIT AAP MODEL
                        aap = AdviserAndPanelist.objects.get(user=studreq.user)
                        aap.panel3 = response.user.userprofile
                        aap.save()

                        pend_panel1 = Panel1request.objects.filter(
                            name=response.user, user=studreq.user)
                        for p_p1 in pend_panel1:
                            p_p1.user = None
                            p_p1.name = None
                            p_p1.timestamp = None
                            p_p1.status = ""
                            p_p1.save()

                        pend_panel2 = Panel2request.objects.filter(
                            name=response.user, user=studreq.user)
                        for p_p2 in pend_panel2:
                            p_p2.user = None
                            p_p2.name = None
                            p_p2.timestamp = None
                            p_p2.status = ""
                            p_p2.save()

                        # pend_adviser = Adviserrequest.objects.filter(
                        #     name=response.user, user=studreq.user)
                        # for p_a in pend_adviser:
                        #     p_a.user = None
                        #     p_a.name = None
                        #     p_a.proposedtitle = None
                        #     p_a.finaltitle = None
                        #     p_a.titledescription = None
                        #     p_a.timestamp = None
                        #     p_a.status = ""
                        #     p_a.save()

                        messages.success(response, "Accepted! ")
                        return HttpResponseRedirect(response.path)

            # IF FACULTY PRESSED DECLINE as PANEL3
            elif response.POST.get('panel3decline') != None:
                print('panel3decline')
                id = response.POST.get('panel3decline')
                studreq = Panel3request.objects.get(id=id)
                studreq.status = 'decline'
                studreq.save()
                return HttpResponseRedirect(response.path)


            # ERROR
            else:
                messages.error(response, 'Error! Cannot process your request')

        return render(response, 'adviserpanelistproposal/faculty_student_request.html', {
            "name": name,
            "userrole": userrole,
            "resuser": resuser,
            "adviserrequests": adviserrequests,
            "panel1requests": panel1requests,
            "panel2requests": panel2requests,
            "panel3requests":panel3requests,
            "adviser":adviser,

        })
    else:
        return redirect("page404")


@login_required
def faculty_student_request_adviser(response, id):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "2" or response.user.userprofile.role == "1":

        # REQUIRED FOR SIDEBAR AND NAVBAR
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()
        resuser = response.user
        adviser = AdviserAndPanelist.objects.filter(
            adviser=resuser.userprofile)

        # GET ADVISER REQUEST
        adviserrequests = Adviserrequest.objects.filter(id=id)
        print(adviserrequests)

        return render(response, 'adviserpanelistproposal/requests/faculty_student_request_adviser.html', {
            "name": name,
            "userrole": userrole,
            "resuser": resuser,
            "adviserrequests": adviserrequests,
            "adviser":adviser,

        })
    else:
        return redirect("page404")


@login_required
def faculty_student_request_panel1(response, id):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "2" or response.user.userprofile.role == "1":

        # REQUIRED FOR SIDEBAR AND NAVBAR
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()
        resuser = response.user
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

        # GET ADVISER REQUEST
        panel1requests = Panel1request.objects.filter(id=id)
        print(panel1requests)

        return render(response, 'adviserpanelistproposal/requests/faculty_student_request_panel1.html', {
            "name": name,
            "userrole": userrole,
            "resuser": resuser,
            "panel1requests": panel1requests,
            "adviser":adviser,

        })
    else:
        return redirect("page404")


# PANEL2
@login_required
def faculty_student_request_panel2(response, id):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "2" or response.user.userprofile.role == "1":

        # REQUIRED FOR SIDEBAR AND NAVBAR
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()
        resuser = response.user
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

        # GET ADVISER REQUEST
        panel1requests = Panel2request.objects.filter(id=id)
        print(panel1requests)

        return render(response, 'adviserpanelistproposal/requests/faculty_student_request_panel1.html', {
            "name": name,
            "userrole": userrole,
            "resuser": resuser,
            "panel1requests": panel1requests,
            "adviser":adviser,

        })
    else:
        return redirect("page404")


# PANEL3
@login_required
def faculty_student_request_panel3(response, id):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "2" or response.user.userprofile.role == "1":

        # REQUIRED FOR SIDEBAR AND NAVBAR
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()
        resuser = response.user
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

        # GET ADVISER REQUEST
        panel1requests = Panel3request.objects.filter(id=id)
        print(panel1requests)

        return render(response, 'adviserpanelistproposal/requests/faculty_student_request_panel1.html', {
            "name": name,
            "userrole": userrole,
            "resuser": resuser,
            "panel1requests": panel1requests,
            "adviser":adviser,

        })
    else:
        return redirect("pae404")




@login_required
def FacultyAdviserAndPanelistView(response):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "2" or response.user.userprofile.role == "1":

        list = AdviserAndPanelist.objects.filter(adviser=response.user.id) | AdviserAndPanelist.objects.filter(
            panel1=response.user.id) | AdviserAndPanelist.objects.filter(
            panel2=response.user.id) | AdviserAndPanelist.objects.filter(
            panel3=response.user.id)

        adviserlists = AdviserAndPanelist.objects.filter(adviser=response.user.id)

        panelistlists = AdviserAndPanelist.objects.filter(
            panel1=response.user.id) | AdviserAndPanelist.objects.filter(
            panel2=response.user.id) | AdviserAndPanelist.objects.filter(
            panel3=response.user.id)

        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        adviser = AdviserAndPanelist.objects.filter(
            adviser=resuser.userprofile)

        # GET NUMBER OF PENDING REQUESTS
        p_adviser = Adviserrequest.objects.filter(name=response.user).filter(status='pending').filter(
            user__userprofile__group_adviser=None)
        p_panel1 = Panel1request.objects.filter(name=response.user).filter(status='pending').filter(
            user__userprofile__group_panel_1=None)
        p_panele2 = Panel2request.objects.filter(name=response.user).filter(status='pending').filter(
            user__userprofile__group_panel_2=None)
        p_panele3 = Panel3request.objects.filter(name=response.user).filter(status='pending').filter(
            user__userprofile__group_panel_3=None)

        a = p_adviser.count()
        p1 = p_panel1.count()
        p2 = p_panele2.count()
        p3 = p_panele3.count()
        pendingrequests = a + p1 + p2 + p3

        return render(response, 'adviserpanelistproposal/adpa.html', {
            'list': list,
            "adviserlists": adviserlists,
            "panelistlists": panelistlists,
            "name": name,
            'userrole': userrole,
            "unseen": unseen,
            "resuser": resuser,
            "pendingrequests": pendingrequests,
            "adviser":adviser
        })

    else:
        return redirect("page404")


@login_required
def delete_adviserandpanelist(response, myid):
    pass


@login_required
def reqadviser(response):
    userrole = response.user.userprofile.role
    name = response.user.get_full_name()

    # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
    resuser = response.user
    unseen = 0
    adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

    return render(response, 'adviserpanelistproposal/request/reqadviser.html', {
        "name": name,
        'userrole': userrole,
        "unseen": unseen,
        "resuser": resuser,
        "adviser":adviser,
    })


def AdviserViewRequestsOfAdvisoree(response, id):

    adviserlists = AdviserAndPanelist.objects.filter(adviser=response.user.id, user=id)

    UserInfo = UserProfile.objects.get(user=id)

    # GET ADVISER REQUEST
    adviserrequests = Adviserrequest.objects.filter(user=id)

    # GET PANEL1 REQUEST
    panel1requests = Panel1request.objects.filter(user=id)

    # GET PANEL2 REQUEST
    panel2requests = Panel2request.objects.filter(user=id)
    

    # GET PANEL3 REQUEST
    panel3requests = Panel3request.objects.filter(user=id)

    userrole = response.user.userprofile.role
    name = response.user.get_full_name()
    

    # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
    resuser = response.user
    unseen = 0
    adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile) 
    
    return render(response, "adviserpanelistproposal/requests/advisoreegrouprequests.html", {
        'adviserlists':adviserlists,
        'adviserrequests': adviserrequests,
        'userrole':userrole,
        'name':name,
        'resuser':resuser,
        'unseen':unseen,
        'panel1requests': panel1requests,
        'panel2requests':panel2requests,
        'panel3requests': panel3requests,
        'UserInfo':UserInfo,
        "adviser":adviser,

    })
