from django.shortcuts import render
from django.http import JsonResponse
from ivote.models import Voter
from ivote.models import Vote_Date
from ivote.models import Election
from ivote.models import County_Votes
from ivote.models import City_Votes
from ivote.models import Voting_Stats
from django.db import models

import random

# Create your views here.


def index(request):
    county_codes = []
    voters = Voter.objects.all()
    # for v in voters:
    #     if v.county_code not in county_codes:
    #         county_codes.append(v.county_code)
    #         print(v.county_code)

    return JsonResponse({"data": county_codes})


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
        'voter_id': person.state_voter_id,
        'address': person.get_address(),
        'county_code': person.county_code,
        'city': person.city,
        'age_group': person.get_age_group()
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


def get_addresses(request):
    quantity = request.GET.get('quantity', None)
    quantity = quantity or 5
    voters = Voter.objects.all()

    addresses = []
    for i in range(quantity):
        rand = random.randint(0, 1000000)
        address = voters[rand].get_address()
        addresses.append(address)
    data = {
        'addresses': addresses
    }
    return JsonResponse(data, status=200)


def get_elections(request):
    county_code = request.GET.get('county_code', None)
    city = request.GET.get('city', None)
    if not county_code:
        return JsonResponse({'message': "Must supply county_code"}, status=400)

    # elections = Election.objects.filter(county_code=county_code)
    # election_dates = [election.election_date for election in elections]
    # print(election_dates)
    # return JsonResponse({'election_dates': election_dates}, status=200)

    if city:
        row = City_Votes.objects.get(city=city)
        print('======== City =========')
    else:
        row = County_Votes.objects.get(county_code=county_code)
        print('======== County =========')

    max_elections = row.max_votes()
    return JsonResponse({'max_elections': max_elections}, status=200)


def get_stats(request):

    age_group = request.GET.get('age_group', None)
    city = request.GET.get('city', None)
    county_code = request.GET.get('county', None)

    if age_group and city:
        rows = Voting_Stats.objects.filter(age_group=age_group, city=city)
    elif age_group and county_code:
        rows = Voting_Stats.objects.filter(
            age_group=age_group, county_code=county_code)
    elif city:
        rows = Voting_Stats.objects.filter(city=city)
    elif county_code:
        rows = Voting_Stats.objects.filter(county_code=county_code)
    else:
        return JsonResponse({'message': "Must supply age_group, and city or county_code"}, status=400)
    max_votes = Voting_Stats.get_max_votes(rows)
    data = {}
    data['county_code'] = rows[0].county_code
    data['city'] = rows[0].city
    for row in rows:
        # data.append({'city': row.city, 'county_code': row.county_code, 'age_group': row.age_group,
        #              'voting_freq': row.voting_freq})
        print("++++++++++++++++++++++++++++++")
        print(row.voting_freq)
        print(row.voting_freq[:max_votes + 1])
        data[row.age_group] = row.voting_freq[:max_votes + 1]

    return JsonResponse({'stats': data}, status=200)
