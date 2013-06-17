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
    def __init__(self, connection=DBConnection):
        self.connection = connection()

    def get_random(self, random=random.random):
        results = self.connection.fetch_all_the_things()
        for result in results:
            if random() > .5:
                yield result

    def get_time(self, time=time.time):
        self.connection.execute('get where time < %s',
                                (time(), ))
        return self.connection.fetch_all()


mock_db = mock.Mock(spec=DBConnection)
mock_random = mock.Mock(return_value=1)
mock_time = mock.Mock(return_value=1371504225)
expected = [1, 2, 3, 4, 5]
caller = DBCaller(connection=mock_db)
caller.connection.fetch_all_the_things.return_value = expected
results = list(caller.get_random(random=mock_random))
assert results == expected
results = caller.get_time(time=mock_time)
