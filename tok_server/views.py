__author__ = 'rt'

from django.shortcuts import *
from django.template import *
from opentok import OpenTok
from opentok import Roles
from django.http import *
import json


def index(request):
    key = "45351832"
    secret = "29d4d704b3a28373202c230946bfe91e3e74c4fb"
    opentok = OpenTok(key, secret)
    if request.method == "POST":
        name = request.POST.get('name', '')
        role = request.POST.get('role', '')
        if role == "": role = "Publisher"
        ses_id = request.POST.get('session', '')
        try:
            if ses_id is "":
                ses = "New Session"
                session = opentok.create_session()
                session_id = session.session_id
                token = opentok.generate_token(session_id,role=Roles.publisher)
            else:
                ses = "Existing Session"
                session_id = ses_id
                if role == "moderator":
                    token = opentok.generate_token(session_id,role=Roles.moderator)
                elif role == "subscriber":
                    token = opentok.generate_token(session_id,role=Roles.subscriber)
                else:
                    token = "Wrong Role requested for existing session id"
            data = {"user": name, "Session": ses, "role":role, "session:": {"Authentication": token, "Session ID": session_id}}
        except Exception as e:
            data = {"Exception": e.message, "Type": type(e)}
        return JsonResponse(data)
