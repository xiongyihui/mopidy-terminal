from __future__ import unicode_literals

import logging
import os

from mopidy import config, ext


__version__ = '0.1.2'

logger = logging.getLogger(__name__)


class Extension(ext.Extension):

    dist_name = 'Mopidy-Terminal'
    ext_name = 'terminal'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def setup(self, registry):

        registry.add('http:static', {
            'name': self.ext_name,
            'path': os.path.join(os.path.dirname(__file__), 'static'),
        })

        registry.add('http:app', {
            'name': self.ext_name,
            'factory': self.factory,
        })

    def factory(self, config, core):
        from terminado import TermSocket, UniqueTermManager

        class WebSocketHandler(TermSocket):
            def check_origin(self, origin=None):
                return True

        term_manager = UniqueTermManager(shell_command=['ssh', 'localhost'])
        return [
            ("/websocket", WebSocketHandler, {'term_manager': term_manager}),
        ]
