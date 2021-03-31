#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 11:57:20 2021

@author: cghiaus

Creates PyClz02.xml file for the following problem in which
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
hi = {:NUMERICAL:} W/m²·K, coefficient of convective exchange between
water and pipe.
ho_min = {:NUMERICAL:} W/m²·K, minimum value of the convective exchange
coefficient of the pipe with the air.
ho_max = {:NUMERICAL:} W/m²·K, maximum value of the convective exchange
coefficient of the pipe with the air.

Fill in the sentence:
The correlation used for forced convection in a tube is called
the formula of {:SHORTANSWER}.

Choose the correct answer:
The type of air flow is {:MULTICHOICE:}
-------------------------------------------------------------------------------

The input data for the problem:
#   T[K]    λ[W/m K]  μ[Pa·s]	ρ[kg/m³]    c[J/kg·K] β[1/K]
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

To see the question: import PyClz02.xml in Moodle.
To see the .xml file: open PyClz02.xml in a browser.
"""

# 1. Import modules
import numpy as np
import sys
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
    g = 9.81    # gravitational acceleration

    # inputs
    [θw, λw, μw, ρw, cw, βw], [θa, λa, μa, ρa, ca, βa], [D, w, v] = \
        [x[k] for k in ['water', 'air', 'pipe_copper']]

    # computation
    Re = ρw * v * (D - 2 * w) / μw
    Pr = μw * cw / λw
    if (0.7 <= Pr <= 160) and (10000 < Re < 120000):
        Nu = 0.023 * Re**0.8 * Pr**0.33
        hw = λw / (D - 2 * w) * Nu
    else:
        print('D = ', D)
        print("Pr = 5.0f, Re = %5.0f" % Re, Pr)
        sys.exit()

    Pr = μa * ca / λa
    Gr = g * βa * ρa**2 * D**3 / μa**2 * (θw - θa)
    flow_air = {"laminar": "",
                "turbulent": ""}
    if 1e3 < Gr < 1e9:
        C = np.array([0.2, 0.6])
        n = 1 / 4
        flow_air["laminar"] = "="
    elif 1e9 < Gr < 1e12:
        C = np.array([0.07, 0.15])
        n = 1 / 3
        flow_air["turbulent"] = "="
    else:
        print("Gr = %5.0f not in 1e7 < Gr < 1e9" % Gr)
        sys.exit()
    Nu = C * (Gr * Pr)**n
    ha = λa / D * Nu

    # outputs
    y = {'hw': hw,
         'ha_min': ha[0],
         'ha_max': ha[1],
         'Gr': Gr,
         'flow_air_laminar': flow_air['laminar'],
         'flow_air_turbulent': flow_air['turbulent']}
    return y


# 3. Define the input space
#                                T     λ      μ	      ρ    c       β
x_ranges = {'water': np.array([[330, 0.650, 489e-6, 984, 4184, 504.0e-6],
                               [340, 0.660, 420e-6, 979, 4188, 566.0e-6],
                               [350, 0.668, 365e-6, 974, 4195, 624.2e-6],
                               [360, 0.674, 324e-6, 967, 4203, 697.9e-6],
                               [365, 0.677, 306e-6, 963, 4209, 701.1e-6]]),
            'air': np.array([[250, 22.3e-3, 15.96e-6, 1.3947, 1.006e3,
                              4.08e-3],
                             [300, 26.3e-3, 18.46e-6, 1.1614, 1.007e3,
                              3.38e-3]]),
            #                           D      w     v
            'pipe_copper': np.array([[22e-3, 1e-3, 0.63],
                                     [35e-3, 1e-3, 0.81],
                                     [42e-3, 1e-3, 0.89]])}


# 4. Write the text of the cloze question in Markdown
text = """
#Evaluation of convective exchange coefficients

Let's consider a copper pipe in which a pump
circulates water. The tube is in still air. It is considered
that the temperature of the outer surface of the tube
is almost equal to the temperature inside the tube.

By using existing correlations for forced convection
in the tube and for natural convection in the air
(based on the Grashof number), find the values of the coefficients
of convective exchange in the tube (water - tube) and outside of the tube
(air - tube) for the water temperature in the pipe
$$\\theta_{{water}}$$ = {water[0]:3.0f} K,
and the air temperature
$$\\theta_{{air}}$$ = {air[0]:3.0f} K.

<br/>

**Data**

*Thermo-physical properties*

|Substance|Temperature    |Conductivity   |	Viscosity     |	Density       | Specific heat  |Expansion coef.|
|---------|---------------|---------------|--------------|---------------|----------------|---------------|
|         |T [K]          |λ [W/m·K]      |μ [Pa·s]      | ρ [kg/m³]     | c [J/kg·K]     | β [1/K]       |
|_________|_______________|_______________|______________|_______________|________________|_______________|
|Water    |{water[0]:2.0f}|{water[1]:4.3f}|{water[2]:.3e}|{water[3]:3.0f}|{water[4]:3.0f} |{water[4]:.4e} |
|Air      |{air[0]:2.0f}  |{air[1]:4.3f}  |{air[2]:.3e}  |{air[3]:3.0f}  |{air[4]:3.0f}   |{air[4]:.4e}   |

<br/>

*Pipe*

|Ext. diameter        | Width                | Water velocity      |
|---------------------|----------------------|---------------------|
| D [m]               | w [m]                | v [m/s]             |
|_____________________|______________________|_____________________|
|{pipe_copper[0]:0.3f}| {pipe_copper[1]:0.3f}|{pipe_copper[2]:3.2f}|

<br/>

**Give the values of:**

$$h_i$$ = {{1:NUMERICAL:={hw:3.0f}:10}} (±10) $$\\mathrm{{W/m^2K}}$$,
coefficient of convective exchange between water and pipe.

$$h_{{o,min}}$$ = {{1:NUMERICAL:={ha_min:3.1f}:1}} (±1) $$\\mathrm{{W/m^2K}}$$,
minimum value of the convective exchange coefficient of the pipe with the air.

$$h_{{o,max}}$$ = {{1:NUMERICAL:={ha_max:3.1f}:1}} (±1) $$\\mathrm{{W/m^2K}}$$,
maximum value of the convective exchange coefficient of the pipe with the air.


**Fill in the sentence:**

The correlation used for forced convection in a tube is called the formula of
{{1:SHORTANSWER:=Colburn}}

**Choose the correct answer:**

The type of air flow is {{1:MULTICHOICE:undetermined
                           ~{flow_air_laminar:s} laminar
                           ~{flow_air_turbulent:s} turbulent}}

"""


# 5. Generate the quiz in Moodle - cloze format and save .xml file
question_name = "PyClz02"          # will be followed by the question number
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
