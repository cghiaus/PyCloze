# Create questions in Python and save them in a Moodle .xml file

Author: [Christian Ghiaus](mailto:cghiaus@gmail.com)

[INSA Lyon](https://www.insa-lyon.fr), France, 2020

This tutorial shows how to create a Python code to obtain questions in `.xml` file that will be imported in Moodle. You can visualize `.xml` files by open them with a browser.

Requirements:

1. Python 3.
2. The file `PyCloze00.py`.

______________________________________
**Typical structure of the Pyton code** to generate cloze questions in `.xml` file:
1. Import modules.
2. Create a function which solves the problem.
3. Insert the variables in the text of the problem.
4. Write the text of the cloze question in Markdown.
5. Define the input space.
6. Generate the quiz in Moodle - cloze format.
7. Save the quiz in an `.xml` file.
8. [Optional] Show the inputs and the outputs for all questions`.
______________________________________

This structure is discussed by going through a simple example, `PyCloze00.py`. Examples of other tests are given in `PyCloze01.py` and `PyCloze02.py`.

______________________________________
**Workflow for developing a new quiz**

When creating a new quiz, the chain of operations is different of the order indicated in the Python code. It may be:

1. Import modules.
5. Define the input space.
8. Show the inputs and outputs of all questions.
2. Create a function which solves the problem.
3. Define the mapping between the variables of the problem: inputs & outputs and the variables of the text of the problem.
4. Write the text of the cloze question in Markdown.
6. Generate the quiz in Moodle - cloze format.
7. Save the quiz in an .xml file.
______________________________________


## `PyCloze00.py`: walk through a simple example

The  aim is to obtain a quiz with embedded input data and answers that looks like below:

______________________________________

John Smith has 3 children: **name_1**, **age_1**, **name_2**, **age_2**, **name_3**,**age_3**.

The mean age of the children is μ =`____`

The eldest child is `________↕`

The child with the longest name is `_________`
______________________________________

For the input space, we want that the `names` of the three children to be one of these two lists:

**[Antoinette, Lawrence, Sebastian]**,

**[Anastasia, Catherine, Quentin]**,

and their respective `ages` to be one of these three lists:

**[10.2, 12.9, 9.7]**,

**[23.4, 12.5, 17.2]**,

**[4.9, 14.1, 8.5]**.

Six (2 names x 3 ages) combinations of inputs are obtained, which corespond to six quizes.

For the answers, we want:

|Answer     |  Type      | Contents                    |
|-----------|------------|-----------------------------|
|μ =`____`  | NUMERICAL  |numerical value +/- 5%       |
|`________↕`| MULTICHOICE|choose one out of three names|
|`_________`| SHORTANSWER|a name                       |

For a quick view of the quiz, [import][Import_questions] the questions in Moodle from the file `PyCloze00.xml` (see [Tutorial_xml2moodle.md](Tutorial_xml2moodle.md) for how to make a test in Moodle and import questions in `.xml` format).  

## Description of Python code

### 1. Import modules

    import numpy as np
    from itertools import product
    import MoodleCloze


You need to [import](https://docs.python.org/3/reference/import.html) at least [itertools](https://docs.python.org/3/library/itertools.html) and `MoodleCloze`. Typically, you will also need [numpy](https://numpy.org/doc/).


### 2. Create a function which solves the problem

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

The inputs `x` and outputs `y` need to be [lists](https://realpython.com/python-lists-tuples/) of [iterators](https://wiki.python.org/moin/Iterator), e.g. [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) or [np.array](https://numpy.org/doc/stable/reference/generated/numpy.array.html) (but not [int or float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)).


*Note*: Python accepts Greek characters. If you use [Spyder](https://www.spyder-ide.org) IDE, you can type them in IPython console as \GreekLetter[TAB]. For example, \alpha[TAB] will give α.

### 3. Insert the variables in the text of the problem

    def insert_variables(x, y, text):
        """
        Problem text
        x   - list
              inputs: data for the quiz
        y   - list
              outputs: embedded answers in the quiz
        """
        problem_text = text % {
            "name_1": x[0][0], "name_2": x[0][1], "name_3": x[0][2],
            "age_1": x[1][0], "age_2": x[1][1], "age_3": x[1][2],
            "mean_age": y[0], "err_mean_age": 0.05*y[0],
            "oldest_1": y[1][0], "oldest_2": y[1][1], "oldest_3": y[1][2],
            "longest_name": y[2]}
        return problem_text


The function `insert_variables(x, y, text)`  inserts the variables (inputs `x` and outputs `y`) in the `text` of the Moodle quiz. It substitues [variables by name](https://realpython.com/python-string-formatting/) by passing to `%`operator the variables using the following **mapping** :

|Name       | Variable|
|-----------|---------|
|"name_1":  | x[0][0] |
|"name_2":  | x[0][1] |
|"name_3":  | x[0][2] |
|"age_1":   | x[1][0] |
|"age_2":   | x[1][1] |
|"age_3":   | x[1][2] |
|"mean_age":| y[0]|
|"err_mean_age":|0.05*y[0]|
|"oldest_1":| y[1][0]|
|"oldest_2":| y[1][1]|
|"oldest_3":| y[1][2]|
|"longest_name": |y[2]|


| Code | Explanation|
|------|------------|
|`problem_text`| Text of the quiz.|
|`text`| Text of the quiz with [old style string formatting][old_format] (see section 4).|
|` % {` |Open the [dictionary][dict] for [old style string formatting][old_format1].|
||*Input data*|
|` "name_1": `| Name of the variable in the `text` of the quiz (see the **mapping**).|
| `x[0][0]`   | Value of the variable taken from `x_ranges`(see section 5).|
| ... | ... |
||*Embedded answers* |
||NUMERICAL|
|`"mean_age":`| Name of the variable in NUMERICAL answer (see the **mapping**).|
|`y[0]`| Value given by the function `problem_fun(x)`.|
|` "err_mean_age": `| Name of the error in NUMERICAL answer (see the **mapping**).|
|`0.05*y[0] `| Value of accepted error (here 5 % of y[0]).|
| | MULTICHOICE|
|` "oldest_1": `| Name of 1st variable (see the **mapping**).|
|` y[1][0] `|Value "=" if the 1st child in the list is the oldest; "" if not.|
|` "oldest_2": `|Name of 2nd variable (see the **mapping**).|
|` y[1][1] `|Value "=" if the 2st child in the list is the oldest; "" if not.|
|` "oldest_3": `|Name of 3rd variable (see the **mapping**).|
|` y[1][2] `|Value "=" if the 3rd child in the list is the oldest; "" if not.|
||SHORTANSWER|
|` "longest_name": `|Name of the variable (see the **mapping**).|
|` y[2] `|Value containing the longest name given by the function `problem_fun(x)`..|
|` } `|Close the dictionary.|


### 4. Write the text of the cloze question in [Markdown](https://www.markdownguide.org)

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

By inserting the variables

    x = (array(['Antoinette', 'Lawrence', 'Sebastian']), array([10.2, 12.9,  9.7]))

and 

    y = [10.933333333333332, ['', '=', ''], 'Antoinette'] 

the `text` becomes a Moodle [cloze][cloze] question:

    John Smith has 3 children: Antoinette, 10.2, Lawrence, 12.9, Sebastian, 9.7. The mean age of the children is $$\mu$$ = {1:NUMERICAL:=10.9:0.55}. The eldest child is : {1:MULTICHOICE: Antoinette ~= Lawrence ~ Sebastian}. The child with the longest name is {1:SHORTANSWER:~=Antoinette}.


The `text` consists of:
1. Simple text. The text included between `$$...$$` is for mathematical expressions and symbols in LaTeX (an online [LaTeX editor][LatexEd] can be used).

2. Formated text for input data, e.g. `%(name_1)s, %(age_1).1f`. The inputs (i.e. given data for the problem) are written as variables using the mapping from `insert_variables(x, y, text)` function, e.g. `%(age_1).1f`.  The variables inserted in the text are in [% string formatter][str_format], e.g. `%(age_1).1f` is variable `age_1`of format `.1f` (float with one digit after the decimal point).

3. Formated text for the embedded answers in the quiz, included between curled braces `{}`.

*Note:* If in [% string formatter][str_format] the [width][width] of the [field][field] is larger than that needed by the number, then spaces are added. These spaces are not accepted by Moodle; therefore they need to be avoided. For example, if a = 1.3333, use %(a).1f (which yields "1.3") instead of %(a)4.1f (which yields "_ _ 1.3").


|Code|Explanation|
|----|-----------|
|` text = `| String that contains the text of the cloze question with string formatted  variables that were **mapped** to inputs *x* and outputs *y*.|
|` """ `| Start the string.|
|` John Smith has 3 children: `| Simple text.|
|` %(name_1)s `| Input data `name_1`(with value given by `x[0][0]`, see the **mapping**) of type `s` i.e. [string][string].|
|` %(age_1).1f `|Input data `age_1`(with value given by `x[1][0]`, see the **mapping**) of type `.1f` i.e. [float][float] with one digit after the decimal point.|
|... |...|
|` The mean age of the children is: `| Simple text.|
|` $$\\mu$$ = `| Text with LaTeX code for Greek letter μ.|
|` {1:NUMERICAL: ...} `| Numerical embedded answer; explained below.|
|` The eldest child is: `| Simple text.|
|` {1:MULTICHOICE: ...}`| Multichoice embedded answer; explained below.|
|` The child with the longest name is `| Simple text.|
|` {1:SHORTANSWER:...}. `| Embedded short answer; explained below.|
|` """ `| End the string.|

#### Embedded answers

[NUMERICAL][cloze]

`{1:NUMERICAL:=%(mean_age)3.1f:%(err_mean_age)3.2f}`

For variable `y[0] = 10.933333333333332`, it gives:

` {1:NUMERICAL:=10.9:0.55} `

*Note*: In `insert_variables(x, y, text)`, the **mapping** is `mean_age:y[0]` and `err_mean_age:0.05*y[0]`.

|Field| Significance |
|-----|--------------|
|`{`    | Begin of the embedded answer.|
|`1`    | Points awarded to the question.|
|`:NUMERICAL:`| Type of question.|
|=    | Precedes the right answer.|
|%(mean_age)3.1f| Value of the right answer given by the variable `mean_age:y[0]` (see ` problem_text` and the **mapping** of variables). It is of format 3.1f, i.e. float of 3 digits of which 1 is after the decimal point.|
|` : `| Separator|
|` %(err_mean_age)3.2f `| Value of the accepted error given by the variable `err_mean_age:0.05*y[0]` (see ` problem_text` and the **mapping** of variables). It is of format 3.2f, i.e. [float][float] of 3 digits of which 2 are after the decimal point.|
|' } ' | Ends the embedded answer.|


[MULTICHOICE][cloze]


` {1:MULTICHOICE:%(oldest_1)s %(name_1)s
               ~%(oldest_2)s %(name_2)s
               ~%(oldest_3)s %(name_3)s} `

For variables

`x[0] = array(['Antoinette', 'Lawrence', 'Sebastian'])`

and

`y[1] = ['', '=', '']`

we obtain:

` {1:MULTICHOICE: Antoinette ~= Lawrence ~ Sebastian} `.

*Note*: In `insert_variables(x, y, text)`, the mapping is ` "oldest_1": y[1][0], "oldest_2": y[1][1], "oldest_3": y[1][2]`.


|Field| Significance |
|-----|--------------|
|`{`    | Begin of the embedded answer.|
|`1`    | Points awarded to the question.|
|`:MULTICHOICE:`| Type of question.|
|` %(oldest_1)s `| Is the 1st child the oldest? Value given by `oldest_1:y[1][0]`(see `problem_text` and the **mapping** table). It is of type `s` (i.e. `string`) and has the value ` "=" ` if the child is the oldest or ` "" ` otherwise.|
|` %(name_1)s ` | Name of the 1st child. Value given by `"name_1": x[0][0]` (see `problem_text` and the **mapping** table).|
|` ~ `|Separator.|
|` %(oldest_2)s `| Idem, for the 2nd child.|
|` %(name_2)s `|  |
|` ~ `|Separator.|
|` %(oldest_3)s `| Idem, for the 3rd child.|
|` %(name_3)s `| |
|` } ` | End of the embedded answer.|


[SHORTANSWER][cloze]

` {1:SHORTANSWER:~=%(longest_name)s} `

For variable

`y[2] = 'Antoinette'`

we obtain:

`{1:SHORTANSWER:~=Antoinette}`.


|Field| Significance |
|-----|--------------|
|`{`    | Begin of the embedded answer.|
|`1`    | Points awarded to the question.|
|`:SHORTANSWER:`| Type of question.|
|` ~ ` | Separates the answers.|
|` = ` | Precedes the right answer.|
|` } ` | End of the embedded answer.|


### 5. Define the input space

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
    
The inputs are lists that, by cartezian [product](https://docs.python.org/3/library/itertools.html#itertools.product), will form the input space. 
 
They need to be [iterables](https://docs.python.org/3/glossary.html#term-iterable). If only one value is needed, e.g. `age = 3`, than define it as `age = np.array([3])`.


### 6. Generate the quiz in Moodle - cloze format

    question_name = "PyCloze_"          # It will be followed by question number
    quiz = MoodleCloze.generate_quiz(question_name, problem_fun, x_ranges, insert_variables, text) 

The `question_name = "PyCloze_" ` will form the name of the question followed by its number, e.g. `PyCloze_001`. This name will identify each question in Moodle.

`quiz = MoodleCloze.generate_quiz( ... )` uses the function `generate_quiz( ... )` from the module `MoodleClose` to generate the questions for the quiz.

### 7. Save the quiz in an `.xml` file.

    xml_file_name = 'PyCloze00.xml'
    with open(xml_file_name, 'w') as MOODLE_cloze:
        MOODLE_cloze.write(quiz)
 
 The variable ` xml_file_name ` contains the name of the `.xml` file; in this case, the saved file is `PyCloze00.xml`.
 
 
### 8. [Optional] Show the inputs and the outputs of all questions

    test_nr = 0
    for x in product(*x_ranges):
        print("Test: ", test_nr)
        print("Inputs:")
        print(x)
        print("Outputs:")
        print(problem_fun(x), "\n")
        test_nr += 1

Uses [product][itprod] from [itertools][it] to obtain the combinations of inputs. Prints the inputs and the outputs of `problem_fun(x)` for the input space.


[Import_questions]:https://docs.moodle.org/39/en/Import_questions#Importing_questions_from_an_existing_file

[cloze]:https://docs.moodle.org/39/en/Embedded_Answers_(Cloze)_question_type

[old_format]:https://docs.python.org/3/tutorial/inputoutput.html#old-string-formatting

[old_format1]:https://realpython.com/python-string-formatting/#1-old-style-string-formatting-operator

[dict]:https://docs.python.org/3/tutorial/datastructures.html#dictionaries

[str_format]:https://www.techbeamers.com/python-format-string-list-dict/

[width]:https://en.wikipedia.org/wiki/Printf_format_string#Width_field

[field]:https://en.wikipedia.org/wiki/Printf_format_string#Type_field

[string]:https://docs.python.org/3.2/library/string.html#format-specification-mini-language

[float]:https://docs.python.org/3.2/library/string.html#format-specification-mini-language

[itprod]:https://docs.python.org/2/library/itertools.html#itertools.product

[it]:https://docs.python.org/fr/3/library/itertools.html

[LatexEd]:https://latex.codecogs.com/eqneditor/editor.php
