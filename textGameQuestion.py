class textGameQuestion:
    def __init__(self, question, possibleAnswers=["Yes", "No"], acceptance=3):
        self._q = question
        self._a = possibleAnswers

        for a in possibleAnswers:
            if acceptance & 1:
                self._a.append(a.lower())
            if acceptance & 2:
                self._a.append(a[0])
                if acceptance & 1:
                    self._a.append(a[0].lower())

    def returnQuestion(self):
        return(self._q)

    def checkAnswer(self, answer):
        return(bool(answer in self._a))
