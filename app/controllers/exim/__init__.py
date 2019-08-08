try:
    from .blueprint import controller
except ImportError:
    import traceback
    traceback.print_exc()