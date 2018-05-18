from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'D & N'

doc = """
Game inspired by cardgame Codenames
"""


class Constants(BaseConstants):
    name_in_url = 'codenames'
    players_per_group = 2
    num_rounds = 80
    all_words = 25
    marked_words = 15

class Subsession(BaseSubsession):
    def creating_session(self):
        print('in creating_session')
        #switch the roles in rounds that are even (i.e. 2,4,6,8 etc)
        if self.round_number ==1:
            pass
        else:
            if self.round_number % 2 == 0:
                print("Switching Roles NOW")
                # reverse the roles
                matrix = self.get_group_matrix()
                for row in matrix:
                    row.reverse()
                self.set_group_matrix(matrix)
            else:
                print("Switching back NOW")
                self.group_like_round(1)

class Group(BaseGroup):
    #filled by HQ
    n_linked_words = models.IntegerField(min=1,max=9)
    link_word = models.StringField()
    linked_words = models.StringField()
    confidence = models.IntegerField(min=0, max=10)

    #filled by field agent
    guessing = models.StringField()

    #filled by define_success based on players' input
    how_success = models.IntegerField(min=0, max=n_linked_words)
    is_success = models.BooleanField()


    def define_success(self):
        #split linked words by comma
        linked_split = [x.strip() for x in self.linked_words.split(',') if x != '']
        #split guessing by comma
        guessing_split = [x.strip() for x in self.guessing.split(',') if x != '']

        #compare the splitted lists
        compare = set(linked_split) & set(guessing_split)
        self.how_success = len(compare)
        if self.how_success == self.n_linked_words:
            self.is_success = True
        else:
            self.is_success = False


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'HQ'
        if self.id_in_group == 2:
            return 'Field'


