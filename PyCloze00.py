#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:49:06 2020

@author: cghiaus

Creates PyCloze00.xml file for the following problem in which
the input data is between * *
the embedded answers are between { }:
-------------------------------------------------------------------------------
John Smith has 3 children: *name_1*, *age_1*, *name_2*, *age_2*,
*name_3*,*age_3*.
The mean age of the children is μ ={:NUMERICAL:}.
The eldest child is {:MULTICHOICE:}.
The child with the longest name is {:SHORTANSWER:}.
-------------------------------------------------------------------------------

The input data for the problem:
    names = np.array([
        ['Antoinette', 'Lawrence', 'Sebastian'],
        ['Anastasia', 'Catherine', 'Quentin']
        ])
    ages = np.array([
        [10.2, 12.9, 9.7],
        [23.4, 12.5, 17.2],
        [4.9, 14.1, 8.5]
        ])

To see the question: import PyCloze00.xml in Moodle.
To see the .xml file: open PyCloze00.xml in a browser.
"""
# 1. Import modules
import numpy as np
from itertools import product
import MoodleCloze


# 2. Create a function which solves the problem
def problem_fun(x):
    """
    Function solving the problem
    x : list
        inputs: data for the quiz
    Returns
    y : list
        outputs: embedded answers in the quiz
    """
    names, ages = x                  # inputs

    mean_age = ages.mean()
    oldest = len(ages)*[""]          # list of 3 ""
    oldest[np.argmax(ages)] = "="    # "=" to the oldest
    names_length = sorted(names, key=len)

    y = [mean_age, oldest, names_length[-1]]
    return y


# 3. Define the mapping between the variables of the problem
# (input and outputs) and the variables of the text of the problem
def insert_variables(x, y, text):
    """
    Problem text
    x : list
        inputs: data for the quiz
    y : list
    -   outputs: embedded answers in the quiz
    """
    problem_text = text % {
        "name_1": x[0][0], "name_2": x[0][1], "name_3": x[0][2],
        "age_1": x[1][0], "age_2": x[1][1], "age_3": x[1][2],
        "mean_age": y[0], "err_mean_age": 0.05*y[0],
        "oldest_1": y[1][0], "oldest_2": y[1][1], "oldest_3": y[1][2],
        "longest_name": y[2]}
    return problem_text


# 4. Write the text of the cloze question in Markdown
text = """
John Smith has 3 children:
%(name_1)s, %(age_1).1f,
%(name_2)s, %(age_2).1f,
%(name_3)s, %(age_3).1f.

The mean age of the children is
$$\\mu$$ = {1:NUMERICAL:=%(mean_age)3.1f:%(err_mean_age)3.2f}.

The eldest child is :
{1:MULTICHOICE:%(oldest_1)s %(name_1)s
              ~%(oldest_2)s %(name_2)s
              ~%(oldest_3)s %(name_3)s}.

The child with the longest name is {1:SHORTANSWER:~=%(longest_name)s}.
"""

# 5. Define the input space
names = np.array([
    ['Antoinette', 'Lawrence', 'Sebastian'],
    ['Anastasia', 'Catherine', 'Quentin']
    ])
ages = np.array([
    [10.2, 12.9, 9.7],
    [23.4, 12.5, 17.2],
    [4.9, 14.1, 8.5]
    ])

x_ranges = [names, ages]

# 6. Generate the quiz in Moodle - cloze format
question_name = "PyCloze_"          # It will be followed by question number
quiz = MoodleCloze.generate_quiz(question_name, problem_fun, x_ranges,
                                 insert_variables, text)

# 7. Save the quiz in an .xml file.
xml_file_name = 'PyCloze00.xml'
with open(xml_file_name, 'w') as MOODLE_cloze:
    MOODLE_cloze.write(quiz)

# 8. [Optional] Show the inputs and outputs of all questions
test_nr = 0
for x in product(*x_ranges):
    print("Test: ", test_nr)
    print("Inputs:")
    print(x)
    print("Outputs:")
    print(problem_fun(x), "\n")
    test_nr += 1
