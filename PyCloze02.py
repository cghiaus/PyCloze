#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 07:06:08 2020

The @author: cghiaus

Creates PyCloze00.xml file for the following problem in which
the input data is between * *
the embedded answers are between { }:
-------------------------------------------------------------------------------
Evaluation of convective exchange coefficients

Let's consider a copper pipe in which a pump circulates water. The tube is in
still air. It is considered that the temperature of the outer surface of
the tube is almost equal to the temperature inside the tube.
By using existing correlations for forced convection in the tube and
for natural convection in the air (based on the Grashof number),
find the values of the coefficients of convective exchange in the tube
(water - tube) and outside of the tube (air - tube) for
the water temperature in the pipe θw = *water_T* K, and the air temperature
θa = *air_T* K.

Data
Thermo-physical properties
Substance	T	λ	μ	ρ	c	β
---------------------------------
Water       Tw λw	μw	ρw	cw	βw
Air         Ta λa	μa	ρa	ca	βa

Pipe
D [m]	w [m]	v [m/s]

Give the values of:
hi = {:NUMERICAL:} W/m2 K, coefficient of convective exchange between
water and pipe.
ho_min = {:NUMERICAL:} W/m2 K, minimum value of the convective exchange
coefficient of the pipe with the air.
ho_max = {:NUMERICAL:} W/m2 K, maximum value of the convective exchange
coefficient of the pipe with the air.

Fill in the sentence:
The correlation used for forced convection in a tube is called
the formula of {:SHORTANSWER}.

Choose the correct answer:
The type of air flow is {:MULTICHOICE:}
-------------------------------------------------------------------------------

The input data for the problem:
#   T[K]    λ[W/m K]  μ[Pa s]	ρ[kg/m^3]   c[J/kg K] β[K^-1]
water = np.array([
    [330,   0.650,  489e-6,     984,        4184,   504.0e-6],
    [340,   0.660,  420e-6,     979,        4188,   566.0e-6],
    [350,   0.668,  365e-6,     974,        4195,   624.2e-6],
    [360,   0.674,  324e-6,     967,        4203,   697.9e-6],
    [365,   0.677,  306e-6,     963,        4209,   701.1e-6]])

air = np.array([
    [250,   22.3e-3, 15.96e-6, 1.3947,      1.006e3, 4.08e-3],
    [300,   26.3e-3, 18.46e-6, 1.1614,      1.007e3, 3.38e-3]])

#    D[m]   w[m]    v [m/s]
pipe_copper = np.array([
    [22e-3, 1e-3,   0.63],
    [35e-3, 1e-3,   0.81],
    [42e-3, 1e-3,   0.89]])

To see the question: import PyCloze02.xml in Moodle.
To see the .xml file: open PyCloze02.xml in a browser.
"""
# 1. Import modules
import numpy as np
import sys
from itertools import product
import MoodleCloze


# . Create a function which solves the problem
def problem_fun(x):
    """
    Function solving the problem

    Parameters
    ----------
    x : list
        Inputs of the fuction that solves the problem.
        To be included in the CLOZE question as given data.

    Returns
    -------
    y : list
        Results of the function.
        To be included in the CLOZE question as requested answers.

    Notes
    -----
    Inputs: x : list of:
    water : list
        [0] : float     temperature, θw [K]
        [1] : float     thermal conductivity, λw [W/m K]
        [2] : float     viscosity, μw [Pa s]
        [3] : float     density, ρw [kg/m^3]
        [4] : float     specific heat, cw [J/kg K]
        [5] : float     expasion coeff, βw [K^-1]
    air : list
        [0] : float     temperature, θa [K]
        [1] : float     thermal conductivity, λa [W/m K]
        [2] : float     viscosity, μa [Pa s]
        [3] : float     density, ρa [kg/m^3]
        [4] : float     specific heat, ca [J/kg K]
        [5] : float     expasion coeff, βa [K^-1]
    pipe-copper : list
        [0] : float     external diameter, D [m]
        [1] : float     width, w [m]
        [2] : float     maximum velocity, v [m/s]


    Outputs: y : list of:
    ha : float          heat convection coeffcient inside, [W/m2 K]
    hw : float          heat convection coeffcient outside, [W/m2 K]
    Gr : float          Grashof number, Gr [-]
    flow_air : dict     flow type "laminar" or "turbulent"
                        ""  : for false
                        "=" : for true
    """
    θw, λw, μw, ρw, cw, βw = x[0]
    θa, λa, μa, ρa, ca, βa = x[1]
    D, w, v = x[2]

    Re = ρw*v*(D - 2*w)/μw
    Pr = μw*cw/λw
    if (0.7 <= Pr <= 160) and (10000 < Re < 120000):
        Nu = 0.023*Re**0.8*Pr**0.33
        hw = λw/(D - 2*w)*Nu
    else:
        print('D = ', D)
        print("Pr = 5.0f, Re = %5.0f" % Re, Pr)
        sys.exit()

    g = 9.81    # gravitational acceleration
    Pr = μa*ca/λa
    Gr = g*βa*ρa**2*D**3/μa**2*(θw - θa)
    flow_air = {
        "laminar": "",
        "turbulent": ""}
    if 1e3 < Gr < 1e9:
        C = np.array([0.2, 0.6])
        n = 1/4
        flow_air["laminar"] = "="
    elif 1e9 < Gr < 1e12:
        C = np.array([0.07, 0.15])
        n = 1/3
        flow_air["turbulent"] = "="
    else:
        print("Gr = %5.0f not in 1e7 < Gr < 1e9" % Gr)
        sys.exit()
    Nu = C*(Gr*Pr)**n
    ha = λa/D*Nu

    y = hw, ha, Gr, flow_air
    return y


# 3. Define the mapping between the variables of the problem
# (input and outputs) and the variables of the text of the problem
def insert_variables(x, y, text):
    """
    Insert the variables x (inputs) and y (outputs) in the text of the problem.

    Parameters
    ----------
    x : list
        Used as inputs for the problem computation function.
        Same as the x used in problem_fun(x).

    y : list
        Results of the problem computation function.
        Same as the x used in problem_fun(x).

    text : string
        Text of the problem with input and output values indicated as
        variables but not inserted.

    Returns
    -------
    problem_text : string
        Text of the problem with input and output values inserted.
    """
    problem_text = text % {
            "θw": x[0][0], "λw": x[0][1], "μw": x[0][2],
            "ρw": x[0][3], "cw": x[0][4], "βw": x[0][5],
            "θa": x[1][0], "λa": x[1][1], "μa": x[1][2],
            "ρa": x[1][3], "ca": x[1][4], "βa": x[1][5],
            "D": x[2][0], "w": x[2][1], "v": x[2][2],

            "hw": y[0], "err_hw": 0.05*y[0],
            "ha_min": y[1][0], "err_ha_min": 0.05*y[1][0],
            "ha_max": y[1][1], "err_ha_max": 0.05*y[1][1],
            "Gr": y[2], "err_Gr": 0.05*y[2],
            "flow_air_laminar": y[3]["laminar"],
            "flow_air_turbulent": y[3]["turbulent"]}
    return problem_text


# 4. Write the text of the cloze question in Markdown
text = """
**Evaluation of convective exchange coefficients**

Let's consider a copper pipe in which a pump
circulates water. The tube is in still air. It is considered
that the temperature of the outer surface of the tube
is almost equal to the temperature inside the tube.


By using existing correlations for forced convection
in the tube and for natural convection in the air
(based on the Grashof number), find the values of the coefficients
of convective exchange in the tube (water - tube) and outside of the tube
(air - tube) for the water temperature in the pipe
$$\\theta_{water}$$ = %(θw)3.0f K,
and the air temperature
$$\\theta_{air}$$ = %(θa)3.0f K.

<br/>

**Data**

*Thermo-physical properties*

|Substance|T        | λ       |	   μ        |	 ρ       |   c        |   β   |
|---------|------   | ------- | -----      | --------   | --------   | ----- |
|         | $$K$$   | $$W/m\\cdot K$$|$$Pa\\cdot s$$| $$kg/m^3$$|$$J/kg\\cdot K$$| $$K^{-1}$$|
|____________|_________|____________|____________|____________|____________|____________|
|Water    |%(θw)2.0f| %(λw)4.3f| %(μw).3e  | %(ρw)3.0f  | %(cw)3.0f | %(βw).4e|
|Air      |%(θa)2.0f| %(λa)4.4f| %(μa).3e  | %(ρa)5.4f  | %(ca)3.0f | %(βa).4e|

<br/>

*Pipe*

|Ext. diameter   | Width       | Water velocity  |
|----------------|-------------|-----------------|
| D [m]          |   e [m]     |      v [m/s]    |
|________________|_____________|_________________|
| %(D)0.3f       |  %(w)0.3f   |   %(v)3.2f      |

<br/>


**Give the values of:**

$$h_i$$ = {1:NUMERICAL:=%(hw)3.0f:%(err_hw)3.1f} $$W/m^2K$$,
coefficient of convective exchange between  water and pipe.

$$h_{o,min}$$ = {1:NUMERICAL:=%(ha_min)3.1f:%(err_ha_min)3.2f} $$W/m^2K$$,
minimum value of the convective exchange coefficient of the pipe with the air.

$$h_{o,max}$$ = {1:NUMERICAL:=%(ha_max)3.1f:%(err_ha_max)3.2f} $$W/m^2K$$,
maximum value of the convective exchange coefficient of the pipe with the air.

**Fill in the sentence:**

The correlation used for forced convection in a tube is called the formula of
{1:SHORTANSWER:=Colburn}

**Choose the correct answer:**

The type of air flow is {1:MULTICHOICE:undetermined
                           ~%(flow_air_laminar)s laminar
                           ~%(flow_air_turbulent)s turbulent}
"""

# 5. Define the input space

# T[K] 	λ[W/m K]	μ[Pa s]	ρ[kg/m^3]	c[J/kg K] β[K^-1]
water = np.array([
    [330, 0.650, 489e-6, 984, 4184, 504.0e-6],
    [340, 0.660, 420e-6, 979, 4188, 566.0e-6],
    [350, 0.668, 365e-6, 974, 4195, 624.2e-6],
    [360, 0.674, 324e-6, 967, 4203, 697.9e-6],
    [365, 0.677, 306e-6, 963, 4209, 701.1e-6]])

air = np.array([
    [250, 22.3e-3, 15.96e-6, 1.3947, 1.006e3, 4.08e-3],
    [300, 26.3e-3, 18.46e-6, 1.1614, 1.007e3, 3.38e-3]])

# D [m], w[m], v [m/s]
pipe_copper = np.array([
    [22e-3, 1e-3, 0.63],
    [35e-3, 1e-3, 0.81],
    [42e-3, 1e-3, 0.89]])

x_ranges = [water, air, pipe_copper]

# 6. Generate the quiz in Moodle.cloze format
question_name = "PyClozeEN_"          # It will be followed by question number
quiz = MoodleCloze.generate_quiz(question_name, problem_fun, x_ranges,
                                 insert_variables, text)

# 7. Save the quiz in an .xml file.
xml_file_name = 'PyCloze02.xml'
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
