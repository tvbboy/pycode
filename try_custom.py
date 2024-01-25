try:  
    raise EmptyError( "The variable is empty" )  
except (EmptyError, var):  
    print( var.arguments ) 