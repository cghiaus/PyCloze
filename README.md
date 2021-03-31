# PyCloze

[![DOI](https://zenodo.org/badge/302832801.svg)](https://zenodo.org/badge/latestdoi/302832801)

[Christian Ghiaus](mailto:cghiaus@gmail.com)

[INSA Lyon](https://www.insa-lyon.fr), France, 18/04/2021

**PyCloze** is a procedure to obtain a sort of [calculated][calculated_q] questions with embedded answers (called [cloze][cloze] questions) for [Moodle][Moodle] learning management system. It needs basic knowledge of [Python 3](https://www.python.org) and [Moodle 3](https://docs.moodle.org/39/en/Main_page). You need to have a [teacher role in Moodle](https://moodle.com/news/lets-edit-moodle-course-minutes/) to be able to turn editing on.

**MoodleCloze** is a Python module and a workflow for creating embedded answers ([cloze][cloze]) questions for [Moodle](https://moodle.org/?lang=en) in [.xml format](https://docs.moodle.org/39/en/Moodle_XML_format). The [penalty factor][penalty] is fixed to 1/3 (but you can change it in `MdlClz.py` file).

The workflow allows us to generate a set of questions from which one will be [randomly assigned][random_q] by Moodle to a student. The problem is the same for all questions, but the input data and the corresponding answeres are different from question to question. Therefore, the procedure is suited for exams and evaluations.

Moodle random questions can be used for quizzes of:
- < 10 min. during lectures to check the comprehension of concepts;
- 1 - 2 hours during seminaries to see the capacity of students to solve their own problem;
- 2 hours for final exams.

## Licence
Code is released under [MIT Lincence](https://choosealicense.com/licenses/mit/).

Docs are released under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

[![Creative Commons License](http://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)

## Differences between versions v.0.0.0 and v.0.1.0
To tell Python where to substitute the values of the variables in `text`  (of type string in `PyCloze__.py` or `PyClz__.py`), the function `generate_quiz`:

- from module `MoodleCloze.py` in v.0.0.0 uses the “old style” string formatting ([% operator](https://realpython.com/python-string-formatting/#1-old-style-string-formatting-operator)). 

- from module `MdlClz.py` in v.0.1.0 uses the “new style” string formating ([str.format](https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat)). 

In v.0.0.0, there is the section `# 3. Define the mapping between the variables of the problem`. This mapping is no more needed (and used) in v.0.1.0.  There are changes in the specification of the variables in `text` (string in `PyCloze00.py` and `PyClz00.py`):

|`text` |`PyCloze00.py` (v.0.0.0) | `PyClz00.py` (v.0.1.0)|
|-------|-------------------------|-----------------------|
|Text   |mean age is `$$\\mu$$`   |mean age is `$$\\mu$$` |
|Inputs |%(name_1)s, age %(age_1).1f|{name[0]:s}, age {age[0]:.1f}|
|Outputs|{1:NUMERICAL:=%(mean_age)3.1f:%(err_mean_age)3.2f} (±5 %%)| {{1:NUMERICAL:={mean_age:.1f}:0.5}} (±0.5)|
|       |{1:MULTICHOICE:%(oldest_1)s %(name_1)s|{{1:MULTICHOICE:{oldest[0]:s} {name[0]:s}|
|       |              ~%(oldest_2)s %(name_2)s|~{oldest[1]:s} {name[1]:s}|
|       |              ~%(oldest_3)s %(name_3)s}|~{oldest[2]:s} {name[2]:s}}}|
|       |{1:SHORTANSWER:~=%(longest_name)s}|{{1:SHORTANSWER:~={longest_name:s}}}|




## Quick start
[Import][Import_questions] one of the `PyClz__.xml` files in Moodle to see the cloze questions. See [Tutorial_xml2moodle.md](Tutorial_xml2moodle.md) for further details on how to create a quiz with [random questions][random_q].

## Installation

Copy the `MdlClz.py` file in the folder in which you develop the cloze question. 
`Import` the module `MdlClze` in your Python code.

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

[Tutorial_py2xml.md](Tutorial_py2xml.md): on how to generate cloze questions with **Python** and export them as `.xml` file.  `PyClz00.py` is used as a walk through example.

[Tutorial_xml2moodle.md](Tutorial_xml2moodle.md): on how to set up a quiz and import `.xml` random questions in **Moodle**.

[Tips&Tricks.md](Tips&Tricks.md): on useful advices and avoidable pitfalls.

### Examples

#### Description
[Description4quizzes.md](Description4quizzes.md) presents three quizzes:

1. PyClz00: given the names and the ages of three children, find the mean age, the eldest child and the longest name.
2. PyClz01: find the thermal resistance, the heat flux and the heat transfer rate of a flat wall. 
3. PyClz02: find the coefficient of heat exchange in forced and in natural convection.


#### Python implementation

`PyClz00.py` a simple example with inputs of type string and numerical, and outputs of type numerical, multichoice and short answers (discussed in [Tutorial_py2xml.md](Tutorial_py2xml.md)).

`PyClz01.py` a typical example with numerical inputs and outputs. It uses [Unicode](https://docs.moodle.org/23/en/Unicode) characters and [LaTex](https://docs.moodle.org/23/en/Using_TeX_Notation) notation in the mathematical formulas.

`PyCloze02.py` an example with numerical data in the form of a table and outputs in numerical, short_answer and multi_choice format.

#### .xml files

`PyClz00.xml` file generated with `PyClz00.py`.

`PyClz01.xml` file generated with `PyClz01.py`.

`PyClz02.xml` file generated with `PyClz02.py`.


[calculated_q]:https://docs.moodle.org/39/en/Calculated_question_type

[cloze]:https://docs.moodle.org/39/en/Embedded_Answers_(Cloze)_question_type

[Import_questions]:https://docs.moodle.org/39/en/Import_questions#Importing_questions_from_an_existing_file

[Moodle]:https://moodle.org/?lang=en

[Tutorial_MarkDown]:https://agea.github.io/tutorial.md/

[random_q]:https://docs.moodle.org/39/en/Random_question_type

[penalty]:https://docs.moodle.org/39/en/Multiple_Choice_question_type#Penalty_factor
