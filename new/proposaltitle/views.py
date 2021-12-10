from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from .forms import ProposeTitleForm, TitleCommentForm
from .models import ProposeTitle, TitleComment
from register.models import UserProfile
from django.utils import timezone

def Titleview(response):

    if response.user.userprofile.role == "4":
        form = ProposeTitleForm()
        name = response.user
        if response.method == "POST":
            form = ProposeTitleForm(response.POST)
            if form.is_valid():
                save = form.save(commit=False)
                save.user = response.user
                save.save()

                return redirect('Title')
        titlelist = ProposeTitle.objects.filter(user=name)

        return render(response, 'main/student/proposals/title/title.html',{
            "titlelist": titlelist,
            "form":form
        })
    elif response.user.userprofile.role == "3" or response.user.userprofile.role == "2" or response.user.userprofile.role == "1":
        titlelist = ProposeTitle.objects.all()
        return render(response,'main/cp/proposals/title/title.html',{
            'titlelist':titlelist
        })

def TitleList(response, id):

    titlelist =  ProposeTitle.objects.filter(id=id).all()

    return render(response, 'main/cp/proposals/title/title_list.html', {'titlelists':titlelist})


def Edit_title(response, id):
    if id:
     title = get_object_or_404(ProposeTitle, id=id)
    if response.method == "POST":
        form = ProposeTitleForm(response.POST, instance=title)
        if form.is_valid():
            save = form.save(commit=False)
            save.user = response.user
            save.save()
            return redirect('Title')
    else:
        form = ProposeTitleForm(instance=title)

    return render(response, 'main/student/proposals/title/edit_title.html', {'form':form})


def TitleCommentview(response, id):
    if response.user.userprofile.role == "3" or response.user.userprofile.role == "2" or response.user.userprofile.role == "1":

        title = ProposeTitle.objects.filter(id=id).first()
        name = response.user
        title_comment = TitleComment.objects.filter(title = title).filter(author=name)
        form = TitleCommentForm()

        if response.method == "POST":
            form = TitleCommentForm(response.POST)
            if form.is_valid():
                save = form.save(commit=False)
                save.author = response.user
                save.title = title
                save.status = response.POST.get('status')
                save.save()
        return render(response, 'main/cp/proposals/title/titlecomment.html',{
            'title':title,
            'comment': title_comment,
            'form':form
        })
    elif response.user.userprofile.role == "4":
        title = ProposeTitle.objects.filter(id=id).first()
        comment = TitleComment.objects.filter(title=title)

        return render(response, 'main/student/proposals/title/titlecomment.html',{'comment':comment, 'title':title})


def Edit_comment(response, id):
    if id:
        comment = get_object_or_404(TitleComment, id=id)
    if response.method == "POST":
        form = TitleCommentForm(response.POST, instance=comment)

        if form.is_valid():
            save = form.save(commit=False)
            save.status = response.POST.get('status')
            save.save()
            return redirect('TitleComment', comment.title.id)
    else:
        form = TitleCommentForm(instance=comment)

    return render(response, "main/cp/proposals/title/edit_comment.html",{
        'form':form
    })

def ProposeTitleGroup(response):
    titlelist = ProposeTitle.objects.all()
    return render(response, "main/cp/proposals/title/title_group_result.html", {'titlelist':titlelist})


def ProposeTitleResult(response, id):

    title = ProposeTitle.objects.filter(id=id).first()
    comment = TitleComment.objects.filter(title=title)


    statusnum = TitleComment.objects.all().count()

    return render(response, 'main/cp/proposals/title/title_result.html', {'title':title, 'comment':comment})


def delete_comment(request, id):
    comment = TitleComment.objects.get(id=id)
    comment.delete()
    return redirect('TitleComment')
