from django.db import models

class Question(models.Model):
    """Model representing a question in the database.

    :param models.Model: The base class for all Django database models.
    :type models.Model: class
    :ivar question_text: The text of the question.
    :vartype question_text: CharField
    :ivar pub_date: The date and time when the question was published.
    :vartype pub_date: DateTimeField
    :return: A string representation of the question.
    :rtype: str
    """    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    """Model representing a choice for a question in the database.

    :param models.Model: The base class for all Django database models.
    :type models.Model: class
    :ivar question: The associated question for the choice.
    :vartype question: ForeignKey
    :ivar choice_text: The text of the choice.
    :vartype choice_text: CharField
    :ivar votes: The number of votes for the choice, default is 0.
    :vartype votes: IntegerField
    :return: A string representation of the choice.
    :rtype: str
    """    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
