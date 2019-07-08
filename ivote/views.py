from django.shortcuts import render
from django.http import JsonResponse
from ivote.models import Voter
from ivote.models import Vote_Date
from django.db import models

# Create your views here.


def index(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }

    return JsonResponse(data)


def show(request):

    first_name = request.GET.get('first_name', None)
    last_name = request.GET.get('last_name', None)

    birthdate = request.GET.get('birthdate', None)

    if not first_name or not last_name or not birthdate:
        return JsonResponse({'message': "Must supply first_name, last_name and birthdate"}, status=400)

    try:
        person = Voter.objects.get(
            f_name=first_name.upper(), l_name=last_name.upper(), birthdate=birthdate.replace('-', '/'))
    except:
        return JsonResponse({'message': f'Record not found for {first_name} {last_name}.'}, status=404)

    data = {
        'first_name': person.f_name,
        'last_name': person.l_name,
        "middle_name": person.m_name,
        'city': person.city,
        'voter_id': person.state_voter_id,
        'address': person.get_address(),
    }

    return JsonResponse(data, status=200)


def show_votes(request):
    voter_id = request.GET.get('state_voter_id', None)
    if not voter_id:
        return JsonResponse({'message': "Must supply state_voter_id"}, status=400)

    votes = Vote_Date.objects.filter(state_voter_id=voter_id)
    data = {
        'voting_days': [vote.election_date for vote in votes]
    }

    return JsonResponse(data, status=200)
