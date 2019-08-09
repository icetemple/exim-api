from .blueprint import controller as queue
from app.helpers.exim import get_queue, get_queue_count


@queue.route('/')
def emails():
    stdout, stderr = get_queue()
    return stderr or stdout, 400 if stderr else 200


@queue.route('/count')
def count():
    stdout, stderr = get_queue_count()
    return stderr or stdout, 400 if stderr else 200

