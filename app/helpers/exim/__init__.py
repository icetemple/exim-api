from ..process import Process


EXIM = '/usr/sbin/exim'


def _call(command):
    try:
        return Process(command).communicate()
    except FileNotFoundError as e:
        return '', str(e)


def get_queue():
    return _call([EXIM, '-bp'])


def get_queue_count():
    return _call([EXIM, '-bpc'])


def check_delivery_route(email):
    return _call([EXIM, '-bt', email])
