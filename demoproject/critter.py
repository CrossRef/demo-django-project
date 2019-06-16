from prometheus_client import Counter, Histogram


CRITTER_PURRS_COUNT = Counter("critter_purrs_count", "Total count of critter purrs")


class Critter:
    def activate(self):
        return True

    def purr(self):
        CRITTER_PURRS_COUNT.inc()
        return True

    def blink(self):
        return True

