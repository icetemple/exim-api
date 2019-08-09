try:
    from .blueprint import controller
    from . import routes
except ImportError:
    import traceback
    traceback.print_exc()