from otree.api import Currency as c, currency_range, BasePlayer
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass


class Link(Page):
    form_model = 'group'
    form_fields = ['n_linked_words', 'link_word', 'linked_words', 'confidence']

    # display this page only to HQ
    def is_displayed(self):
        hq = self.group.get_player_by_role('HQ')
        return self.player.id_in_group == hq.id_in_group

    #display the correct pattern card
    def vars_for_template(self):
        id = self.player.in_round(1).id_in_group
        print(id)
        return {'pattern_1': id}

class WaitForHQ(WaitPage):
    def is_displayed(self):
        field = self.group.get_player_by_role('Field')
        return self.player.id_in_group == field.id_in_group


class Contact(Page):
    form_model = 'group'
    form_fields = ['guessing']

    # display this page only to Field Agent
    def is_displayed(self):
        field = self.group.get_player_by_role('Field')
        return self.player.id_in_group == field.id_in_group


class WaitForField(WaitPage):
    def is_displayed(self):
        hq = self.group.get_player_by_role('HQ')
        return self.player.id_in_group == hq.id_in_group


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.define_success()


class Results(Page):
    def vars_for_template(self):
        return {'next_r': sum([self.group.how_success for x in self.group.in_all_rounds()])}


page_sequence = [
    Instructions,
    Link,
    WaitForHQ,
    Contact,
    WaitForField,
    ResultsWaitPage,
    Results
]
