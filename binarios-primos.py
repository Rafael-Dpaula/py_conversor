
import datetime
import os
import sys
sys.set_int_max_str_digits(2100000000)
current_size = sys.get_int_max_str_digits()
#print(current_size)



def clearConsole():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')


def estimated_time(time, P, val):
    initTime = datetime.datetime.time(time)
    #print(f'---------the init time is: ->{initTime}')
    if(int(datetime.datetime.now().strftime("%M")) > int(initTime.strftime("%M"))):
        min_passed = (int(datetime.datetime.now().strftime("%M")) - int(initTime.strftime("%M")))
    else:
        min_passed = (int(initTime.strftime("%M")) - int(datetime.datetime.now().strftime("%M")))
    if(int(datetime.datetime.now().strftime("%H")) > int(initTime.strftime("%H"))):
        hour_passed = (int(datetime.datetime.now().strftime("%H")) - int(initTime.strftime("%H")))
    else:
        hour_passed = (int(initTime.strftime("%H")) - int(datetime.datetime.now().strftime("%H")))
    if(int(datetime.datetime.now().strftime("%S")) > int(initTime.strftime("%S"))):
        sec_passed = (int(datetime.datetime.now().strftime("%S")) - int(initTime.strftime("%S")))
    else:
        sec_passed = (int(initTime.strftime("%S")) - int(datetime.datetime.now().strftime("%S")))
    if(int(datetime.datetime.now().strftime("%f")) > int(initTime.strftime("%f"))):
        milisec_passed = (int(datetime.datetime.now().strftime("%f")) - int(initTime.strftime("%f")))
    else:
        milisec_passed = (int(initTime.strftime("%f")) - int(datetime.datetime.now().strftime("%f")))

    #sectime = ((hour_passed * 3600) + (min_passed * 60) + sec_passed)
    #print(f'------------hour passed is: ->{hour_passed}', f'min passed is: ->{min_passed}', f'sec passed is: ->{sec_passed}')
    
    rest = (val - P)
    
    #estimated = ((int(rest) * int(sectime) // int(P)))
    
    estimated_min = ((int(rest) * int(min_passed) // int(P)))
    estimated_hour = ((int(rest) * int(hour_passed) // int(P)))
    estimated_sec = ((int(rest) * int(sec_passed) // int(P)))
    estimated_milisec = ((int(rest) * int(milisec_passed) // int(P)))
    
    if(estimated_sec % 60 >= 1):
        estimated_min = estimated_min + (estimated_sec // 60)
        estimated_sec = estimated_sec % 60
    elif(estimated_min % 60 >= 1):
        estimated_hour = estimated_hour + (estimated_min // 60)
        estimated_min = estimated_min % 60
    elif(estimated_milisec % 1000 >= 1):
        estimated_sec = estimated_sec + (estimated_milisec // 1000)
        estimated_milisec = estimated_milisec % 1000
    
    
    if(estimated_hour <= 10):
        estimated_hour = int(f'0{estimated_hour}')
    elif(estimated_min <= 10):
        estimated_min = int(f'0{estimated_min}')
    elif(estimated_sec <= 10):
        estimated_sec = int(f'0{estimated_sec}')
    elif(estimated_milisec <= 10):
        estimated_milisec = int(f'0{estimated_milisec}')
    
    time_estimated = (f'{estimated_hour}h:{estimated_min}m:{estimated_sec}.{estimated_milisec}s')
    
    #print(f'------------rest is: ->{rest}')#, f'sectime is: ->{sectime}')
    print(f'The estimated time is: {time_estimated}')
    #print(f'The estimated time is: {(estimated // 3600)}:{(estimated // 60)}:{estimated}')
    
    
    
    
def binary(): #calculate the binary number of the typed by user.
    binNum = ''
    val = int(input('Number for conversion: -> '))
    result = int(val)
    
    initime = datetime.datetime.now()
    if(str(val).isdigit()):
        if (val > 1):
            print('processing........')
            while (result != 1):
                binNum = binNum + str((result % 2))
                if (result // 2 == 1):
                    binNum = binNum + str((result // 2))
                    #print('test1 -> ' + str(result))
                    break
                else: 
                    result = result // 2
                    #print('test2 -> ' + str(result))
            print('converted value is: -> ' + str(binNum[::-1]))
            endtime = datetime.datetime.now()
            print(f'Time taken: {endtime - initime}')
            program_selection()
        elif (val == 0): 
            print('processing........')
            binNum = '0'
            print('converted value is: -> ' + binNum[::-1])
        elif (val == 1):
            print('processing........')
            binNum = '1'
            print('converted value is: -> ' + binNum[::-1])
    else: 
        print('Input invalid.')
    #end function
    
def simpleprime():
    val = int(input('Number to compare if is prime: -> '))
    initime = datetime.datetime.now()
    tenP = (val * (10/100))
    sevenP = (val * (70/100))
    fiveP = (val * (50/100))
    threeP = (val * (30/100))
    if(str(val).isdigit()):
        for n in range(1, int(val) + 1):
            ##print (n)
            if(n == 1):
                print('starting the processing..')
            elif(n == int(tenP)):
                print('processing... 10%')
                estimated_time(initime, tenP, val)
            elif(n == int(threeP)):
                print('processing...... 30%')
                estimated_time(initime, threeP, val)
            elif(n == int(fiveP)):
                print('processing......... 50%')
                estimated_time(initime, fiveP, val)
            elif(n == int(sevenP)):
                print('processing almost done.......... 70%')
                estimated_time(initime, sevenP, val)
            if(n == int(val)):
                ##print('test1 pass')
                if(val % n == 0 and val % 1 == 0):
                    print(f"The value {val} selected is Prime.")
                    endtime = datetime.datetime.now()
                    print(f'Time taken: {endtime - initime}')
                    break
            elif(val % n == 0 and n != 1):
                print(f"The value {val} selected i'snt Prime.")
                endtime = datetime.datetime.now()
                print(f'Time taken: {endtime - initime}')
                break
    else:
        print('invalid input')
        simpleprime()

def marsenne_prime():
    valE = int(input('Number to search if is a mersenne prime: -> '))
    #print(valE)
    valT = (2**(int(valE))-1)
    print(f"The total is: -> {valT}")
    tenP = (valT * (10/100))
    sevenP = (valT * (70/100))
    fiveP = (valT * (50/100))
    threeP = (valT * (30/100))
    initime = datetime.datetime.now()
    if(str(valE).isdigit()):
        for n in range(1, int(valT) + 1):
            #print (n)
            if(n == 1):
                print('starting the processing..')
            elif(n == int(tenP)):
                print('processing... 10%')
                estimated_time(initime, tenP, valT)
            elif(n == int(threeP)):
                print('processing...... 30%')
                estimated_time(initime, threeP, valT)
            elif(n == int(fiveP)):
                print('processing......... 50%')
                estimated_time(initime, fiveP, valT)
            elif(n == int(sevenP)):
                print('processing almost done.......... 70%')
                estimated_time(initime, sevenP, valT)
            if(n == int(valT)):
                ##print('test1 pass')
                if(valT % n == 0):
                    print(f"The value 2^({valE} - 1) selected is Prime.")
                    endtime = datetime.datetime.now()
                    print(f'Time taken: {endtime - initime}')
                    break
            elif(valT % n == 0 and n != 1):
                print(f"The value 2^{valE} selected i'snt Prime.")
                endtime = datetime.datetime.now()
                print(f'Time taken: {endtime - initime}')
                break

def prime_select():
    print('Chose what kind of number you want to test:')
    print('1. Simple prime')
    print('2. Marsenne prime')
    print('3. Return to program selection')
    print('4. Exit')
    selection = input('-->  ')
    
    if(selection == '1'):
        #clearConsole()
        print('Simple primes selected sucessfully')
        simpleprime()
    elif(selection == '2'):
        #clearConsole()
        print('Mersenne primes selected sucessfully')
        marsenne_prime()
    elif(selection == '3'):
        #clearConsole()
        print('Return to selection')
        program_selection()
    elif(selection == '4'):
        #clearConsole()
        print('Program exited sucessfully')
        return
    else:
        #clearConsole()
        print('Invalid selection. Please try again.')
        prime_select()

#Program selection
def program_selection():
    print('Choose a program:')
    print('1. Binary Calculator')
    print('2. Prime numbers')
    print('3. Exit')
    selection = input('-->  ')
    
    if(selection == '1'):
        #clearConsole()
        print('Binary Calculator selected sucessfully')
        binary()
    elif(selection == '2'):
        #clearConsole()
        print('Prime numbers selected sucessfully')
        prime_select()
    elif(selection == '3'):
        #clearConsole()
        print('Program exited')
        return
    else:
        #clearConsole()
        print('Invalid selection. Please try again.')
        program_selection()
    ##end program selection function
program_selection()