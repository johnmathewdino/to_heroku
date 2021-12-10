# from django.contrib.sessions.models import Session
# from django.contrib.auth.signals import user_logged_in
# from django.db.models import Q
# from django.utils import timezone


# def limit_sessions(sender, user, request, **kwargs):
#     # this will be slow for sites with LOTS of active users

#     for session in Session.objects.filter(
#         ~Q(session_key=request.session.session_key),
#         expire_date__gte=timezone.now()
#     ):
#         data = session.get_decoded()
#         if data.get('_auth_user_id', None) == str(user.id):
#             # found duplicate session, expire it
#             session.expire_date = timezone.now()
#             session.save()

#     return


# user_logged_in.connect(limit_sessions)
