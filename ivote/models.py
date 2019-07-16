from django.db import models
from django.contrib.postgres.fields import ArrayField
import datetime

# Create your models here.


class Voter(models.Model):
    state_voter_id = models.CharField(max_length=25, default='00')
    county_voter_id = models.CharField(max_length=25, default='00')
    f_name = models.CharField(max_length=30, default='00')
    m_name = models.CharField(max_length=30, default='00')
    l_name = models.CharField(max_length=30, default='00')
    name_suffix = models.CharField(max_length=10, default='00')
    birthdate = models.CharField(max_length=15, default='00')
    gender = models.CharField(max_length=5, default='00')
    st_num = models.CharField(max_length=15, default='00')
    st_frac = models.CharField(max_length=10, default='00')
    st_name = models.CharField(max_length=50, default='00')
    st_type = models.CharField(max_length=20, default='00')
    unit_type = models.CharField(max_length=15, default='00')
    st_post_direction = models.CharField(max_length=5, default='00')
    st_pre_direction = models.CharField(max_length=5, default='00')
    unit_num = models.CharField(max_length=15, default='00')
    city = models.CharField(max_length=30, default='00')
    state = models.CharField(max_length=10, default='00')
    zip_code = models.CharField(max_length=10, default='00')
    county_code = models.CharField(max_length=20, default='00')
    precinct_code = models.CharField(max_length=20, default='00')
    precinct_part = models.CharField(max_length=20, default='00')
    legislative_district = models.CharField(max_length=10, default='00')
    congressional_district = models.CharField(max_length=10, default='00')
    registration_date = models.CharField(max_length=15, default='00')
    absentee_type = models.CharField(max_length=10, default='00')
    last_voted = models.CharField(max_length=15, default='00')
    status_code = models.CharField(max_length=10, default='00')

    def __str__(self):
        return self.f_name

    def get_age_group(self):
        year = datetime.datetime.now().year
        age = year - int(self.birthdate.split('/')[2])
        if age < 25:
            return '18-24'
        elif age < 35:
            return '25-34'
        elif age < 45:
            return '35-44'
        elif age < 55:
            return '45-54'
        elif age < 65:
            return '55-64'
        elif age < 75:
            return '65-74'
        elif age < 85:
            return '75-84'
        else:
            return '85+'

    def get_address(self):

        return f'{self.st_num} {self.st_pre_direction} {self.st_name} {self.st_type} {self.st_post_direction} {self.unit_type}{self.unit_num}, {self.city}, {self.state}, {self.zip_code}'


class Vote_Date(models.Model):

    state_voter_id = models.CharField(max_length=15, default='00')
    county_code = models.CharField(max_length=10, default='00')
    election_date = models.CharField(max_length=15, default="00")

    def __str__(self):

        return f'{self.state_voter_id}, {self.election_date}, {self.county_code}'


class Election(models.Model):
    county_code = models.CharField(max_length=10, default='00')
    election_date = models.CharField(max_length=15, default="00")

    def __str__(self):

        return f'{self.county_code}, {self.election_date}'


# TODO: combine county_votes and city votes into one table

class Voting_Stats(models.Model):
    county_code = models.CharField(max_length=10, default='00')
    city = models.CharField(max_length=30, default='00')
    voting_freq = ArrayField(models.IntegerField(), size=10,)
    age_group = models.CharField(max_length=20, default='00')

    @staticmethod
    def get_max_votes(rows):
        totals = []
        for i in range(len(rows[0].voting_freq)):
            total = 0
            for row in rows:
                total += row.voting_freq[i]
            totals.append(total)
        sample_size = sum(totals)
        max_votes = len(totals) - 1
        for i in range(len(totals)):
            if (totals[max_votes] / sample_size) < .03:
                max_votes -= 1
            else:
                break
        return max_votes


class County_Votes(models.Model):
    county_code = models.CharField(max_length=10, default='00')
    zero = models.IntegerField()
    one = models.IntegerField()
    two = models.IntegerField()
    three = models.IntegerField()
    four = models.IntegerField()
    five = models.IntegerField()
    six = models.IntegerField()
    seven = models.IntegerField()

    def __str__(self):

        return f'County: {self.county_code} \nNumber of Elections: '

    def sample_size(self):
        return self.zero + self.one + self.two + self.three + self.four + self.five + self.six + self.seven

    def max_votes(self):
        votes = [self.seven, self.six, self.five, self.four,
                 self.three, self.two, self.one, self.zero]
        max_elections = 7
        for freq in votes:
            if freq != 0:
                break
            max_elections -= 1
        return max_elections


class City_Votes(models.Model):
    city = models.CharField(max_length=30, default='00')
    zero = models.IntegerField()
    one = models.IntegerField()
    two = models.IntegerField()
    three = models.IntegerField()
    four = models.IntegerField()
    five = models.IntegerField()
    six = models.IntegerField()
    seven = models.IntegerField()
    eight = models.IntegerField()

    def __str__(self):

        return f'City: {self.city}'

    def sample_size(self):
        return self.zero + self.one + self.two + self.three + self.four + self.five + self.six + self.seven + self.eight

    def max_votes(self):
        votes = [self.seven, self.six, self.five, self.four,
                 self.three, self.two, self.one, self.zero]
        max_elections = 7
        for freq in votes:
            if freq != 0:
                break
            max_elections -= 1
        return max_elections
