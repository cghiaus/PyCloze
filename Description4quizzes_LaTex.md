# Description of quizzes

Author: [Christian Ghiaus](mailto:cghiaus@gmail.com)

[INSA Lyon](https://www.insa-lyon.fr), France, 18/04/2021

Three quizzes are presented:

1. PyClz00: given the names and the ages of three children, find the mean age, the eldest child and the longest name.
2. PyClz01: find the thermal resistance, the heat flux and the heat transfer rate of a flat wall. 
3. PyClz02: find the coefficient of heat exchange in forced and in natural convection.

For a quick visualization of the quizzes, [import][Import_questions] one of the `PyClz__.xml` files in Moodle. See [Tutorial_xml2moodle.md](Tutorial_xml2moodle.md) for further details on how to create a quiz with [random questions][random_q] (i.e. different questions for each student).

To visualize a `PyClz__.xml` file, open it with a browser. The file structure is according to [.xml format][xml].

Convenctions used in the descriptions of the problems: 
- input data is in **bold**,
- embedded answers are between { }.

## Quiz PyClz00

### Problem
______________________
John Smith has 3 children: **name_1**, age **age_1**, **name_2**, age, **age_2**,
**name_3**, age **age_3**. 

The mean age of the children is μ ={:NUMERICAL:}.

The eldest child is {:MULTICHOICE:}.

The child with the longest name is {:SHORTANSWER:}.
______________________

The input data for the problem:

|  |Child_1   |Child_2  |Child_3  |
|--|----------|---------|---------|
|Names|
|1.|Antoinette|Lawrence |Sebastian|
|2.|Anastasia |Catherine|Quentin  |
|Ages|
|1.|10.2      |12.9     |9.7      |
|2.|23.4      |12.5     |17.2     |
|3.|4.9       |14.1     |8.5      |

This set of data will generate 2 (name_list) x 3 (age_list) = 6 combinations of inputs from which one will be randomly assigned to a student.

## Quiz PyClz01

### Problem
______________________
Let's consider a flat concrete wall of width **w** [m] and surface area **S** [m²]. The surfaces at x = 0 and at x = w are maintained at temperatures **θ0** [°C] and **θw** [°C]. It will be assumed that
the heat transfer is in one direction and in steady state, without internal sources and that the thermal conductivity of concrete is **λ** [W/m·K].

Give the values of:

$U$ = {:NUMERICAL:} W/m²·K, thermal transmittance,

$R$ = {:NUMERICAL:} K/W, (absolute) thermal resistance,

$\varphi_{0,e}$ = {:NUMERICAL:} W/m², heat flux,

$q_{0,e}$ = {:NUMERICAL:} W, heat transfer rate.
_______________

The input data for the problem:

    w = np.arange(0.10, 0.30, 0.10)     # width [m] (2 values)
    S = np.arange(20, 30, 10)           # surface area [m²] (1 value)
    θ0 = np.arange(0, -10, -5)          # temperature at x = 0 [°C] (2 values)
    θw = np.arange(20, 22, 2)           # temperature at x = w [°C] (1 value)
    λ = np.array([0.5, 1.0, 1.8])       # thermal conductivity [W/m·K] (3 values)

This set of data will generate 2 x 1 x 2 x 1 x 3 = 12 questions from which one will be randomly assigned to a student.

### Solution

$$U = \frac{\lambda}{w}$$

$$R = \frac{1}{US}$$

$$\varphi_{0e} = U (\theta_0 - \theta_w)$$

$$q_{0e} = \frac{1}{R} (\theta_0 - \theta_w)$$


## Quiz PyClz02

### Problem

_______________
**Evaluation of convective exchange coefficients**

Let's consider a copper pipe in which a pump circulates water. The tube is in still air. It is considered that the temperature of the outer surface of the tube is almost equal to the temperature inside the tube. By using existing correlations for forced convection in the tube and for natural convection in the air (based on the Grashof number), find the values of the coefficients of convective exchange in the tube (water - tube) and outside of the tube (air - tube) for the water temperature in the pipe **θw** [K], and the air temperature **θa** [K].

Data

Thermo-physical properties

|Substance |T [K]|λ [W/m·K]|μ [Pa·s]|ρ [kg/m³]|c [J/kg·K]|β [1/K]|
|----------|-----|---------|--------|---------|----------|-------|
|Water     | Tw  |    λw   |   μw   |    ρw   |     cw   |   βw  |
|Air       | Ta  |    λa   |   μa   |    ρa   |     ca   |   βa  |

Pipe

|D [m]| w [m]| v [m/s]|
|-----|------|--------|
| D   | w    | v      |

Give the values of:

$h_i$ = {:NUMERICAL:} W/m²·K, coefficient of convective exchange between
water and pipe.

$h_{o, min}$ = {:NUMERICAL:} W/m²·K, minimum value of the convective exchange
coefficient of the pipe with the air.

$h_{o, max}$ = {:NUMERICAL:} W/m²·K, maximum value of the convective exchange
coefficient of the pipe with the air.

Fill in the sentence:

The correlation used for forced convection in a tube is called
the formula of {:SHORTANSWER}.

Choose the correct answer:

The type of air flow is {:MULTICHOICE:}
_______________

**The input data for the problem**

Thermophysical properties:

| |T[K] |    λ[W/m·K] | μ[Pa·s] |ρ[kg/m³] | c[J/kg·K] |  β[1/K] |
|-|-----|-------------|---------|---------|-----------|---------|
|water|
|1|330  |   0.650     |  489e-6 |     984 |      4184 | 504.0e-6|
|2|340  |   0.660     |  420e-6 |     979 |      4188 | 566.0e-6|
|3|350  |   0.668     |  365e-6 |     974 |      4195 | 624.2e-6|
|4|360  |   0.674     |  324e-6 |     967 |      4203 | 697.9e-6|
|5|365  |   0.677     |  306e-6 |     963 |      4209 | 701.1e-6|
|air  |
|1|250  |   22.3e-3   | 15.96e-6|  1.3947 |   1.006e3 | 4.08e-3 |
|2|300  |   26.3e-3   | 18.46e-6|  1.1614 |   1.007e3 | 3.38e-3 |

Copper pipe:

| |D[m] |  w[m] |  v [m/s] |
|-|-----|-------|----------|
|1|0.022| 0.001 |   0.63   |
|2|0.035| 0.001 |   0.81   |
|3|0.042| 0.001 |   0.89   |

This set of data will generate 5 x 2 x 3 = 30 questions from which one will be randomly assigned to a student.

### Solution


Find the convective coeficient for water:
- Find Reynolds number for the water in the tube:

$$Re = \frac{\rho v (D - 2 w)}{\mu}$$

- Find Prandtl number for water:

$$Pr = \frac{\mu c}{\lambda}$$

- If $0.7 \leq Pr \leq 160$ and $10000 \leq  Re  \leq 120000$, then:

$$Nu = 0.023 Re^{0.8} Pr^{0.33}$$

$$h_i = \frac{\lambda}{D - 2 w} Nu$$

Find the convective coeficient for air:

$$Pr = \frac{\mu c}{\lambda}$$

$$Gr = \frac{g \beta \rho^2 D^3}{\mu^2} (\theta_w - \theta_a)$$

If $10^3 < Gr < 10^9$, the flow is laminar;

if $10^9 < Gr < 10^12$, the flow is turbulent;

otherwise, the corelations are not applicable.

From

$$Nu = C (Gr Pr)^n$$

with the values of $C$ and $n$ given by:

|Flow type |      C        |  n  |
|----------|---------------|-----|
|laminar   | 0.2 ... 0.6   | 1/4 |
|turbulent | 0.07 ... 0.15 | 1/3 |

it results

$$h_o = \frac{\lambda}{D} Nu$$

The minimum and maximim values of $h_o$ are given by considering the minimum and maximum values of $C$.


[Import_questions]:https://docs.moodle.org/39/en/Import_questions#Importing_questions_from_an_existing_file

[xml]:https://docs.moodle.org/39/en/Moodle_XML_format

[random_q]:https://docs.moodle.org/39/en/Random_question_type