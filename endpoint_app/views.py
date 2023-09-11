from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import pytz

# Create your views here.


def get_info(request):
    slack_name = request.GET.get("slack_name")
    track = request.GET.get("track")

    current_day = datetime.now(pytz.utc).strftime("%A")

    utc_time = datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    github_file_url = "https://github.com/Josh565565/endpoin-with-django/blob/main/endpoint_app/views.py"
    github_repo_url = "https://github.com/Josh565565/endpoin-with-django"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200,
    }

    return JsonResponse(response_data)
