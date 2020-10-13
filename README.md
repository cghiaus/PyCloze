# PyCloze

- author: [Christian Ghiaus](mailto:cghiaus@gmail.com)
- institution: [INSA Lyon](https://www.insa-lyon.fr), France
- date: 2020

**PyCloze** is a procedure to obtain questions with embedded answers ([cloze][cloze]) for [Moodle][Moodle] learning management system. It needs basic knowledge of [Python 3](https://www.python.org) and [Moodle 3](https://docs.moodle.org/39/en/Main_page), and editting rights in Moodle. 

**MoodleCloze** is a Python module for creating embedded answers ([cloze][cloze]) questions for [Moodle](https://moodle.org/?lang=en) in [.xml format](https://docs.moodle.org/39/en/Moodle_XML_format). The [penalty factor][penalty] is fixed to 1/3 (but you can change it).

The procedure allows us to generate a set of questions from which one will be [randomly assigned][random_q] by Moodle to a student. The problem is the same for all questions, but the input data and the responses are different from question to question. Therefore, the procedure is suited for exams and evaluations.

Moodle random questions can be used for quizzes of:
- 10 min. during lectures (especially video lectures) to check the comprehension of concepts;
- 1 hour during seminaries to see the capacity of students to solve their own problem;
- 2 hours for final exams.

## Licence
Code is released under [MIT Lincence](https://choosealicense.com/licenses/mit/).

Docs are released under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

[![Creative Commons License](http://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
[![MIT](https://www.nicepng.com/ourpic/u2t4t4e6w7w7a9a9_license-icon-mit-open-source-license-logo/)

## Quick start
[Import][Import_questions] one of the `PyCloze__.xml` files in Moodle to see cloze questions. See [Tutorial_xml2moodle.md](Tutorial_xml2moodle.md) for further details on how to create a quiz with [random questions][random_q].

## Installation

Copy the `MoodleCloze.py` file in the folder in which you develop the cloze question. 
`Import` the module `MoodleCloze` in your Python code.

## How to use it

Typical workflow:

In Moodle (see [Tutorial_xml2moodle.md](Tutorial_xml2moodle.md)):

1.	Create and set up a quiz.
2.	Create a category for the specific question of the quiz in the question bank.

In Python (see [Tutorial_py2xml.md](Tutorial_py2xml.md)):

3.	Create or modify the questions and save them in an `.xml` file.

In Moodle (see [Tutorial_xml2moodle.md](Tutorial_xml2moodle.md)):

4.	Import the `.xml `file into the question bank in the category of the quiz corresponding to the type of question.
5.	Preview the questions of a category in the question bank. If there are errors in the questions:
    - Delete the questions from the category.
    - Go to step 3.

    If there are no errors, go to the next step.
6.	Add a random question to the test.
7.	Preview the test.

## Contents
### Tutorials

[Tutorial_py2xml.md](Tutorial_py2xml.md): on how to generate cloze questions with **Python** and export them as `.xml` file.  `PyCloze00.py` is used as an walk through example.

[Tutorial_xml2moodle.md](Tutorial_xml2moodle.md): on how to set up a quiz and import `.xml` random questions in **Moodle**.

### Examples

#### Description
[Description4quizzes.md](Description4quizzes.md) presents three quizzes:

1. PyCloze00: given the names and the ages of three children, find the mean age, the eldest child and the longest name.
2. PyCloze01: find the thermal resistance, the heat flux and the heat transfer rate of a flat wall. 
3. PyCloze02: find the coefficient of heat exchange in forced and in natural convection.


#### Python implementation

`PyCloze00.py` a simple example with inputs of type string and numerical and outputs of type numerical, multichoice and short answers (discussed in [Tutorial_py2xml.md](Tutorial_py2xml.md)).

`PyCloze01.py` an example with numerical inputs and numerical outputs.

`PyCloze02.py` a more complicated example.

#### .xml files

`PyCloze00.xml` file generated with `PyCloze00.py`.

`PyCloze01.xml` file generated with `PyCloze01.py`.

`PyCloze02.xml` file generated with `PyCloze02.py`.


[cloze]:https://docs.moodle.org/39/en/Embedded_Answers_(Cloze)_question_type

[Import_questions]:https://docs.moodle.org/39/en/Import_questions#Importing_questions_from_an_existing_file

[Moodle]:https://moodle.org/?lang=en

[Tutorial_MarkDown]:https://agea.github.io/tutorial.md/

[random_q]:https://docs.moodle.org/39/en/Random_question_type

[penalty]:https://docs.moodle.org/39/en/Multiple_Choice_question_type#Penalty_factor
