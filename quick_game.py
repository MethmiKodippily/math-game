import random
import mysql.connector
correct_answers = []    #list to hold correct answer output string
incorrect_anwers = []   #list to hold incorrect answer output string

def quickGame():
    
    user_name = input("Enter your name: ") #get users name
    
    for i in range (5): #loop 5 times
        
        #generate two random numbers
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
        
        #get users answer
        answer = input(str(num1) + " + " +str(num2) + " = " ) #have to convert num1, num2 to str
        
        #calculate correct value
        sum = num1+num2
        
        if(int(answer) == int(sum)):
            correct_answers.append(str(num1) + " + " + str(num2) + " =" + str(sum) + "(answer = " + str(sum) + ")" + "[corect]")
        else:
            incorrect_anwers.append(str(num1) + " + " + str(num2) + " =" + str(answer) + "(answer = " + str(sum) + ")" + "[Incorect]")

    
      
    #output results
    for i in range(len(correct_answers)):
        print(correct_answers[i])
    for i in range(len(incorrect_anwers)):
        print(incorrect_anwers[i])
     #calculating the percentage
    percentage=len(correct_answers)/5*100
     
    # display results
    print("Number of Questions: 5 ")
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
    myValues=(user_name,len(correct_answers),"5",percentage)   
    cursor.execute(mySQLText, myValues)
    db.commit()
    db.close()
    
