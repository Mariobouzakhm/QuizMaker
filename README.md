# QuizMaker
Two Scripts that allow a user to create short randomly generator quizzes.

The first script: QuestionsMaker.py is used to create the questions sheet.
This question sheet contains all the questions that are going to be in the quizzes with their respective right and wrong answers. 
(The correct answer is always stored in the A slot)
The questions are stored in a .txt file.
For help on how to use the script, enter the command help when the program starts.

The second script: QuestionsGenerator.py is where all the magic happen.
User will be prompted to enter the number of quizzes to genearator.
Each quiz will be generated with a random order of questions and answers for the questions.
With every quiz that is created, an answer key is generator for the specific quiz.
The quiz are stored in a .txt file with the name quiz_(number).txt
The answer key for each quiz is also stored in a .txt file with the name quiz_answers_(number).txt
