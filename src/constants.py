from utils import create_keyboard
from types import SimpleNamespace


KEYS = SimpleNamespace(**dict(
    random_connect=':bust_in_silhouette: Random Connect',
    settings=':gear: Settings'
))

KEYBOARDS = SimpleNamespace(**dict(
    main = create_keyboard([KEYS.random_connect, KEYS.settings])
))