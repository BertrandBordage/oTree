# -*- coding: utf-8 -*-
import guessing.models as models
from guessing._builtin import Page, WaitPage


class Introduction(Page):

    template_name = 'guessing/Introduction.html'

    def variables_for_template(self):
        return {'players_count': len(self.player.other_players_in_subsession()),
                'winner_payoff': self.treatment.winner_payoff}


class Guess(Page):

    template_name = 'guessing/Guess.html'

    form_model = models.Player
    form_fields = ['guess_value']


class Results(Page):

    template_name = 'guessing/Results.html'

    def variables_for_template(self):
        other_guesses = [p.guess_value for p in self.player.other_players_in_subsession()]

        return {'guess_value': self.player.guess_value,
                'other_guesses': other_guesses,
                'other_guesses_count': len(other_guesses),
                'two_third_average': round(self.subsession.two_third_guesses, 4),
                'players': self.subsession.players,
                'is_winner': self.player.is_winner,
                'payoff': self.player.payoff}


class ResultsWaitPage(WaitPage):

    group = models.Match

    def after_all_players_arrive(self):
        self.subsession.set_payoffs()


def pages():

    return [Introduction,
            Guess,
            ResultsWaitPage,
            Results]
