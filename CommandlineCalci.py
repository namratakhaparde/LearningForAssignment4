import sys
def userinputs(typedata, input_count=None):
    data=list()
    choice='Y'
    while True:
        input=raw_input("""\nPlease enter the input values
Enter N/n when done with inputs
Enter X/x to go back to the main menu\n\n>>""")
        choice= input
        if choice not in ["n","N","X","x"]:
            #data.append(input)
            try:
                conversion= typedata(input)
                data.append(conversion)
                if len(data) == input_count:
                    break
            except Exception as E:
                print("\nInvalid input %s, Operation can not be performed" %(input))
                print ("Please enter integer values!\n\n")
        elif choice in ["X","x"]:
            return None  
        elif choice in ["n", "N"]:
            if len(data)< 2:
                print('\nPlease enter at least 2 inputs\n')
                continue      
            break
    return data

# def validateinput(typedata,userlist):
#     finaluserlist=[]
#     for each in userlist:
#         try:
#             conversion= typedata(each)
#             finaluserlist.append(conversion)
#         except Exception as E:
#             print("Invalid input %s, Expecting %s" %(each,str(typedata)))
#             print ("Operation cannot be performed!")
#             return None
#     return finaluserlist


def summation():
    
    #print userlist
    while True:
        #validateinput(int,userlist)
        final_list= userinputs(int)
        if final_list is None:
            return
        else:
            print("\nYour entered inputs are:")
            print final_list
            add=0
            for each in final_list:
                add=each+add
            print("\nYour addition is   %s\n\n" %add)
            break

        # else:
            
        #     choice= raw_input('Press 1 to enter inputs or Press 0 to go back to the main menu')
        #     while not choice or choice not in ['1','0']:
        #         print('Please enter either 1 or 0')
        #         choice= raw_input('Press 1 to enter inputs or Press 0 to go back to the main menu')
                
        #     if choice =='1':
        #         print ("Please reenter your inputs")
        #         continue    
        
        #     elif choice =='0':
        #         break
        


def subtraction():
    while True:
        final_list= userinputs(int)
        if final_list is None:
            return
        else:
            print("\nYour entered inputs are:")
            print final_list
            subtract=final_list[0]
            for each in final_list[1:]:
                subtract=subtract-each
            print("\nThe subtraction is   %s\n\n" %subtract)
            break
       

def multiplication():
    while True:
        final_list= userinputs(int)
        if final_list is None:
            return
        else:
            print("\nYour entered inputs are:")
            print final_list
            product=1
            for each in final_list:
                product=product*each
            print("\nThe multiplication is   %s\n\n" %product)
            break


def division():
    while True:
        final_list=userinputs(int,2)
        if final_list is None:
            return
        else:
            print("\nYour entered inputs are:")
            print final_list
            if final_list[1] ==0:
                print ('\n0 cannot be denominator for division')
                break
            else:
                quotient=final_list[0]
                for each in final_list[1:]:
                    quotient=quotient/each
                    remainder= final_list[0]%each
                print("\nThe quotient is   %s" %quotient)
                print ("\nThe remainder is  %s" %remainder)
                break

def minimum():
    while True:
        final_list=userinputs(int)
        minimum= final_list[0]
        if final_list is None:
            return
        else:
            for each in final_list[1:]:
                if each<=minimum:
                    minimum=each
            print ("\nThe minimum element is   %s" %minimum)
            break


def maximum():
    while True:
        final_list=userinputs(int)
        maximum= final_list[0]
        if final_list is None:
            return
        else:
            for each in final_list[1:]:
                if each>=maximum:
                    maximum= each
            print('\nThe maximum element is   %s' %maximum)
            break


def main():
    while True:
        option= raw_input("""\nEnter your option:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Minimum Value
6. Maximum Value
7. Exit\n\n>>""")
        #print "The option you have selected is  ",option
        #if option not None and option != ''
        if not option or option not in ['1',"2","3","4","5","6","7"]:
            print "Please enter valid input"
        elif option == '1':
            summation()
        elif option == '2':
            subtraction()
        elif option == '3':
            multiplication()
        elif option =='4':
            division()
        elif option == '5':
            minimum()
        elif option == '6':
            maximum()
        elif option =='7':
            sys.exit()

main()
