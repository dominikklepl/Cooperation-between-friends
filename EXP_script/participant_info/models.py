from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

from codename_generator import codename


author = 'Your name here'

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = "info"
    players_per_group = 2
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    organization = models.StringField()
    def get_organization(self):
        org = codename()
        print(org)
        self.organization = org

class Player(BasePlayer):
    group_n = models.IntegerField(
        label="Group number (Researcher will tell you that)"
    )
    condition = models.StringField(
        choices=["Friendly contact","Stranger danger"],
        widget=widgets.RadioSelectHorizontal,
        label="Project (Researcher will tell you that)"
    )
    age = models.IntegerField()
    gender = models.StringField(
        choices=['Male', 'Female'],
        widget=widgets.RadioSelectHorizontal,
        label="Your Gender"
    )

    nationality = models.StringField(
        label="Your nationality"
    )
