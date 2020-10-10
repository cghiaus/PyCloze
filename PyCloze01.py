#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 08:15:01 2020

@author: cghiaus

Creates PyCloze00.xml file for the following problem in which
the input data is between * *
the embedded answers are between { }:
-------------------------------------------------------------------------------
Let's consider a flat concrete wall of width w = *w* m and
surface area S = *S* m2. The surfaces at x = 0 and at x = w are maintained
at temperatures θ0 = *θ0* °C and θw = *θw* °C. It will be assumed that
the heat transfer is in one direction and in steady state, without
internal sources and that the thermal conductivity of concrete is
λ = *λ* W/m•K.

Give the values of:
U = {:NUMERICAL:} W/m2K, thermal transmittance,
R = {:NUMERICAL:} K/W, (absolute) thermal resistance,
φ_{0,e} = {:NUMERICAL:} W/m2, heat flux,
q_{0,e} = {:NUMERICAL:} W, heat transfer rate.
-------------------------------------------------------------------------------

The input data for the problem:
    w = np.arange(0.10, 0.30, 0.10)     # width [m]
    S = np.arange(20, 30, 10)           # surface area [m2]
    θ0 = np.arange(0, -10, -5)          # temperature at x = 0 [°C]
    θw = np.arange(20, 22, 2)           # temperature at x = w [°C]
    λ = np.array([0.5, 1.0, 1.8])       # thermal conductivity [W/m K]

To see the question: import PyCloze01.xml in Moodle.
To see the .xml file: open PyCloze01.xml in a browser.
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
        inputs
    Returns
    y : list
        outputs
    """
    w, S, θ0, θw, λ = x     # inputs
    U = λ / w               # thermal transmittance (U-value) [W/m2•K]
    R = 1 / (U * S)         # (absolute) thermal resistance [K/W]
    φ = U * (θ0 - θw)     # heat flux [W/m2]
    q = 1 / R * (θ0 - θw)   # heat transfer rate [W]
    y = U, R, φ, q        # outputs
    return y


# 3. Define the mapping between the variables of the problem
# (input and outputs) and the variables of the text of the problem
def insert_variables(x, y, text):
    """
    Problem text
    x   - input (list): inputs for the problem computation function
    y   - output (list): result of problem computation function
    """

    problem_text = text % {
        "w": x[0], "S": x[1], "θ0": x[2], "θw": x[3], "λ": x[4],
        "U": y[0], "err_U": 0.05*y[0],
        "R": y[1], "err_R": 0.05*y[1],
        "φ": y[2], "err_phi": 0.05*y[2],
        "q": y[3], "err_q": 0.05*y[3]}
    return problem_text


# 4. Write the text of the cloze question in Markdown
text = """
Let's consider a flat concrete wall of width
$$w$$ = %(w)3.2f m
and surface area
$$S$$ = %(S)3.2f m<sup>2</sup>.
The surfaces at $$x$$ = 0 and at $$x = w$$ are maintained at temperatures
$$\\theta_0$$ = %(θ0)3.1f °C and
$$\\theta_w$$ = %(θw)3.1f °C.
It will be assumed that the heat transfer is in one direction and in steady
state, without internal sources and that the thermal conductivity of medium
concrete is
$$\\lambda$$ = %(λ)3.2f W/m•K.

**Give the values of:**

$$U$$ = {1:NUMERICAL:=%(U)3.2f:%(err_U)3.2f} W/m<sup>2</sup>K,
thermal transmittance

$$R$$ = {1:NUMERICAL:=%(R)7.6f:%(err_R)7.6f} K/W,
(absolute) thermal resistance,

$$\\varphi_{0,e}$$ = {1:NUMERICAL:=%(φ)3.2f:%(err_phi)3.2f} W/m<sup>2</sup>,
heat flux,

$$q_{0,e}$$ = {1:NUMERICAL:=%(q)3.2f:%(err_q)3.2f} W,
heat transfer rate.
"""

# 5. Define the space of the inputs of the problem
w = np.arange(0.10, 0.30, 0.10)     # width [m]
S = np.arange(20, 30, 10)           # surface area [m2]
θ0 = np.arange(0, -10, -5)          # temperature at x = 0 [°C]
θw = np.arange(20, 22, 2)           # temperature at x = w [°C]
λ = np.array([0.5, 1.0, 1.8])       # thermal conductivity [W/m K]

x_ranges = (w, S, θ0, θw, λ)

# 6. Generate the quiz in Moodle.cloze format
question_name = "PyCloze01_"
quiz = MoodleCloze.generate_quiz(question_name, problem_fun, x_ranges,
                                 insert_variables, text)

# 7. Save the quiz in an .xml file.
xml_file_name = 'PyCloze01.xml'
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
