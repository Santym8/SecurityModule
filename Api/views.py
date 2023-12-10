from rest_framework.decorators import api_view
from rest_framework.response import Response
from AdministrationSite.audit.models import Audit
from AdministrationSite.user.models import User
from AdministrationSite.function.models import Function
from .requests.PostAuditRequest import PostAuditRequest
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

def validate_jwt(request):
    try:
        payload = jwt.decode(request.headers["Authorization"], key="secret", algorithms="HS256")
        user = User.objects.filter(username=payload["username"])
        if user.count() == 0:
            return None
        return user.first()
    except:
        return None
    

@api_view(["POST"])
def register_audit(request):
    user = validate_jwt(request)
    if user is None:
        return Response({"message":"Invalid jwt"}, status=400)

    audit_request = PostAuditRequest(data=request.data) 
    if not audit_request.is_valid():
        return Response(
            {
                "message":"Invalid request", 
                "errors": audit_request.errors
            }, 
            status=400
        )

    function = Function.objects.filter(name=audit_request.data["function_name"])
    if function.count() == 0:
        return Response({"message":"Function not found"}, status=404)
    function = function.first()
  
    audit = Audit(
        action=audit_request.data["action"],
        description=audit_request.data["description"],
        observation=audit_request.data["observation"] or None,
        ip=audit_request.data["ip"],
        date=audit_request.data["date"],
        user=user,
        function=function
    )
    audit.save()   
    return Response({"message":"Register audit"}, status=200)

