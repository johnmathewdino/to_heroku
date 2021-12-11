from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist

# from django.shortcuts import redirect


class OnlyOneUserMiddleware(object):
    """
    Middleware to ensure that a logged-in user only has one session active.
    Will kick out any previous session. 
    """
    def process_request(self, request):
        if request.user.is_authenticated():
            cur_session_key = request.user.get_profile().session_key
            if cur_session_key and cur_session_key != request.session.session_key:
                # Default handling... kick the old session...
                try:
                    s = Session.objects.get(session_key=cur_session_key)
                    s.delete()
                except ObjectDoesNotExist:
                    pass
            if not cur_session_key or cur_session_key != request.session.session_key:
                p = request.user.get_profile()
                p.session_key = request.session.session_key
                p.save()

# class OneSessionPerUserMiddleware:
#     # Called only once when the web server starts


#     def __init__(self, get_response):
#         self.get_response = get_response


#     def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#         if request.user.is_authenticated:
#             session_key = request.session.session_key

#             try:
#                 logged_in_user = request.user.logged_in_user
#                 stored_session_key = logged_in_user.session_key
#                 # stored_session_key exists so delete it if it's different
#                 if stored_session_key and stored_session_key != request.session.session_key:
#                     Session.objects.get(session_key=stored_session_key).delete()
                    
#                 request.user.logged_in_user.session_key = request.session.session_key
#                 request.user.logged_in_user.save()
#             except Session.DoesNotExist:
#                 Session.objects.create(session_key=session_key)
                
#             stored_session_key = request.user.logged_in_user.session_key

#             # if there is a stored_session_key  in our database and it is
#             # different from the current session, delete the stored_session_key
#             # session_key with from the Session table
#             if stored_session_key and stored_session_key != request.session.session_key:
#                 Session.objects.get(session_key=stored_session_key).delete()
#                 # return redirect("login")

#             request.user.logged_in_user.session_key = request.session.session_key
#             request.user.logged_in_user.save()

#         response = self.get_response(request)

#         # This is where you add any extra code to be executed for each request/response after
#         # the view is called.
#         # For this tutorial, we're not adding any code so we just return the response

#         return response


# # class OneSessionPerUserMiddleware:
# #     # Called only once when the web server starts
# #     def __init__(self, get_response):
# #         self.get_response = get_response

# #     def __call__(self, request):
# #         # Code to be executed for each request before
# #         # the view (and later middleware) are called.
# #         if request.user.is_authenticated:
# #             stored_session_key = request.user.logged_in_user.session_key

# #             # if there is a stored_session_key  in our database and it is
# #             # different from the current session, delete the stored_session_key
# #             # session_key with from the Session table
# #             if stored_session_key and stored_session_key != request.session.session_key:
# #                 Session.objects.get(session_key=stored_session_key).delete()

# #             request.user.logged_in_user.session_key = request.session.session_key
# #             request.user.logged_in_user.save()

# #         response = self.get_response(request)

# #         # This is where you add any extra code to be executed for each request/response after
# #         # the view is called.
# #         # For this tutorial, we're not adding any code so we just return the response

# #         return response
