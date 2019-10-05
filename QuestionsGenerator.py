import os, random, re
os.chdir('C:\\Users\\K\\PythonScripts\\Coursera\\Extra\\QuizMaker')

#Dictionnary that contains the questions as key and the answers in a list as a value with the first one being the answers
questions = dict()

#File IOWrapper Used to read the file
file = open('Questions.txt', 'r')

#Regular Expressions that differentiate between the questions and the answers
regex = re.compile(r'[0-9]{1}\. (.*)') #Matches a question

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

number = None
while True:
    try:
        number = int(input('Enter the number of quizzes you want to generate: '))
        break
    except:
        print("Invalid Number. Please enter an integer")


for i in range(number):
    #Creating the two files for the quiz and the answer key
    quiz = open('quiz_%d.txt' % (i + 1), 'w')
    answer = open('quiz_answers_%d.txt' % (i + 1), 'w')

    #Create the headers for the quizzes
    quiz.write('Name:\nDate:\nQuiz no.%d\n\n' % (i + 1))
    answer.write('Answer Key for Quiz no.%d\n\n' % (i + 1))

    keys = list(questions.keys())
    random.shuffle(keys)

    for j in range(len(keys)):
        dic = questions[keys[j]]
        for quest, anws in list(dic.items()):
            correct_a = anws[0]
            random.shuffle(anws)
            correctLetter = 'ABCD'[anws.index(correct_a)]

            quiz.write('%d. %s\n' % (j + 1, quest))

            for k in range(len(anws)):
                quiz.write((' ' * 3) + '%s. %s\n' % ('ABCD'[k], anws[k]))
            quiz.write('\n')
            answer.write('%d. %s\n' % (j + 1, correctLetter))

    #Close the file handles
    quiz.close()
    answer.close()
