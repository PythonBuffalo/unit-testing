import mock


class Test(object):
    def get_db_connection(self):
        print 'calling Test.get_db_connection'
        return {}  # imagine this as an actual db connection

    def get_results_from_db(self):
        print 'calling Test.get_results_from_db'
        connection = self.get_db_connection()
        connection.execute('some sql statement')
        return connection.fetchall()


# mocking get_results_from_db on a "real" instance
t = Test()
t.get_results_from_db = mock.Mock(return_value=[1, 2, 3, 4])
print t.get_results_from_db()


# creating a custom function to call for the mocked method
def mocked_get_db_connection():
    print 'calling mocked_get_db_connection'
    connection = mock.Mock()
    connection.fetchall.return_value = [1, 2, 3, 4]
    return connection

t = Test()
t.get_db_connection = mock.Mock(side_effect=mocked_get_db_connection)
print t.get_results_from_db()


# creating a mimic mock of the class
test_mock = mock.Mock(spec=Test)
test_mock.get_results_from_db.return_value = [1, 2, 3, 4]
print test_mock.get_results_from_db()
