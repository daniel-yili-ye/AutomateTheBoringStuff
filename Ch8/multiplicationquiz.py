"""
To see how much PyInputPlus is doing for you, try re-creating the multiplication quiz project on your own without importing it.
This program will prompt the user with 10 multiplication questions, ranging from 0 × 0 to 9 × 9. You’ll need to implement the 
following features:

If the user enters the correct answer, the program displays “Correct!” for 1 second and moves on to the next question.
The user gets three tries to enter the correct answer before the program moves on to the next question.
Eight seconds after first displaying the question, the question is marked as incorrect even if the user enters the 
correct answer after the 8-second limit.
"""

import random
import time

def multiplication_test():
    mark = 0
    for i in range(1,11):
        x = random.randint(0,9)
        y = random.randint(0,9)
        answer = (x*y)
        print (str(i) + '. ' + str(x) + ' x ' + str(y))
        counter = 0
        start_time = time.time()
        while True:
            if counter < 3:
                try:
                    response = int(input('answer: '))
                except:
                    if (time.time() - start_time) < 8:
                        print ('sorry i did not understand that please try again: ')
                        counter += 1
                        continue
                    else:
                        print ('looks like you took ' + str(int((time.time() - start_time) - 8)) + ' extra seconds to answer. let\'s move onto the next question...')
                        break
                if response == answer:
                    if (time.time() - start_time) < 8:
                        mark += 1
                        print ('Correct! Answered in ' + str(int(time.time() - start_time)) + ' seconds.')
                        time.sleep(1)
                        break
                    else:
                        print ('Although you were correct, it looks like you took ' + str(int((time.time() - start_time) - 8)) + ' extra seconds to answer. let\'s move onto the next question...')
                        break
                else:
                    if (time.time() - start_time) < 8:
                        counter += 1
                        continue
                    else:
                        print ('looks like you took ' + str(int((time.time() - start_time) - 8)) + ' extra seconds to answer. let\'s move onto the next question...')
                        break
            else:
                print ('looks like you used up all your tries. let\'s move onto the next question...')
                break
    print ('Your final mark: ' + str(mark))

multiplication_test()