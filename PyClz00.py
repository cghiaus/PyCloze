#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 10:38:03 2021

@author: cghiaus

Creates PyClz00.xml file for the following problem in which
the input data is between * *
the embedded answers are between { }:
-------------------------------------------------------------------------------
John Smith has 3 children: *name_1*, age *age_1*, *name_2*, age *age_2*,
*name_3*, age *age_3*.
The mean age of the children is μ ={:NUMERICAL:}.
The eldest child is {:MULTICHOICE:}.
The child with the longest name is {:SHORTANSWER:}.
-------------------------------------------------------------------------------

The input data for the problem:
    name = np.array([['Antoinette', 'Lawrence', 'Sebastian'],
                     ['Anastasia', 'Catherine', 'Quentin']])
    age = np.array([[10.2, 12.9, 9.7],
                    [23.4, 12.5, 17.2],
                    [4.9, 14.1, 8.5]])

To see the question: import PyClz00.xml in Moodle.
To see the .xml file: open PyClz00.xml in a browser.
"""

# 1. Import modules
import numpy as np
import MdlClz


# 2. Create a function which solves the problem
def problem_fun(x):
    """
    Function solving the problem
    x : dict
        inputs: data for the quiz
    Returns
    y : dict
        outputs: embedded answers in the quiz
    """
    mean_age = x['age'].mean()

    oldest = len(x['age']) * [""]       # list of 3 ""
    oldest[np.argmax(x['age'])] = "="   # "=" to the oldest

    names_length = sorted(x['name'], key=len)
    longest_name = names_length[-1]

    y = {'mean_age': mean_age,
         'oldest': oldest,
         'longest_name': longest_name}
    return y


# 3. Define the input space
x_ranges = {'name': np.array([['Antoinette', 'Lawrence', 'Sebastian'],
                              ['Anastasia', 'Catherine', 'Quentin']]),
            'age': np.array([[10.2, 12.9, 9.7],
                             [23.4, 12.5, 17.2],
                             [4.9, 14.1, 8.5]])}


# 4. Write the text of the cloze question in Markdown
text = """
John Smith has 3 children:
{name[0]:s}, age {age[0]:.1f},
{name[1]:s}, age {age[1]:.1f},
{name[2]:s}, age {age[2]:.1f}.

The mean age of the children is
$$\\mu$$ = {{1:NUMERICAL:={mean_age:.1f}:0.5}} (±0.5).

The eldest child is :
{{1:MULTICHOICE:{oldest[0]:s} {name[0]:s}
               ~{oldest[1]:s} {name[1]:s}
               ~{oldest[2]:s} {name[2]:s}}}.

The child with the longest name is {{1:SHORTANSWER:~={longest_name:s}}}.
"""


# 5. Generate the quiz in Moodle - cloze format and save .xml file
question_name = "PyClz00"          # will be followed by the question number
quiz = MdlClz.generate_quiz(question_name, problem_fun, x_ranges, text)


# 6. Show the inputs and outputs of all tests
test_nr = 0
for x in MdlClz.cprod(x_ranges):
    print("Test: ", test_nr)
    print("Inputs:")
    print(x)
    print("Outputs:")
    print(problem_fun(x), "\n")
    test_nr += 1
