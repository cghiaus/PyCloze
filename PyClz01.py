#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 10:38:03 2021

@author: cghiaus

Creates PyClz01.xml file for the following problem in which
the input data is between * *
the embedded answers are between { }:
-------------------------------------------------------------------------------
Let's consider a flat concrete wall of width w = *w* m and
surface area S = *S* m². The surfaces at x = 0 and at x = w are maintained
at temperatures θ0 = *θ0* °C and θw = *θw* °C. It will be assumed that
the heat transfer is in one direction and in steady state, without
internal sources and that the thermal conductivity of the concrete is
λ = *λ* W/m•K.

Give the values of:
U = {:NUMERICAL:} W/m²·K, thermal transmittance,
R = {:NUMERICAL:} K/W, (absolute) thermal resistance,
φ_{0,e} = {:NUMERICAL:} W/m², heat flux,
q_{0,e} = {:NUMERICAL:} W, heat transfer rate.
-------------------------------------------------------------------------------

The input data for the problem:
    w = np.arange(0.10, 0.30, 0.10)     # width [m]
    S = np.arange(20, 30, 10)           # surface area [m²]
    θ0 = np.arange(0, -10, -5)          # temperature at x = 0 [°C]
    θw = np.arange(20, 22, 2)           # temperature at x = w [°C]
    λ = np.array([0.5, 1.0, 1.8])       # thermal conductivity [W/m·K]

To see the question: import PyClz01.xml in Moodle.
To see the .xml file: open PyClz01.xml in a browser.
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
    # inputs
    w, S, θ0, θw, λ = [x[k] for k in ['w', 'S', 'θ0', 'θw', 'λ']]

    # computation
    U = λ / w               # thermal transmittance (U-value) [W/m²·K]
    R = 1 / (U * S)         # (absolute) thermal resistance [K/W]
    φ = U * (θ0 - θw)       # heat flux [W/m²]
    q = 1 / R * (θ0 - θw)   # heat transfer rate [W]

    # outputs
    y = {'U': U,
         'R': R,
         'φ': φ,
         'q': q}
    return y


# 3. Define the input space
x_ranges = {'w': np.arange(0.10, 0.30, 0.10),   # width [m]
            'S': np.arange(20, 30, 10),         # surface area [m²]
            'θ0': np.arange(0, -10, -5),        # temperature at x = 0 [°C]
            'θw': np.arange(20, 22, 2),         # temperature at x = w [°C]
            'λ': np.array([0.5, 1.0, 1.8])}     # thermal conductivity [W/m·K]


# 4. Write the text of the cloze question in Markdown
text = """
Let's consider a flat concrete wall of width $$w$$ = {w:3.2f} m
and surface area $$S$$ = {S:3.2f} m<sup>2</sup>.
The surfaces at $$x$$ = 0 and at $$x = w$$ are maintained at temperatures
$$\\theta_0$$ = {θ0:3.1f} °C and
$$\\theta_w$$ = {θw:3.1f} °C.
It will be assumed that the heat transfer is in one direction and in steady
state, without internal sources and that the thermal conductivity of medium
concrete is
$$\\lambda$$ = {λ:3.2f} W/m·K.

**Give the values of:**

$$U$$ = {{1:NUMERICAL:={U:3.2f}:0.5}} (±0.5) W/m<sup>2</sup>K,
thermal transmittance

$$R$$ = {{1:NUMERICAL:={R:7.6f}:0.005}} (±0.005) K/W,
(absolute) thermal resistance,

$$\\varphi_{{0,w}}$$ = {{1:NUMERICAL:={φ:3.2f}:10}} (±10) W/m<sup>2</sup>,
heat flux from $$x$$ = 0 to $$x = w$$,

$$q_{{0,w}}$$ = {{1:NUMERICAL:={q:3.2f}:100}} (±100) W,
heat transfer rate from $$x$$ = 0 to $$x = w$$.
"""

# 5. Generate the quiz in Moodle - cloze format and save .xml file
question_name = "PyClz01"          # will be followed by the question number
quiz = MdlClz.generate_quiz(question_name, problem_fun, x_ranges, text)

# 6. Show the inputs and outputs of all questions
test_nr = 0
for x in MdlClz.cprod(x_ranges):
    print("Test: ", test_nr)
    print("Inputs:")
    print(x)
    print("Outputs:")
    print(problem_fun(x), "\n")
    test_nr += 1
