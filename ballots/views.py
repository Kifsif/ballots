from django.views.generic import DetailView, ListView

from ballots.models import Ballot


class DebugBallotDetailView(DetailView):
    model = Ballot


class DebugBallotListView(ListView):
    model = Ballot
