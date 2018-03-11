import inspect
import os
from pathlib import Path
import toml

from . import settings, utils

OPTIONS_FILE = 'defaults.toml'


@utils.run_once
def initialize(start_py: str, debug: bool = False, finalize_settings: bool = True):
    options_path = find_options_file(start_py)
    options = toml.load(options_path.as_posix())

    try:
        settings.ROUTES_MODULE = options['django']['routes-module']
        settings.SETTINGS_MODULE = options['django']['settings-module']
    except KeyError as err:
        raise RuntimeError(f'Improperly configured {OPTIONS_FILE}') from err

    settings.DJANGO_ROOT = options_path.parent

    if not finalize_settings:
        return

    settings.finalize(debug=debug)

    comment = '(autoreload.py)' if os.environ.get('RUN_MAIN') == 'true' else ''
    print(f'Initialized django-defaults in {settings.DJANGO_ROOT} {comment}')


def find_options_file(start_py: str = __file__) -> Path:
    p2 = Path(start_py).resolve()

    while True:
        p = p2.parent
        if p is p2:
            start = Path(start_py).parent.resolve()
            raise RuntimeError(f'Cannot find {OPTIONS_FILE} (starting from {start}, got to {p})')

        options = p / OPTIONS_FILE
        if options.is_file():
            return options

        p2 = p


def emplace(*, debug: bool = True):
    """
    Copy settings from the `defaults.settings` module to this function's callsite.
    """

    frame = inspect.stack()[1]

    initialize(frame.filename, debug)

    module = inspect.getmodule(frame.frame)

    for a in dir(settings):
        if utils.should_copy(a):
            setattr(module, a, getattr(settings, a))


def setenv(*, bundled: bool = False):
    if not bundled:
        frame = inspect.stack()[1]

        initialize(frame.filename, finalize_settings=False)

    assert settings.SETTINGS_MODULE is not None

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings.SETTINGS_MODULE)
