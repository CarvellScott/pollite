#!/usr/bin/env python3
from time import time, sleep
from unittest import TestCase
from statistics import mean, pvariance

class _TimedPollTestCase(TestCase):
    def test_one_second_frequency_microsecond_precision(self):
        frequency = 1.0
        ticks = []
        for i in TimeRange(frequency, duration=30):
            ticks.append(i)
        differences = []
        for i in range(1, len(ticks) - 1):
            differences.append(ticks[i] - ticks[i - 1])
        mu = mean(differences)
        variance = pvariance(differences, mu)
        err = "Expected variance of less than 10 ** -6, got {}"
        err = err.format(variance)
        assert variance < 10.0 ** -6, variance


class TimeRange():
    """
    TimeRange is intended to be used in a loop as a way to poll some sort of
    service or periodically run some block of code subject to rate-limiting.

    It can be used as such:
    >>> for i in TimeRange(frequency=.5, duration=10):
    ...     print(i)
    `i` here will be the "most recent tick", the value of time().
    """
    def __init__(self, frequency=1, duration=1, forever=False):
        """
        @param frequency how often, in seconds, should TimeRange be polled.
        @param duration how long the TimeRange object should be polled for.
        @param forever if forever is True, TimeRange is polled forever.
        """
        self.start_time = time()
        self.end_time = self.start_time + duration
        self.most_recent_tick = self.start_time - 1
        self.frequency = frequency
        self.forever = forever

    def __iter__(self):
        return self

    def __next__(self):
        elapsed = time() - self.most_recent_tick
        if elapsed < self.frequency:
            sleep(self.frequency - elapsed)
        self.most_recent_tick = time()
        if self.forever or self.most_recent_tick < self.end_time:
            return self.most_recent_tick
        else:
            raise StopIteration
