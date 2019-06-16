from random import randint
from prometheus_client import Counter, Gauge


CRITTER_PURRS_COUNT = Counter("critter_purrs_count", "Total count of critter purrs")
CRITTER_MOOD = Gauge("critter_mood", "Current mood of the critter")


class Critter:
    def activate(self):
        CRITTER_MOOD.set(randint(0, 9))
        return True

    def purr(self):
        CRITTER_PURRS_COUNT.inc()
        return True

    def blink(self):
        return True

