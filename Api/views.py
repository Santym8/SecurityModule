from rest_framework.decorators import api_view
from rest_framework.response import Response
from AdministrationSite.user.models import User
from .requests.LoginRequest import LoginRequest
import jwt

@api_view(["POST"])
def login(request):
    login_request = LoginRequest(data=request.data)

    if not login_request.is_valid():
        return Response(
            {
                "message":"Invalid request", 
                "errors": login_request.errors
             }, 
            status=400
        )

    user = User.objects.filter(email=login_request.data["user"])
    if user.count() == 0:
        user = User.objects.filter(username=login_request.data["user"]) 

    if user.count() == 0:
        return Response({"message":"User not found"}, status=404)
    
    user = user.first()
    if not user.check_utn_credentials(login_request.data["password"]):
        return Response({"message":"Password incorrect"}, status=400)
    
    payload = {
        "username": user.username,
    }

    jwt_response = jwt.encode(payload=payload, key="secret", algorithm="HS256")

    response = {
        "message":"Login success",
        "user": user.email,
        "functionalities": user.get_all_functionalities(),
        "jwt": jwt_response,
    }
    return Response(response, status=200)
