import random
import time

import mock


class DBConnection(object):
    def fetch_all_the_things(self):
        pass

    def fetch_all(self):
        pass

    def execute(self, query, bindings):
        pass


class DBCaller(object):
    def __init__(self):
        self.connection = DBConnection()

    def get_random(self):
        results = self.connection.fetch_all_the_things()
        for result in results:
            if random.random() > .5:
                yield result

    def get_time(self):
        self.connection.execute('get where time < %s',
                                (time.time(), ))
        return self.connection.fetch_all()


with mock.patch("__main__.DBConnection") as db:
    with mock.patch("random.random", return_value=1):
        with mock.patch("time.time", return_value=1371504225):
            expected = [1, 2, 3, 4, 5]
            caller = DBCaller()
            caller.connection.fetch_all_the_things.return_value = expected
            results = list(caller.get_random())
            assert results == expected
            results = caller.get_time()
