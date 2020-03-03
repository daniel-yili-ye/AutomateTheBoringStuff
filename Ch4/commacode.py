def commacode(input):
        for x in range (len(input)):
                if input[-2] == input[x]:
                        print ((input[x]) + (", and "), end='')
                elif input[-1] == input[x]:
                        print (input[x])
                else:
                        print ((input[x]) + (", "), end='')

spam = ['apples', 'bananas', 'tofu', 'cats']

commacode(spam)