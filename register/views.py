from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from main.models import Code
from .forms import RegisterForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib import messages
from verify_email.email_handler import send_verification_email
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from proposalpanelists.models import AdviserAndPanelist



from .models import UserProfile


def register(response):

    code = "EZ22WX"
    allusercodes = Code.objects.all()
    for usercode in allusercodes:

        if code == str(usercode.code):
            print("equal")
            if usercode.role == "Student":
                print("Student")
            else:
                print("Not ")
        else:
            print("not equal")

    #
    # if code not in Code.objects.filter(code=code):
    #     userrole = Code.objects.get(code=code)
    #     print(userrole.role)
    # else:
    #     print("Not")


    if response.method == "POST":
        form = RegisterForm(response.POST)
        profile_form = UserProfileForm(response.POST)
        allusercodes = Code.objects.all()

        if form.is_valid() and profile_form.is_valid():

            code = response.POST.get("code")

            for usercode in allusercodes:

                if code == str(usercode.code):
                    user = form.save(commit=False)
                    user.is_active = False
                    user.save()
                    profile = profile_form.save(commit=False)
                    profile.user = user


                    if usercode.role == "Student":
                        profile.role = "4"
                    elif usercode.role == "Faculty":
                        profile.role = "3"


                    profile.save()
                    current_site = get_current_site(response)
                    mail_subject = 'Activate your account.'
                    message = render_to_string('registration/acc_active_email.html', {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                    })
                    to_email = form.cleaned_data['email']
                    email = EmailMessage(mail_subject, message, to=[to_email])
                    email.send()
                    return render(response, 'registration/emailconfirm.html')


                # else:
                #
                #     messages.error(response,"Code does not exist")
            messages.error(response, "Code does not exist")

            # return redirect("/")
            # return HttpResponseRedirect(reverse("home"))
    else:
        form = RegisterForm()
        profile_form = UserProfileForm()



    return render(response, 'registration/register.html', {
        "form": form,
        "profile_form":profile_form,

    })

UserModel = get_user_model()

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'registration/emailconfirmsuccess.html')
    else:
        return render(request, 'registration/emailconfirmfail.html')


@login_required
def profile(response):
    if response.method == 'POST':
        p_form = ProfileUpdateForm(response.POST, response.FILES, instance=response.user.userprofile)
        u_form = UserUpdateForm(response.POST, instance=response.user)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            print('here')
            messages.success(response, 'Your Profile has been updated!')
            return HttpResponseRedirect(reverse("profile"))
        else:
            print("here1")
            messages.error(response, 'invalid Input!')
            return HttpResponseRedirect(reverse("profile"))
    else:
        print('hereee111')

        u_form = UserUpdateForm(instance=response.user)
        p_form = ProfileUpdateForm(instance=response.user.userprofile)
    userrole = response.user.userprofile.role
    name = response.user.get_full_name()
    names = response.user
    adviser = AdviserAndPanelist.objects.filter(adviser=names.userprofile)



    context = {'p_form': p_form, 'u_form': u_form, 'userrole':userrole, "name":name, "names":names, "adviser":adviser}
    return render(response, 'registration/profile.html', context)