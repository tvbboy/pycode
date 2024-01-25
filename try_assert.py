try:  
    a = 100
    b = 99
    assert a == b
except AssertionError:  
        print ("Assertion Exception Raised.")
else:  
    print ("Success, no error!")