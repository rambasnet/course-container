import hi

def test_hi():
    assert hi.answer() == 'Hello World!'

def test_hi_fail():
    assert hi.answer() == 'Hello World!'
    print('This will not print')