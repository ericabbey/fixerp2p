import datetime
from mail_templated import send_mail

from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from .models import Action


def create_action(user, verb, extra, target=None):
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    similar_actions = Action.objects.filter(user_id=user.id, verb = verb, created__gte=last_minute)
    if target:
        target_ct = ContentType.objects.get_for_model(target)
        similar_actions = similar_actions.filter(target_ct=target_ct, target_id=target.id)
    if not similar_actions:
        # no existing actions found
        action = Action(user=user, verb=verb, target=target, additional=extra)
        action.save()
        return True
    return False


def sendmail(user, data, email=None):
    send_mail('email/hello.tpl', {'user': user}, 'FixerP2P', ['ericabbey.cyber@gmail.com'])