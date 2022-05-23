#Connecting to the database and displaying past player results
import mysql.connector
def score():
    print("\n\t\t\t\tPast Player Scores\n")
    print("Name\t\tCorrect Answers\t\tTotal Questions\t\tPercentage(%)")
    conDict={'host':'localhost',
             'database':'python math game',
             'user':'root',
             'password':''}
    db=mysql.connector.connect(**conDict)
    cursor=db.cursor()
    cursor.execute("SELECT * FROM score")
    data=cursor.fetchall()
    for item in data:
        print("\r")
        for r in item:
            print(r,end="\t\t\t")
        