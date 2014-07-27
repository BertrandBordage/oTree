import ptree.test
import stag_hunt.views as views
from stag_hunt.utilities import Bot
import random


class ParticipantBot(Bot):

    def play(self):

        # random decision
        choice = random.choice((('Stag', 'Stag'), ('Hare', 'Hare')))[0]

        self.submit(views.Decide, {"decision": choice})

        # results
        self.submit(views.Results)