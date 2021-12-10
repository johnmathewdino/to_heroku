from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import GuideForm
from .models import guide, guide_topic
from django.contrib import messages
from proposalpanelists.models import AdviserAndPanelist



def Guide(request):
    topics = guide_topic.objects.all()
    contents = guide.objects.all()
    if request.method == "POST":
        form = GuideForm(request.POST, request.FILES)
        topic = request.POST.get("topic")
        if form.is_valid():
            if guide_topic.objects.filter(guidetopic=topic):
                topic = guide_topic.objects.filter(guidetopic=topic).first()
            else:
                topic_save = guide_topic(guidetopic=topic)
                topic_save.save()
                topic = guide_topic.objects.filter(guidetopic=topic).first()
            save = form.save(commit=False)
            save.topic = topic
            save.save()   
            messages.success(request, 'Success! Guide Posted!')
            return HttpResponseRedirect(request.path)
        else:
            messages.error(request, 'Error! Invalid!')
            return HttpResponseRedirect(request.path)

    form = GuideForm()


    posted = guide.objects.all()
    userrole = request.user.userprofile.role
    name = request.user.get_full_name()

    # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
    resuser = request.user
    adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)




    return render(request, 'guide/guide.html', {
        'form':form,
        'posted': posted,
        'topics':topics,
        'contents':contents,
        "userrole": userrole,
        "name": name,
        "resuser": resuser,
        'adviser':adviser,
    })



def Edit_Guide(response, id):
    if response.user.userprofile.role == "1" or response.user.userprofile.role == "2":

        contents = guide.objects.filter(id=id).first()
        topics = guide_topic.objects.all()
        user = response.user
        if id:
            contents = get_object_or_404(guide, id=id)
        if response.method == "POST":
            form = GuideForm(response.POST, response.FILES, instance=contents)
            topic = response.POST.get("topic")
            if form.is_valid():
                if guide_topic.objects.filter(guidetopic=topic):
                    topic = guide_topic.objects.filter(guidetopic=topic).first()
                else:
                    topic_save = guide_topic(guidetopic=topic)
                    topic_save.save()
                    topic = guide_topic.objects.filter(guidetopic=topic).first()
                save = form.save(commit=False)
                save.topic = topic
                save.user = user
                save.save()
                messages.success(response, 'Successfully Edited!')
                return redirect('guide')
            else:
                messages.error(response, 'Invalid input!')

        else:
            form = GuideForm(instance=contents)
        userrole = response.user.userprofile.role

        # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
        resuser = response.user

        return render(response, 'guide/edit_guide.html', {
            'form':form,
            'contents':contents,
            "userrole": userrole,
            "resuser": resuser,

        })
    else:
        return redirect("page404")


def Delete_guide(response, id):
    contents = guide.objects.filter(id=id).first()
    contents = get_object_or_404(guide, id=id)
    contents.delete()
    messages.error(response, 'Successfully Deleted!')
    return redirect('guide')





def guidepost(response, id):
    userrole = response.user.userprofile.role
    name = response.user.get_full_name()



    posts = guide.objects.get(id=id)

    # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
    resuser = response.user
    adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)


    return render(response, 'guide/guidepost.html',
              {
                  "posts": posts,
                  "userrole": userrole,
                  "name": name,
                  "resuser": resuser,
                  "adviser":adviser,
              })

