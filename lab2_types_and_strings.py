#course: Object-oriented programming, year 2, semester 1
#academic year: 201920
#author: B. Schoen-Phelan
#date: 29-09-2019
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    #def play_with_strings(self):
        # working with strings
        # message = ("he said \"that\'s fantastic!\"")
        # print("Originally entered: "+ message)
        #
        # # print only first and last of the sentence
        # print(message[0] + message[6])
        #
        # # use slice notation
        # print(message[:4])
        # print(message[:2])
        # print(message[3:4])
        # print(message[0:7])
        #
        #
        # # escaping a character
        #
        #
        # # find all a's in the input word and count how many there are
        # x = message.count("a")
        # x=str(x)
        # print(x)
        #
        # print(len(message))
        #
        #
        # # replace all occurences of the character a with the - sign
        # # try this first by assignment of a location in a string and
        # # observe what happens, then use replace()
        # # message[4] = "-"
        # # print(message)..str object does not support item assignment
        #
        # q = message.replace("a","-")
        # print(q)
        #
        #
        # # printing only characters at even index positions
        # p=range(1, 5, 1)
        # for i in p:
        #     print(i)
        #
        # s = input("Enter your noun:")
        # print("Originally entered: " + s)
        #
        # for q in range(0, 10, 2):
        #     print("Index[" + str(q) + "] " +s[q])
    def play_with_lists(self):
          message = input("Please enter a whole sentence: ")
          print("Originally entered: "+ message)

        # hand the input string to a list and print it out
          x = message.split()
          print(x)
          print(x[1])

        # append a new element to the list and print
          x.append("potato")
          print(x)

    # remove from the list in 3 ways

        # del x[:2] deletes everything before 2 and not 2
        # del x[2:] deletes everything after 2 and 2
        # del x[2]

        #  y = x.pop(2) popping here puts the popped item into y and removes it from x and finds it by index notation
        #  print(y)
        #  print(x)

          # x.remove("i") removes word from list by typing in what u want to get rid of
          # print(x)      it only removes the first instance of the itm
          # x.remove("a") if its not in the list there will be a valueerror in the program
          # print(x)
        # check if the word cake is in your input list
          if "cake" in x:
              print("cake")
          else:
                print("no")

        # reverse the items in the list and print
        #   x.reverse()
        #   print(x)

        # reverse the list with the slicing trick
        # y = x[::-1]
        # print(y)

        # print the list 3 times by using multiplication
          print(x*3)


tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()