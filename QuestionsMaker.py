import os, re

#Set the current working directory
os.chdir('C:\\Users\\K\\PythonScripts\\Coursera\\Extra\\QuizMaker')

#Regular Expressions that differentiate between the questions and the answers
regex = re.compile(r'[0-9]{1}\. (.*)') #Matches a question

#File IOWrapper Used to read the file
file = open('Questions.txt', 'r')

#Dictionnary to store the Questions
questions = dict()

#Section of code that read through the file and store the questions and the answers in a dictionnary
lines = file.readlines()
for i in range(len(lines)):
    match = regex.search(lines[i])
    if match is not None:
        question = lines[i][lines[i].find('.')+2:].strip()
        a1 = lines[i+1][lines[i+1].find('.')+2:].strip()
        a2= lines[i+2][lines[i+2].find('.')+2:].strip()
        a3 = lines[i+3][lines[i+3].find('.')+2:].strip()
        a4 = lines[i+4][lines[i+4].find('.')+2:].strip()

        questions[len(questions) + 1] = {question:[a1, a2, a3, a4]}

#Close the file to be able to write to it later
file.close()

#Section of code that prompts allow the user to modify the questions
while True:
    usage = ''' - Usage:
    1- New - To add new questions
    2- List - To list the current registered questions
    3- Done - To exit the question question maker
    4- Usage - To print this message
      '''
    choice = input('Enter the command corresponding to the action you want to perform: ')
    if choice.lower() == 'new':
        question = input('Enter the question you want to add: ')
        a1 = input('Enter the correct answer to the question: ')
        a2 = input('Enter the first wrong answer: ')
        a3 = input('Enter the second wrong answer: ')
        a4 = input('Enter the third wrong answer: ')

        questions[len(questions) + 1] = {question:[a1, a2, a3, a4]}
        print('Question Added !')
    elif choice.lower() == 'list':
        if len(questions.keys()) == 0:
            print('No Questions Found.')
        else:
            print(questions)
    elif choice.lower() == 'done':
        print('Exiting Question Maker.')
        break
    elif choice.lower() == 'usage':
        print(usage)
    else:
        print(usage)

#Reopen the file in write mode to modify the files
file = open('Questions.txt', 'w')

#Section that write the questions to the file.
for key, dic in list(questions.items()):
    for quest, anws in list(dic.items()):
        file.write('%d. %s\n' % (key, quest))
        for i in range(len(anws)):
            file.write('%s. %s\n' % ('ABCD'[i], anws[i]))

#Close the file after writting the Questions
file.close()
