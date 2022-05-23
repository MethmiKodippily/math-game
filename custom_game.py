#Refference:https://stackoverflow.com/questions/26260950/how-can-i-randomly-choose-a-maths-operator-and-ask-recurring-maths-questions-wit?answertab=votes#tab-top
#Refference:https://www.programiz.com/python-programming/methods/built-in/eval
import random
import mysql.connector

def customGame():
    user_name = input("Enter your name: ")  #get user name
    difficulty_level = str(input("Enter difficulty level(easy/medium/hard): "))  #get difficulty level
    number_of_questions = int(input("Enter number of questions: ")) #get number of questinons
    
    if(difficulty_level != "easy" and difficulty_level != "medium" and difficulty_level != "hard") :
        print("Invalid difficulty level, try again..")
        
    if(difficulty_level == "easy"):
        easy(user_name,difficulty_level,number_of_questions)  
    if(difficulty_level == "medium"): 
        medium(user_name,difficulty_level,number_of_questions)  
    if(difficulty_level == "hard"):
        hard(user_name,difficulty_level,number_of_questions)  
    
        
        
#0-10 and +
def easy(name,difficulty,num_questions):
    correct_answers = []    #list to hold correct answer output string
    incorrect_anwers = []   #list to hold incorrect answer output string
    for i in range (num_questions): 
        
        #generate two random numbers
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
        
        #get users answer
        answer = input(str(num1) + " + " + str(num2) + " = " ) #have to convert num1, num2 to str
        
        #calculate correct value
        sum = num1+num2
        
        if(int(answer) == int(sum)):
            correct_answers.append(str(num1) + " + " + str(num2) + " = " + str(sum) + "(answer = " + str(sum) + ")" + "[corect]")
        else:
            incorrect_anwers.append(str(num1) + " + " + str(num2) + " = " + str(answer) + "(answer = " + str(sum) + ")" + "[Incorect]")
            
    #output results
    print("Game results")
    print("------------")
    print("Your name is " + name) 
    print("Your difficulty level :" + difficulty)
    print("You answered " + str(num_questions) + "questions")
    
    
    
    for i in range(len(correct_answers)):
        print(correct_answers[i])
    for i in range(len(incorrect_anwers)):
        print(incorrect_anwers[i])
    
    #calculating the percentage
    percentage=len(correct_answers)/num_questions*100
     
    # display results
    print("Number of Questions: ",num_questions)
    print("Correct Answers: ",len(correct_answers))
    print("Percentage: ",percentage,"%")
    
    #connecting to the database 
    conDict={'host':'localhost',
             'database':'python math game',
             'user':'root',
             'password':''}
    db=mysql.connector.connect(**conDict)
    cursor=db.cursor()
    mySQLText="INSERT INTO score (name,correct,totalQuestions,percentage) VALUES(%s,%s,%s,%s)"#ceating the query
    myValues=(name,len(correct_answers),num_questions,percentage)   
    cursor.execute(mySQLText, myValues)
    db.commit()
    db.close()
    
 
           

#0-50 and +,-
def medium(name,difficulty,num_questions):
     correct_answers = []    #list to hold correct answer output string
     incorrect_anwers = []   #list to hold incorrect answer output string
    
     operations_medium = ['+', '-']
     
     for i in range (num_questions): 
         #generate two random numbers
         num1 = random.randint(0,50)
         num2 = random.randint(0,50)
         
         #generate random operand
         op = random.choice(operations_medium)
         
         #get users answer
         answer = input(str(num1) + op + str(num2) + " = " ) #have to convert num1, num2 to str
         
          #calculate correct value
         correct_value = eval(str(num1) + op + str(num2))
         #correct_value = int(correct_value)
         
         if(int(answer) == int(correct_value)):
            correct_answers.append(str(num1) + op + str(num2) + " = " + str(correct_value) + "(answer = " + str(correct_value) + ")" + "[corect]")
         else:
            incorrect_anwers.append(str(num1) + op + str(num2) + " = " + str(answer) + "(answer = " + str(correct_value) + ")" + "[Incorect]")
            
     #output results
     print("Game results")
     print("------------")
     print("Your name is " + name) 
     print("Your difficulty level :" + difficulty)
     print("You answered " + str(num_questions) + "questions")
    
     for i in range(len(correct_answers)):
         print(correct_answers[i])
     for i in range(len(incorrect_anwers)):
         print(incorrect_anwers[i])
         
     #calculating the percentage
     percentage=len(correct_answers)/num_questions*100
     
     #display results
     print("Number of Questions: ",num_questions)
     print("Correct Answers: ",len(correct_answers))
     print("Percentage: ",percentage,"%")    
     
    #connecting to the database 
     conDict={'host':'localhost',
             'database':'python math game',
             'user':'root',
             'password':''}
     db=mysql.connector.connect(**conDict)
     cursor=db.cursor()
     mySQLText="INSERT INTO score (name,correct,totalQuestions,percentage) VALUES(%s,%s,%s,%s)"#creating the query
     myValues=(name,len(correct_answers),num_questions,percentage)     
     cursor.execute(mySQLText, myValues)
     db.commit()
     db.close()
         
#0-100 and +,-,*    
def hard(name,difficulty,number_questions):
    correct_answers = []  #list to hold correct answer output string
    incorrect_answers = [] #list to hold incorrect answer output string
    
    operations_hard = ['+', '-', '*']
    
    for i in range (number_questions): 
         #generate two random numbers
         num1 = random.randint(0,100)
         num2 = random.randint(0,100)
         
         #generate random operand
         op = random.choice(operations_hard)
         
         #get users answer
         answer = input(str(num1) + op + str(num2) + " = " ) #have to convert num1, num2 to str
         
         #calculate correct value
         correct_value = eval(str(num1) + op + str(num2))
         
         #correct_value = int(correct_value)
        
         if(int(answer) == int(correct_value)):
            correct_answers.append(str(num1) + op + str(num2) + " = " + str(correct_value) + "(answer = " + str(correct_value) + ")" + "[corect]")
         else:
            incorrect_answers.append(str(num1) + op + str(num2) + " = " + str(answer) + "(answer = " + str(correct_value) + ")" + "[Incorect]")
     #output results
    print("Game results")
    print("------------")
    print("Your name is " + name) 
    print("Your difficulty level :" + difficulty)
    print("You answered " + str(number_questions) + "questions")
    
    for i in range(len(correct_answers)):
         print(correct_answers[i])
    for i in range(len(incorrect_answers)):
         print(incorrect_answers[i])  
    #calculating the percentage
    percentage=len(correct_answers)/number_questions*100
     
    # display results
    print("Number of Questions: ",number_questions)
    print("Correct Answers: ",len(correct_answers))
    print("Percentage: ",percentage,"%")

    #connecting to the database 
    conDict={'host':'localhost',
             'database':'python math game',
             'user':'root',
             'password':''}
    db=mysql.connector.connect(**conDict)
    cursor=db.cursor()
    mySQLText="INSERT INTO score (name,correct,totalQuestions,percentage) VALUES(%s,%s,%s,%s)"#creating the query
    myValues=(name,len(correct_answers),number_questions,percentage)   
    cursor.execute(mySQLText, myValues)
    db.commit()
    db.close()