# Solutions to quizes

Author: [Christian Ghiaus](mailto:christian.ghiaus@insa-lyon.fr)

[INSA Lyon](https://www.insa-lyon.fr), France, 2020

For a quick visualization and test of the quizes, [import][Import_questions] one of the `PyCloze__.xml` files in Moodle. See [Tutorial_xml2moodle.md](Tutorial_xml2moodle.md) for further details on how to create a quiz with [random questions][random_q] (i.e. questions different for each student).

To visualize a `PyCloze__.xml` file, open it with a browser. The file structure is according to [.xml format][xml].

Convenctions used in the descriptions of the problems: 
- the input data is in **bold**,
- the embedded answers are between { }.

## Quiz PyCloze00.xml

### Problem
______________________
John Smith has 3 children: **name_1**, **age_1**, **name_2**, **age_2**,
**name_3**, **age_3**. 

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

This set of data will generate 2 x 3 = 6 combinations of inputs from which one will be randomly assigned to a student.

## Quiz PyCloze01.xml

### Problem
______________________
Let's consider a flat concrete wall of width **w** [m] and surface area **S** [m2]. The surfaces at x = 0 and at x = w are maintained at temperatures **θ0** [°C] and **θw** [°C]. It will be assumed that
the heat transfer is in one direction and in steady state, without internal sources and that the thermal conductivity of concrete is **λ** [W/m•K].

Give the values of:

U = {:NUMERICAL:} W/m2•K, thermal transmittance,

R = {:NUMERICAL:} K/W, (absolute) thermal resistance,

![$\varphi_{0,e}$](https://latex.codecogs.com/gif.latex?%5Cvarphi_%7B0%2Ce%7D) = {:NUMERICAL:} W/m2, heat flux,

¡[$q_{0,e}$](https://latex.codecogs.com/gif.latex?q_%7B0%2Ce%7D) = {:NUMERICAL:} W, heat transfer rate.
_______________

The input data for the problem:

    w = np.arange(0.10, 0.30, 0.10)     # width [m]
    S = np.arange(20, 30, 10)           # surface area [m2]
    θ0 = np.arange(0, -10, -5)          # temperature at x = 0 [°C]
    θw = np.arange(20, 22, 2)           # temperature at x = w [°C]
    λ = np.array([0.5, 1.0, 1.8])       # thermal conductivity [W/m•K]

This set of data will generate 2 x 1 x 2 x 1 x 3 = 12 questions from which one will be randomly assigned to a student.

### Solution
![$$U = \frac{\lambda}{w}$$](https://latex.codecogs.com/gif.latex?U%20%3D%20%5Cfrac%7B%5Clambda%7D%7Bw%7D)

![$$R = \frac{1}{US}$$](https://latex.codecogs.com/gif.latex?R%20%3D%20%5Cfrac%7B1%7D%7BUS%7D)

![$$\varphi_{0e} = U (\theta_0 - \theta_w)$$](https://latex.codecogs.com/gif.latex?%5Cvarphi_%7B0e%7D%20%3D%20U%20%28%5Ctheta_0%20-%20%5Ctheta_w%29)

![$$q_{0e} = \frac{1}{R} (\theta_0 - \theta_w)$$](https://latex.codecogs.com/gif.latex?q_%7B0e%7D%20%3D%20%5Cfrac%7B1%7D%7BR%7D%20%28%5Ctheta_0%20-%20%5Ctheta_w%29)


## Quiz PyCloze02.xml

### Problem

_______________
**Evaluation of convective exchange coefficients**

Let's consider a copper pipe in which a pump circulates water. The tube is in still air. It is considered that the temperature of the outer surface of the tube is almost equal to the temperature inside the tube. By using existing correlations for forced convection in the tube and for natural convection in the air (based on the Grashof number), find the values of the coefficients of convective exchange in the tube (water - tube) and outside of the tube (air - tube) for the water temperature in the pipe **θw** [K], and the air temperature **θa** [K].

Data

Thermo-physical properties

|Substance |T   |  λ |  μ |  ρ | c  |  β |
|----------|----|----|----|----|----|----|
|Water     | Tw | λw | μw | ρw | cw | βw |
|Air       | Ta | λa | μa | ρa | ca | βa |

Pipe

|D [m]| w [m]| v [m/s]|
|-----|------|--------|
| D   | w    | v      |

Give the values of:

h_i = {:NUMERICAL:} W/m2 K, coefficient of convective exchange between
water and pipe.

h_o,min = {:NUMERICAL:} W/m2 K, minimum value of the convective exchange
coefficient of the pipe with the air.

h_o,max = {:NUMERICAL:} W/m2 K, maximum value of the convective exchange
coefficient of the pipe with the air.

Fill in the sentence:

The correlation used for forced convection in a tube is called
the formula of {:SHORTANSWER}.

Choose the correct answer:

The type of air flow is {:MULTICHOICE:}
_______________

**The input data for the problem**

Thermophysical properties:

| |T[K] |    λ[W/m K] | μ[Pa s] |ρ[kg/m3] | c[J/kg K] |  β[1/K] |
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

![$$Re = \frac{\rho v (D - 2 w)}{\mu}$$](https://latex.codecogs.com/gif.latex?Re%20%3D%20%5Cfrac%7B%5Crho%20v%20%28D%20-%202%20w%29%7D%7B%5Cmu%7D)

- Find Prandtl number for water:

![$$Pr = \frac{\mu c}{\lambda}$$](https://latex.codecogs.com/gif.latex?Pr%20%3D%20%5Cfrac%7B%5Cmu%20c%7D%7B%5Clambda%7D)

- If 0.7 < Pr < 160 and 10000 <  Re  < 120000, then:

![$$Nu = 0.023 Re^{0.8} Pr^{0.33}$$](https://latex.codecogs.com/gif.latex?Nu%20%3D%200.023%20Re%5E%7B0.8%7D%20Pr%5E%7B0.33%7D)

![$$h_w = \frac{\lambda}{(D - 2 w)} Nu$$](https://latex.codecogs.com/gif.latex?h_w%20%3D%20%5Cfrac%7B%5Clambda%7D%7B%28D%20-%202%20w%29%7D%20Nu)

Find the convective coeficient for air:

![$$Pr = \frac{\mu c}{\lambda}$$](https://latex.codecogs.com/gif.latex?Pr%20%3D%20%5Cfrac%7B%5Cmu%20c%7D%7B%5Clambda%7D)

![$$Gr = \frac{g \beta \rho^2 D^3}{\mu^2} (\theta_w - \theta_a)$$](https://latex.codecogs.com/gif.latex?Gr%20%3D%20%5Cfrac%7Bg%20%5Cbeta%20%5Crho%5E2%20D%5E3%7D%7B%5Cmu%5E2%7D%20%28%5Ctheta_w%20-%20%5Ctheta_a%29)

If 1e3 < Gr < 1e9, the flow is laminar;

if 1e9 < Gr < 1e12, the flow is turbulent;

otherwise, the corelations are not applicable.

From

![$$Nu = C (Gr Pr)^n$$](https://latex.codecogs.com/gif.latex?Nu%20%3D%20C%20%28Gr%20Pr%29%5En)

with

|Flow type  |      C        |  n  |
|----------|---------------|-----|
|laminar   | 0.2 ... 0.6   | 1/4 |
|turbulent | 0.07 ... 0.15 | 1/3 |

it results

![$$h_a = \frac{\lambda}{D} Nu$$](https://latex.codecogs.com/gif.latex?h_a%20%3D%20%5Cfrac%7B%5Clambda%7D%7BD%7D%20Nu)

with minimum and maximim values of ![$h_a$](https://latex.codecogs.com/gif.latex?h_a) given by the values of C.


[Import_questions]:https://docs.moodle.org/39/en/Import_questions#Importing_questions_from_an_existing_file

[xml]:https://docs.moodle.org/39/en/Moodle_XML_format

[random_q]:https://docs.moodle.org/39/en/Random_question_type
