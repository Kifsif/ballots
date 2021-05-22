from django import template

from ballots.models import Ballot

register = template.Library()


@register.simple_tag
def ballots(id: int) -> str:
    votes = Ballot.objects.get(pk=id)

    return str(votes)
