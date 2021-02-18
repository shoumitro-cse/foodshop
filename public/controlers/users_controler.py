from public.models import Users


class UserData:

    def __init__(self):
        pass

    def getUserId(self, user_email):
        user_check_list = Users.objects.filter(email=user_email)
        if user_check_list:
            user_obj = user_check_list[0]
            return user_obj.id
        else:
            return None

    def getUserObj(self, user_email):
        user_check_list = Users.objects.filter(email=user_email)
        if user_check_list:
            user_obj = user_check_list[0]
            return user_obj
        else:
            return None

    def getSessionUserEmail(self, request):
        if request.session.has_key('username'):
            email = request.session['username']
            return email
        else:
            return None

