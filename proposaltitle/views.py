from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from register.models import UserProfile
from .forms import ProposeTitleForm, TitleCommentForm, CommentReplyForm
from .models import CommentReply, ProposeTitle, TitleComment, CommentReply
from django.contrib import messages
from proposalpanelists.models import AdviserAndPanelist

@login_required
def StudentTitleview(response):
    if response.user.userprofile.role == "4":

        form = ProposeTitleForm()
        name = response.user
        group = UserProfile.objects.get(user=response.user).group_name
        print(response.POST.get("description"))
        if response.method == "POST":
            form = ProposeTitleForm(response.POST)
            if form.is_valid():
                save = form.save(commit=False)
                save.user = response.user
                if group == None or group == "":
                    messages.error(response, "Error: You don't have group yet!")
                    return HttpResponseRedirect(response.path)
                else:
                    save.group = group
                    save.description = response.POST.get("description")
                    save.save()
                    messages.success(response, "Propose Title Successfully submitted!")
                    return HttpResponseRedirect(response.path)
            else:
                messages.error(response, "Invalid Input!")
                return HttpResponseRedirect(response.path)

        titlelist = ProposeTitle.objects.filter(user=name)
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0




        return render(response, 'proposaltitle/student/StudentTitle.html',{
            "titlelist": titlelist,
            "userrole": userrole,
            "form": form,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
        })
    else:
        return redirect("page404")

@login_required
def FacultyTitleview(response):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "2" or response.user.userprofile.role == "1":
        titlelist = ProposeTitle.objects.all()

        groupnames = []
        for title in titlelist:
            name = title.group
            id = title.user_id
            user = UserProfile.objects.get(id=id)
            title_count = ProposeTitle.objects.filter(
                user=id, status="").count()
            if [name,id,user, title_count] not in groupnames:
                # print(name)
                # print(title.user)
                if title.group != "None":
                    groupnames.append([name, id, user, title_count])
                    print("here")
                if title.group == "None" :
                    groupnames.append([title.user.get_full_name, id, title_count])

        
        print(title_count)
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        adviser = AdviserAndPanelist.objects.filter(
            adviser=resuser.userprofile)



        return render(response, 'proposaltitle/faculty/FacultyTitle.html', {
            'titlelist': titlelist,
            "userrole": userrole,
            "groupnames":groupnames,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
            "adviser":adviser,
            'title_count': title_count,
            
                  
            })
    else:
        return redirect("page404")


@login_required
def TitleList(response, id):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "2" or response.user.userprofile.role == "1":
        titlelist = ProposeTitle.objects.filter(user=id).all()
        # print(titlelist)
        groupname = []
        for title in titlelist:
            if title.group not in groupname:
                groupname.append(title.group)

        # print(groupname)
        userrole = response.user.userprofile.role
        # print(ProposeTitle.objects.values("user"))
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)




        return render(response, 'proposaltitle/faculty/Title_list.html', {
            'titlelists':titlelist,
            "userrole": userrole,
            "groupname":groupname,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
            'adviser':adviser,
        })
    else:
        return redirect("page404")

@login_required
def Edit_title(response, id):
    if response.user.userprofile.role == "4":
        if id:
            title = get_object_or_404(ProposeTitle, id=id)
        if response.method == "POST":
            form = ProposeTitleForm(response.POST, instance=title)
            if form.is_valid():
                save = form.save(commit=False)
                save.user = response.user
                if response.POST.get("edit") != "" or response.POST.get("edit") != None:
                    save.status = ""
                    save.edited = response.POST.get("edit")
                    save.save()
                    return HttpResponseRedirect(reverse("Student_Title"))
                else:
                    save.edited = None
                    save.save()
                    # return redirect('Student_Title')
                    # return HttpResponseRedirect('student/proposal/title/')
                    return HttpResponseRedirect(reverse("Student_Title"))
        else:
            form = ProposeTitleForm(instance=title)
        userrole = response.user.userprofile.role
        titles = ProposeTitle.objects.get(id=id)
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0





        return render(response, 'proposaltitle/student/edit_title.html', {
            'form':form,
            "userrole": userrole,
            "titles":titles,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,

        })
    else:
        return redirect("page404")
#
@login_required
def StudentTitleCommentview(response, id):
    if response.user.userprofile.role == "4":
        title = ProposeTitle.objects.filter(id=id).first()
        comments = TitleComment.objects.filter(title=title)
        if response.method == "POST":
            author = response.user
            comment = response.POST.get("comment")
            title = title
            com = TitleComment(comment=comment, author=author, title=title)
            print(com)
            com.save()
            messages.success(response, "Successfully Replied!")

        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0

        return render(response, 'proposaltitle/student/title_comment.html',{
            'comments':comments,
            'title':title,
            "userrole": userrole,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
        })
    else:
        return redirect("page404")


@login_required
def FacultyTitleCommentView(response,id):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "2" or response.user.userprofile.role == "1":
        title = ProposeTitle.objects.filter(id=id).first()
        print(title.user.id)
        name = response.user
        title_comment = TitleComment.objects.filter(title = title)
        form = TitleCommentForm()
        accepted = response.POST.get("status")
        comment = response.POST.get("Comment")
        print(accepted)
        print(comment)
        if response.method == "POST":
            if accepted != None:
                print("status",title.status)
                title.status = accepted
                if title.status == "Accepted":
                    title.save()
                    messages.success(response, "Title Accepted!")
                elif title.status == "Rejected":
                    title.save()
                    messages.error(response, "Title Rejected!")
                elif title.status == "Title Needs Clarifications":
                    title.save()
                    messages.warning(response, "Title Needs Clarifications")

                return HttpResponseRedirect('/proposal/titlelist/'+str(title.user.id)+'/')
            if comment != None:
                comment = response.POST.get("comment")
                save = TitleComment(comment=comment, author=response.user, title=title)
                save.save()
                messages.success(response, "Comment Successfully delivered!")
                return HttpResponseRedirect('/proposal/titlelist/' + str(title.user.id) + '/')



        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)



        return render(response, 'proposaltitle/faculty/title_comment.html',{
            'title':title,
            'comments': title_comment,
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
def Edit_comment(response, id):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "2" or response.user.userprofile.role == "1" or response.user.userprofile.role == "4":
        action = response.POST.get("action")
        if id:
            comment = get_object_or_404(TitleComment, id=id)
            if response.method == "POST":
                # submit
                # delete
                # back
                if action == "submit":
                    form = TitleCommentForm(response.POST, instance=comment)
                    if response.user.userprofile.role == "4":
                        save = form.save(commit=False)
                        save.save()
                        messages.success(response, "Comment Successfully Edited!")
                        return redirect('StudentTitleComment', comment.title.id)
                    else:
                        if form.is_valid():
                            save = form.save(commit=False)
                            save.status = response.POST.get('status')
                            save.save()
                            messages.success(response, "Comment Successfully Edited!")
                            return redirect('FacultyTitleComment', comment.title.id)
                elif action == "delete":
                    if response.user.userprofile.role == "4":
                        comment = get_object_or_404(TitleComment, id=id)
                        comment.delete()
                        messages.error(response, "Comment Deleted!")
                        return redirect('StudentTitleComment', comment.title.id)
                    else:
                        comment = get_object_or_404(TitleComment, id=id)
                        comment.delete()
                        messages.error(response, "Comment Deleted!")
                        return redirect('FacultyTitleComment',comment.title.id)

                elif action == "back":
                    if response.user.userprofile.role == "4":
                        return redirect('StudentTitleComment', comment.title.id)
                    else:
                        return redirect('FacultyTitleComment',comment.title.id)

        comment = get_object_or_404(TitleComment, id=id)
        form = TitleCommentForm(instance=comment)
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0
        adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)



        return render(response, "proposaltitle/faculty/edit_comment.html",{
            'form':form,
            "comment":comment,
            "userrole": userrole,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
            "adviser":adviser,
        })
    else:
        return redirect("page404")

        
# STUDENT COMMENT REPLY
def Student_Comment_ReplyView(response, id):
    if response.user.userprofile.role == "4":
        comment = TitleComment.objects.filter(id=id).first()
        com_reply = CommentReply.objects.filter(cp_comment=comment)
        form = CommentReplyForm()
        if response.method == 'POST':
            form = CommentReplyForm(response.POST)
            if form.is_valid():
                save = form.save(commit=False)
                save.user = response.user
                save.cp_comment = comment
                save.save()
                messages.success(response, "Reply Successfully Sent!")
                return HttpResponseRedirect(response.path)
            else:
                messages.error(response, "Invalid Input!")
                return HttpResponseRedirect(response.path)

        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        return render(response, 'proposaltitle/student/student_comment_reply.html',{
            'name':name,
            'form':form,
            'userrole':userrole,
            'comment':comment,
            'com_reply':com_reply,

        })
    else:
        return redirect("page404")


def Edit_comment_reply(response, id):
    if response.user.userprofile.role == "4":

        reply = CommentReply.objects.filter(id=id).first()
        if id:
            rep = get_object_or_404(CommentReply, id=id)
        if response.method == 'POST':
            form = CommentReplyForm(response.POST, instance=rep)
            if form.is_valid():
                save = form.save(commit=False)
                save.save()
                messages.success(response, "Successfully Edited!")
                
                return redirect("Student_Comment_ReplyView", reply.cp_comment.id)
            else:
                messages.error(response, "Invalid Input!")

        userrole = response.user.userprofile.role
        name = response.user.get_full_name()
        form = CommentReplyForm(instance=rep)

        return render(response, 'proposaltitle/student/edit_reply.html', {
            'name':name, 
            'userrole':userrole,
            'reply':reply,
            'form':form,

        })
    else:
        return redirect("page404")
    
            
def delete_reply(response, id):
    reply = CommentReply.objects.filter(id=id).first()
    reply.delete()
    messages.error(response, "Deleted!")
    return redirect("Student_Comment_ReplyView", reply.cp_comment.id)



def Cp_ViewReply(response, id):
    comment = TitleComment.objects.filter(id=id).first()
    reply = CommentReply.objects.filter(cp_comment=comment)
    userrole = response.user.userprofile.role
    name = response.user.get_full_name()

    return render(response, 'proposaltitle/faculty/student_reply.html', {
        'comment':comment,
        'reply':reply,
        'userrole':userrole,
        'name':name,
    })

@login_required
def studentTitleRevision(response, id):

    if response.user.userprofile.role == "4":

        form = ProposeTitleForm()
        name = response.user
        group = UserProfile.objects.get(user=response.user).group_name
        print(response.POST.get("description"))
        if response.method == "POST":
            form = ProposeTitleForm(response.POST)
            if form.is_valid():
                save = form.save(commit=False)
                save.user = response.user
                if group == None or group == "":
                    messages.error(
                        response, "Error: You don't have group yet!")
                    return HttpResponseRedirect(response.path)
                else:
                    save.group = group
                    save.description = response.POST.get("description")
                    save.save()
                    messages.success(
                        response, "Propose Title Successfully submitted!")
                    return HttpResponseRedirect(response.path)
            else:
                messages.error(response, "Invalid Input!")
                return HttpResponseRedirect(response.path)

        titlelist = ProposeTitle.objects.filter(user=name)
        userrole = response.user.userprofile.role
        name = response.user.get_full_name()

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user
        unseen = 0

        return render(response, 'proposaltitle/student/StudentTitle.html', {
            "titlelist": titlelist,
            "userrole": userrole,
            "form": form,
            "name": name,
            "unseen": unseen,
            "resuser": resuser,
        })
    else:
        return redirect("page404")
