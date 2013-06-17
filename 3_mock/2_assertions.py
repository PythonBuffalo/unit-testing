import mock

mocked_obj = mock.Mock()
mocked_obj()

print 'some_method was called: %r' % (mocked_obj.called, )

# reset the state of called
mocked_obj.reset_mock()
print 'some_method was called: %r' % (mocked_obj.called, )

# call mocked method with arguments
mocked_obj('here', 'are', some='arguments')
mocked_obj.assert_called_with('here', 'are', some='arguments')

# get the arguments that the method was called with
print 'some_method was called with %r' % (mocked_obj.call_args, )

# invalid argument assertion throws the proper exception
try:
    mocked_obj.assert_called_with('other' 'arguments')
except AssertionError:
    print 'some_method was not called with those arguments'

# get the number of times the method was called
mocked_obj('other', 'arguments')
print 'some_method has been called %s times' % (mocked_obj.call_count, )

# get all the method calls to the mock object
mocked_obj.other_method()
mocked_obj.test.some.deeply.nested.method(with_some='args')
print 'mocked_obj has had the following method calls %r' % (mocked_obj.method_calls, )
