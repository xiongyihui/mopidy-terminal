from __future__ import unicode_literals

import logging
import os

from mopidy import config, ext


__version__ = '0.1.0'

# TODO: If you need to log, use loggers named after the current Python module
logger = logging.getLogger(__name__)


def make_term_factory(config, core):
    from terminado import TermSocket, UniqueTermManager
    term_manager = UniqueTermManager(shell_command=['sh'])
    return [
        ("/websocket", TermSocket, {'term_manager': term_manager}),
    ]


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
            'factory': make_term_factory,
        })
