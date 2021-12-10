from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Comment, Topic
from .forms import PostForm, CommentForm, TopicForm
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib import messages
from proposalpanelists.models import AdviserAndPanelist


# Create your views here.


@login_required
def topic(response):
    form = TopicForm()
    if response.method == "POST":
        form = TopicForm(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, "Topic Successfully Posted!")
            return HttpResponseRedirect(response.path)
        else:
            messages.error(response, "Invalid Input!")
            return HttpResponseRedirect(response.path)

    userrole = response.user.userprofile.role
    name = response.user.get_full_name()
    Topics = Topic.objects.all()
    topics = []
    for topic in Topics:
        numpost = Post.objects.filter(topic=topic)
        numreplies = Comment.objects.filter(topic=topic)
        topic_id = topic.id
        topic_description = topic.description
        topics.append([topic_id, topic, topic_description,
                      len(numpost), len(numreplies)])
    print(topics)

    # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
    resuser = response.user
    adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

    return render(response, 'forum/forum_topic.html', {
        "form": form,
        "topics": topics,
        "userrole": userrole,
        "name": name,
        "resuser": resuser,
        "adviser":adviser,
    })


def forum(response, id):
    topic = Topic.objects.filter(id=id).first()
    posts = Post.objects.filter(topic=topic)
    user = response.user

    form = PostForm()
    if response.method == "POST":
        form = PostForm(response.POST, response.FILES)
        if form.is_valid():
            save = form.save(commit=False)
            save.user = response.user
            save.topic = topic
            save.save()
            messages.success(response, "Successfully Posted!")
            return HttpResponseRedirect(response.path)
        else:
            messages.error(response, "Invalid Input!")
            return HttpResponseRedirect(response.path)

    userrole = response.user.userprofile.role
    name = response.user.get_full_name()
    # print(posts)

    postslist = []
    for list in posts:
        comment = Comment.objects.filter(post=list)
        # id, user, title, timestamp, content, lencomment, image
        postslist.append([list.id, list.user, list.title, list.timestamp,
                         list.post_content, len(comment), list.image])
    print(postslist)

    # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
    resuser = response.user
    adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

    return render(response, 'forum/forum.html', {
        "topic": topic,
        'form': form,
        'posts': posts,
        'user': user,
        "userrole": userrole,
        "name": name,
        "postslist": postslist,
        "resuser": resuser,
        "adviser":adviser,
    })


def discussion(response, id):
    post = Post.objects.filter(id=id).first()
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    user = response.user
    if response.method == "POST":
        form = CommentForm(response.POST)
        if form.is_valid():

            user = response.user
            comment = response.POST.get('comment_content', '')
            image = response.POST.get('image', '')
            reply = Comment(
                post=post, user=user, comment_content=comment, image=image, topic=post.topic)
            reply.save()
            messages.success(response, "Successfully Posted!")
            return HttpResponseRedirect(response.path)
        else:
            messages.error(response, "Invalid Input!")
            return HttpResponseRedirect(response.path)

    userrole = response.user.userprofile.role
    name = response.user.get_full_name()

    # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
    resuser = response.user
    adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

    return render(response, 'forum/forum_discussion.html', {
        'post': post,
        'comments': comments,
        'form': form,
        'user': user,
        "userrole": userrole,
        "name": name,
        "resuser": resuser,
        "adviser":adviser,
    })


def update_topic(response, id):
    topic = Topic.objects.filter(id=id).first()
    if id:
        topic = get_object_or_404(Topic, id=id)
    if response.method == "POST":
        form = TopicForm(response.POST, instance=topic)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(response, "Successfully Edited!")
            return redirect("topic")
        else:
            messages.error(response, "Invalid Input!")
            return redirect("topic")

    else:
        form = TopicForm(instance=topic)
    userrole = response.user.userprofile.role

    # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
    resuser = response.user
    adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

    return render(response, 'forum/edit_topic.html', {
        'form': form,
        'userrole': userrole,
        'topic': topic,
        "resuser": resuser,
        "adviser":adviser,
    })


def delete_topic(response, id):
    topic = get_object_or_404(Topic, id=id)
    topic.delete()
    messages.error(response, "Deleted!")
    return redirect('topic')


def update_forum(response, id):
    post = Post.objects.filter(id=id).first()
    if id:
        post1 = get_object_or_404(Post, id=id)
    if response.method == "POST":
        form = PostForm(response.POST, instance=post1)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(response, "Successfully Edited!")
            return redirect('forum', post.topic.id)
        else:
            messages.error(response, "Invalid Input!")
            return redirect('forum', post.topic.id)

    form = PostForm(instance=post1)

    userrole = response.user.userprofile.role

    # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
    resuser = response.user
    adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

    return render(response, 'forum/edit_forum.html', {

        'form': form,
        'userrole': userrole,
        'post': post,
        "resuser": resuser,
        "adviser":adviser,
    })


def delete_forum(response, id):
    post = Post.objects.filter(id=id).first()
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.error(response, "Deleted!")
    return redirect('forum', post.topic.id)


def update_reply(response, id):
    comment = Comment.objects.filter(id=id).first()
    if id:
        comment = get_object_or_404(Comment, id=id)
    if response.method == "POST":
        form = CommentForm(response.POST, instance=comment)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(response, "Successfully Edited!")
            return redirect('forum_discussion', comment.post.id)
        else:
            messages.error(response, "Invalid Input!")
            return redirect('forum_discussion', comment.post.id)
            
    else:
        form = CommentForm(instance=comment)

    userrole = response.user.userprofile.role
    adviser = AdviserAndPanelist.objects.filter(adviser=resuser.userprofile)

    # FOR CHAT PLEASE INCLUDE IN EVERY VIEWS and OUTPUT resuser AND unseen
    resuser = response.user

    return render(response, 'forum/edit_reply.html', {
        'form': form,
        'comment': comment,
        'userrole': userrole,
        "resuser": resuser,
        "adviser":adviser,
    })


def delete_reply(response, id):
    comment = Comment.objects.filter(id=id).first()
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    messages.error(response, "Deleted!")
    return redirect('forum_discussion', comment.post.id)
