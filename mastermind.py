import random 



def run_game():
    list_number =[]
    while len(list_number) != 4:
        n = int(random.randint(1,8))
        if n not in list_number:
            list_number.append(n)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.") 

   

   #Step 2
    lives = 12
    while lives > 0:
        new_list =[]
        correct = 0
        incorrect = 0
         
        guess_1 = input("Input 4 digit code: ")

        
        if len(guess_1) ==4 and guess_1.isdigit() and "0" not in guess_1 and "9" not in guess_1:
            correct = 0
            incorrect = 0
            for x in guess_1:
                new_list.append(int(x)) #creates a new list from the str
            for i in range(len(list_number)): #to check length which is 4
                if new_list[i] in list_number and list_number[i] == new_list[i]:#check if the each number is in the generated code and in the same position with the number in the
                    correct +=1
                elif new_list[i] in list_number and list_number[i] !=new_list[i]:
                    incorrect +=1
            print("Number of correct digits in correct place:    ",str(correct))
            print("Number of correct digits not in correct place:",str(incorrect))
            if new_list == list_number:
                print("Congratulations! You are a codebreaker!")
                code = list(map(str,new_list))
                random_number = "".join(code)
                print("The code was: "+str(random_number)) 
                break
            else:
                lives -=1
                print(f"Turns left: {lives}")

            if lives==0:
                code = list(map(str,list_number))
                random_number = "".join(code)
                print("The code was: "+str(random_number))
                

        else:
            print("Please enter exactly 4 digits.") 
            
    


if __name__ == "__main__":
    run_game()