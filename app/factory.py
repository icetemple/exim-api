import os
import sys
import logging
import logging.config

from flask import Flask
from werkzeug.utils import find_modules, import_string
from werkzeug.middleware.proxy_fix import ProxyFix


class Factory(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wsgi_app = ProxyFix(self.wsgi_app, x_for=1, x_proto=1, x_host=1)

    def process_response(self, response):
        response.headers['server'] = self.config['SERVER_HEADER']
        super().process_response(response)
        return response

    def register_controllers(self, package_name='app.controllers'):
        if not self._ismainrun():
            return

        try:
            logging.debug('controller {}'.format(package_name))
            import_string(package_name)
        except ImportError:
            logging.error('failed import in package {}'.format(package_name))
            return

        for name in find_modules(package_name, True):
            try:
                logging.debug('controller {}'.format(name))
                mod = import_string(name)
            except ImportError:
                logging.error('failed import in package {}'.format(name))
                continue

            if hasattr(mod, 'controller'):
                self.register_blueprint(mod.controller)

    def _ismainrun(self):
        return not self.debug \
               or os.environ.get('WERKZEUG_RUN_MAIN') == 'true' \
               or sys.argv[0].endswith('sphinx-build') \
               or sys.argv[0].endswith('gunicorn')
