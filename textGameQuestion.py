# Imports
from tgerrors import *

# Base Class
class textGameQuestion:
    def __init__(self, question, possibleAnswers={"Yes":True, "No":False}, acceptance=3):
        """ Create a text-based game question.

possibleAnswers is a dictionary of possible answers matching
up to what they mean.
acceptance is an integer defining whether or not to accept
certain cases using bitwise AND.

&1 means accept lowercase.
&2 means accept first letter.
"""
        self._q = question
        self._a = list(possibleAnswers.keys())
        self._a2 = list(possibleAnswers.values())
        self._a3 = {}

        for ans in possibleAnswers.keys():
            if acceptance & 1: # Case doesn't matter
                self._a.append(ans.lower())
                self._a2.append(possibleAnswers[ans])
                self._alower = True
            if acceptance & 2: # First letter works
                self._a.append(ans[0])
                self._a2.append(possibleAnswers[ans])
                if acceptance & 1: # Lowercase first letter
                    self._a.append(ans[0].lower())
                    self._a2.append(possibleAnswers[ans])

        for n in range(0, len(self._a)):
            self._a3[self._a[n]] = self._a2[n]

    def returnQuestion(self):
        " Return the question to be asked. "
        return(self._q)

    def askQuestion(self):
        " Ask the question and return the output if the answer is valid. "
        a = input(self._q + "\n")
        if self.checkValidAnswer(a):
            return(self.checkAnswerOutput(a))
        else:
            raise InvalidAnswerError("Answer was invalid.") # Catch the error and handle it your own way

    def checkValidAnswer(self, answer):
        " Check if an answer is valid. "
        if self._alower:
            try:
                return(bool(answer.lower() in self._a))
            except AttributeError:
                return(bool(answer in self._a))
        else:
            return(bool(answer in self._a))

    def checkAnswerOutput(self, answer):
        " Give the output to a given answer. "
        try:
            if self._alower:
                try:
                    return(self._a3[answer.lower()])
                except AttributeError:
                    return(self._a3[answer])
            else:
                return(self._a3[answer])
        except KeyError:
            raise InvalidAnswerError("Answer was invalid. Always check answer using checkValidAnswer(answer).")

# Pre-made answer classes
class textGameYesNo(textGameQuestion):
    def __init__(self, question, acceptance=3):
        " Create a true or false text-based game question. For more info see textGameQuestion. "
        textGameQuestion.__init__(self, question, {'Yes':True, 'No':False}, acceptance)

class textGameNumbers(textGameQuestion):
    def __init__(self, question, minnum, maxnum, acceptance=3):
        " Create a text-based question with answers between two numbers accepted. For more info see textGameQuestion. "
        adict = {}
        for x in range(minnum, maxnum+1):
            adict[str(x)] = x
        textGameQuestion.__init__(self, question, adict, acceptance)
