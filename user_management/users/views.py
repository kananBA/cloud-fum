from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from users.serializers import UserSerializer, User


# Create your views here.
class UserApi(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, user_id=None):
        if user_id is None:
            users = User.objects.all()
            users_serializer = UserSerializer(users, many=True)
            return JsonResponse(users_serializer.data, safe=False)
        else:
            user = User.objects.get(id=user_id)
            users_serializer = UserSerializer(user)
            return JsonResponse(users_serializer.data, safe=False)

    def post(self, request):
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=user_data)
        if users_serializer.is_valid():
            user = users_serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = users_serializer.data
                json['token'] = token.key
                return JsonResponse({
                    "message": "User has been added",
                    "data": json,
                    }, safe=False
                )
        return JsonResponse(users_serializer.errors, safe=False)


class AuthApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return JsonResponse({"success": True}, safe=False)

