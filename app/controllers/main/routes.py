from .blueprint import controller as main


@main.route('/')
def health():
    return 'OK', 200
