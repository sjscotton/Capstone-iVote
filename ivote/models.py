from django.db import models

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

    def get_address(self):
        return self.city


class Vote_Date(models.Model):

    state_voter_id = models.CharField(max_length=15, default='00')
    county_code = models.CharField(max_length=10, default='00')
    election_date = models.CharField(max_length=15, default="00")

    def __str__(self):
        return f'{self.state_voter_id}, {self.election_date}, {self.county_code}'
