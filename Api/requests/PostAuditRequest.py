from rest_framework import serializers
from AdministrationSite.audit.models import Audit

class PostAuditRequest(serializers.ModelSerializer):
    function_name = serializers.CharField(max_length=50, required=False)
    class Meta:
        model = Audit
        fields = [
            "action", 
            "description", 
            "observation", 
            "ip", 
            "date", 
            "function_name"
        ]
