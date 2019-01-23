#! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

#Here is what the program does:
#1) Creates 35 different quizzes.

#2) Creates 50 multiple-choice questions for each quiz, in random order.

#3)Provides the correct answer and three random wrong answers for each question, in random order.

#4) Writes the quizzes to 35 text files.

#4) Writes the answer keys to 35 text files.

import random

capitals = {'Alabama': 'Montgomery', 'Alaska':'Juneau' , 'Arizona':'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
           'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
           'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
           'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
           'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
           'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
           'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
           'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
           'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
           'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
           'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
           'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
           'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
           'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
           'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


#creating 35 quiz and answer key files
for quiz_num in range(35):
    quizFile = open('quiz no {}'.format(quiz_num+1), 'w') #.............
    answerFile = open('answer file no {}'.format(quiz_num+1),'w')


    #Write out the header of the quiz
    quizFile.write('State capital quiz. number {}'.format(quiz_num+1))
    quizFile.write('Name : \n Date : \n')
    quizFile.write('\n\n')


    #shuffle the order of the states
    states = list(capitals.keys()) #get all the states in the list
    random.shuffle(states)   # randomize the order of the states

    #loop through all 50 states, making a question for each
    for question_num in range(50):

        #Get right and wrong answers
        correctanswer = capitals[states[question_num]]
        wronganswer = list(capitals.values())
        del wronganswer[wronganswer.index(correctanswer)] # removes the right answer from the list
        wronganswer = random.sample(wronganswer,3) # pick 3 wrong answers from the list

        answer_options = wronganswer + [correctanswer]
        random.shuffle(answer_options) # randomly shuffle the answer options

        #write the quetsion and answer options to the file
        quizFile.write(" Q.no {} - What is the capital of {}?\n".format(question_num+1, states[question_num]))
        for i in range(4):
            quizFile.write("{}.{}\n".format('ABCD'[i],answer_options[i]))
        quizFile.write('\n')

        #write out the answer key to a file :
        answerFile.write('{}.{}'.format((question_num+1), answer_options.index(correctanswer)))
    quizFile.close()
    answerFile.close()
