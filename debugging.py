# Note of debugging

# Raising the exception -> raise Exception(<mssg>) *** mssg is a helpful message
# It seem like can gracefully handle the error instead let entire programme crash
#   The exception can be store in for loop
#       eg: try :
#                .......
#           except Exception as err:
#                print("<mssg>" + str(err))
# See the notefunction0

#------------------------------------------------------
import traceback
# Getting error message
# Getting traceback as string -> traceback.format_exc()
# Through this function, you can write the error mssg into a log file...
# and keep your program running.
# See notefunction1()
# Even though the programme move forward to the exception...
# But it still can print the error mssg which in the try section
#------------------------------------------------------

#---------------------------------------------------
# Assertion - sanity check to make sure ur code wont do obviously wrong
# if the check fail , the AssertionError is raised
#   eg1: assert _____ == 'condition for testing' , 'msg when is False'
#       If true : then continue False : return the msg
#   See notefunction2
#   eg2 : assert '_' in '_' , 'msg'
#       If true : continue False : print msg and programme immediately stop
#   See notefunction3
# Conclusion : Assertion is just like the try/exception for the developer
# Disabling Assertion -> python -O / -0 <name>.py
#--------------------------------------------------------

import logging
#--------------------------------------------------------------------------------
# Logging module
# Similar to print() statement
# Understand what happen in your programme
# eg: logging.basicConfig(level=logging.DEBUG, format ='....')
#   Level : logging.debug()/logging info/logging.warning/logging.error/logging.critical
#   The level is start from bug to critical
#   U can use logging.__ to identify the error
#   %(asctime)s - timestamp
#   %(levelname)s - level
#   %(message)s - string that insert in the logging.debug('')
# See notefunction4
# The benefit of the logging is u can use command to disable it -> logging.disable(logging.CRITICAL())
# In contrast, the print() u need delete it one by one
#   Addition ( Adding the logging event to the notepad)
#   code: logging.basicConfig(filename='<name.txt>',<level>,<format>)
# ---------------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# IDLE Debugger
# Go - program will execute normally until it terminate to a breakpoint
# Step - execute the next line of  code and pause again
# Over - similar to the 'step' but it will skip the code in the function on the next line
# Out - cause the debugger to execute the lines of code at full speed until it return from the current funtion
# Quit - Stop the debugger
#-----------------------------------------------------------------------------------

def notefunction0 (symbol,width,height):
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string")
    if width <= 2:
        raise Exception("Width must be greater than 2.")
    if height <= 2:
        raise Exception("Height must be greater than 2")

    print(symbol*width)
    for i in range(height - 2) :
        print(symbol + (' ' *(width-2)) + symbol)
    print(symbol*width)


def notefunction1() :
    a = cwd()

    try :
        raise Exception('This is the hmm error')  #Python will skip the error
    except :
        errorFile = open(a + '\\errorInfo.txt','w')

        errorFile.write(traceback.format_exc())

        errorFile.close
        print("The traceback info was written to errorInfo.txt ")
        space()

def notefunction2() :
    a = 1
    assert a == 1 ,'gg'
    print("which mean no error")
    a = 2
    assert a == 1,'gg'
    print("Ha gg ")

# Variables for notefunction3
market_street = {'ns':'green','ew':'red'}
mission_street = {'ns':'red','ew':'green'}
def notefunction3(stoplight) :
    # Changing the sequence of light from green to yellow and to red
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    # The program is fine, but there is a problem on the traffic
    # Ur traffic light never have red light !!!
    # So prevent this bug happen again in the future , use assert !!!!
    assert 'red' in stoplight.values(), 'Neither light is red !' + str(stoplight)
    print('Bug is clear !!!')

def notefunction4() :
    a = cwd()
    #logging.basicConfig(filename= a + '\\log.txt',level=logging.DEBUG,format = ' %(asctime)s -  %(levelname)s  -   %(message)s') # -> display on the txt  
    logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s -  %(levelname)s  -   %(message)s') #-> display on the terminal
    #logging.disable(logging.CRITICAL)  # disable the log message
    logging.debug('start of program')
    print(factorial(5))
    logging.debug("End of the program")

def  factorial(n) :
    logging.debug("Start of factorial(%s)" % (n))
    total = 1
    for i in range(1,n+1) :
        total *= i
        logging.debug('i is ' +str(i)+', total is ' + str(total))
    logging.debug("End of factorial(%s)" %(n))
    return total



import os

def space():
    print('')
def cwd() :
    print(os.getcwd())
    return os.getcwd()
def new_note(n):
    if n == '0' :
        print("Symbol ?\nWidth ?\nHeight ?")
        print("Or type 'try' to see the error")
        a = input()
        if a == 'try' :
            try :
                notefunction0('x',1,3)
            except Exception as err:
                print("An exception happend " + str(err))
        else :
            b = input()
            b = int(b)
            c = input()
            c =int(c)
            notefunction0(a,b,c)
    elif n == '1' :
         notefunction1()
    elif n == '2' :
         notefunction2()
    elif n == '3' :
         notefunction3(market_street)
         # Application of the assert for testing the bug
         # Make sure the program always have the red light
    elif n == '4' :
        notefunction4()
    elif n == 'cwd' :
        cwd()
#Loop
while True :
    print("What example you want me to show ?")
    num = input()
    new_note(num)