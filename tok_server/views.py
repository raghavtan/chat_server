__author__ = 'rt'

from django.shortcuts import *
from django.template import *
from opentok import OpenTok
from django.http import *
import json


def index(request, ses_id):
    key = "45351832"
    secret = "29d4d704b3a28373202c230946bfe91e3e74c4fb"
    opentok = OpenTok(key, secret)
    if request.method == "POST":
        name = request.POST.get('name', '')
        ses_id = request.POST.get('session', '')
        try:
            if ses_id is "":
                ses = "New Session"
                session = opentok.create_session()
                session_id = session.session_id
            else:
                ses = "Existing Session"
                session_id = ses_id
            token = opentok.generate_token(session_id)
            data = {"user": name, "Session": ses, "session:": {"Authentication": token, "Session ID": session_id}}
        except Exception as e:
            data = {"Exception": e.message, "Type": type(e)}
        return JsonResponse(data)
