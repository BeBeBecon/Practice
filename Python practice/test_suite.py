import sys

def test(test_pass):

    linenum = sys._getframe(1).f_lineno
    if test_pass:
        msg = "Test at line {0} is Passed".format(linenum)
    else:
        msg = "Test at line {0} is falied".format(linenum)
    print(msg)
