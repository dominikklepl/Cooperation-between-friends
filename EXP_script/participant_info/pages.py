from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Intro(Page):
    pass

class Plan(Page):
    pass


class MyPage(Page):
    form_model = 'player'
    form_fields = ['group_n', 'condition', 'age', 'gender', 'nationality']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.get_organization()


class Results(Page):
    pass


page_sequence = [
    Intro,
    Plan,
    MyPage,
    ResultsWaitPage,
    Results
]
