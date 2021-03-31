# Create questions in Python and save them in a Moodle .xml file

Author: [Christian Ghiaus](mailto:cghiaus@gmail.com)

[INSA Lyon](https://www.insa-lyon.fr), France, 18/04/2021

This tutorial shows how to create a Python code to obtain questions in `.xml` file that can be imported in a question bank Moodle. You can visualize `.xml` files by opening them within a browser.

Requirements:

1. [Python 3](https://www.python.org/download/releases/3.0/).
2. The file `PyClz00.py`.

______________________________________
**Typical structure of Pyton code** to generate cloze questions in `.xml` file:
1. Import modules.
2. Create a function which solves the problem.
3. Define the input space.
4. Write the text of the cloze question in Markdown.
5. Generate the quiz in *Moodle - cloze* format and save `.xml` file.
6. [Optional] Show the inputs and outputs of all tests.

______________________________________

This structure is discussed by going through a simple example, `PyClz00.py`. Examples of other tests are given in `PyClz01.py` and `PyClz02.py`.

## `PyClz00.py`: walk through a simple example

The  aim is to obtain a quiz with embedded input data and answers that looks like below:

______________________________________

John Smith has 3 children: **name_1**, age **age_1**, **name_2**, age **age_2**, **name_3**,age **age_3**.

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

Six (2 name_list x 3 age_list) combinations of inputs are obtained, which corespond to six quizes.

For the answers, we want:

|Answer     |  Type      | Contents                    |
|-----------|------------|-----------------------------|
|μ =`____`  | NUMERICAL  |numerical value ±0.5       |
|`________↕`| MULTICHOICE|choose one out of three names|
|`_________`| SHORTANSWER|a name                       |

For a quick view of the quiz, [import][Import_questions] the questions in Moodle from the file `PyClz00.xml` (see [Tutorial_xml2moodle.md](Tutorial_xml2moodle.md) for how to make a test in Moodle and import questions in `.xml` format).  

## Description of Python code

### 1. Import modules

    import numpy as np
    import MdlClz


You need to [import](https://docs.python.org/3/reference/import.html) at least `MdlClz`. Typically, you will also need to import [NumPy](https://numpy.org/doc/).


### 2. Create a function which solves the problem

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

The inputs `x` and the outputs `y` are [dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries). The inputs `x`are given in the dictionary `x_ranges` (see the next section).

*Note*: Python accepts [Unicode](https://en.wikipedia.org/wiki/List_of_Unicode_characters) characters. If you use [Spyder](https://www.spyder-ide.org) IDE, you can type Greek characters in IPython console as \\`GreekLetter` `(Tab ↹)`. For example, \alpha `(Tab ↹)` will give α.

### 3. Define the input space
  
    x_ranges = {'name': np.array([['Antoinette', 'Lawrence', 'Sebastian'],
                                  ['Anastasia', 'Catherine', 'Quentin']]),
                'age': np.array([[10.2, 12.9, 9.7],
                                 [23.4, 12.5, 17.2],
                                 [4.9, 14.1, 8.5]])}
    
Here, there are two lists of names (with three names each) and three lists of ages (with three values each). The cartezian [product](https://docs.python.org/3/library/itertools.html#itertools.product) of inputs will form the input space. In this case, there will be *2 name_list X 3 age_list = 6 questions*.

### 4. Write the text of the cloze question in [Markdown](https://www.markdownguide.org)

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

By inserting the variables `name` and `age` (the inputs of the `problem_fun(x)`), and `mean_age`, `oldest` and `longest_name` (the outputs of the `problem_fun(x)`), the `text` becomes a Moodle [cloze][cloze] question. For our example (see `PyClz00.xml`):

            <![CDATA[
    John Smith has 3 children:
    Antoinette, age 23.4,
    Lawrence, age 12.5,
    Sebastian, age 17.2.

    The mean age of the children is
    $$\mu$$ = {1:NUMERICAL:=17.7:0.5}.

    The eldest child is :
    {1:MULTICHOICE:= Antoinette
                   ~ Lawrence
                   ~ Sebastian}.
                   
    The child with the longest name is {1:SHORTANSWER:~=Antoinette}.
            ]]>


The `text` consists of:
1. Simple text containing mathematical expressions and symbols in LaTeX included between `$$...$$` (an online [LaTeX editor][LatexEd] can be used). For example:


    The mean age of the children is $$\\mu$$ =

*Note*: The control charatcer `\\` in `text` will become `\` in `.xml` file.

2. Formated text for input data, e.g.


    {name[0]:s}, age {age[0]:.1f},
    {name[1]:s}, age {age[1]:.1f},
    
 

The variables inserted in the text are in the "new style" [string formating][str_format] (`str.format`), e.g. `{name[0]:s}` is the variable `name[0]` of format string and `{age[0]:.1f}` is the variable `age[0]`of format `.1f` (float with one digit after the decimal point).

3. Formated text for the embedded answers in the quiz, included between curled braces `{{}}`, e.g.:


    $$\\mu$$ = {{1:NUMERICAL:={mean_age:.1f}:0.5}} (±0.5).


*Note:* If in [string formating][str_format] the [width][width] of the [field][field] is larger than that needed by the number, then spaces are added. These spaces are not accepted by Moodle; therefore they need to be avoided. For example, if a = 1.3333, use {a:.1f} (which yields "1.3") instead of {a:5.1f} (which yields "_ _ 1.3").


|Code|Explanation|
|----|-----------|
|`text =`| String that contains the text of the cloze question with string formatted  variables.|
|`"""`| Start the string containing  the text of the problem.|
|`John Smith has 3 children:`| Simple text.|
|`{name[0]:s}`| Input data `name[0]` of type `s`, i.e. [string][string].|
|`{age[0]:.1f}`|Input data `age[0]` of type `.1f` i.e. [float][float] with one digit after the decimal point.|
|... |...|
|`The mean age of the children is:`| Simple text.|
|`$$\\mu$$ =`| Text with LaTeX code for Greek letter μ. Control character `\` needs to be doubled.|
|`{{1:NUMERICAL:=...}}`| Numerical embedded answer; explained below. Control characters `{` and `}` need to be doubled.|
|`The eldest child is: `| Simple text.|
|`{{1:MULTICHOICE: ...}}`| Multichoice embedded answer; explained below.|
|`The child with the longest name is`| Simple text.|
|`{{1:SHORTANSWER:...}}. `| Embedded short answer; explained below.|
|` """ `| End the string.|

#### Embedded answers

[NUMERICAL][cloze]

`{{1:NUMERICAL:={mean_age:.1f}:0.5}}`

Variable `y.['mean_age']= 10.933333333333332` in `text = """ ... """` gives `{1:NUMERICAL:=10.9:0.5}` in `PyClz.xml` file.


|Field| Significance |
|-----|--------------|
|`{{`    | Begin of the embedded answer. Note that `{{` from `text = """..."""` will be transformed in `{` in the `.xml` file.|
|`1`    | Points awarded to the question. Can be only integers, e.g. 1, 3. See [Tips&Tricks](Tips&Tricks.md) on *Grades, marks and points*.|
|`:NUMERICAL:`| Type of question.|
|=    | Precedes the correct answer.|
|{mean_age:.1f}| Value of the right answer given by the variable `y.['mean_age']`. It is of format `.1f`, i.e. float with one decimal.|
|` : `| Separator|
|`0.5`| Value of the accepted error.|
|'}}' | Ends the embedded answer. Note that `}}` from `text = """..."""` will be transformed in `}` in the `.xml` file.|


[MULTICHOICE][cloze]


`{{1:MULTICHOICE:{oldest[0]:s} {name[0]:s}
               ~{oldest[1]:s} {name[1]:s}
               ~{oldest[2]:s} {name[2]:s}}}. `

For variables

    x['name'] = array(['Antoinette', 'Lawrence', 'Sebastian'], , dtype='<U10')
    x['age'] = array([10.2, 12.9,  9.7])
and

    y['oldest'] = ['', '=', '']


in `PyClz.xml` file we obtain that `Lawrence` is the oldest in the list (shown by the `=` sign in front of his name):

` {1:MULTICHOICE: Antoinette ~= Lawrence ~ Sebastian} `.


|Field| Significance |
|-----|--------------|
|`{{`    | Begin of the embedded answer.|
|`1`    | Points awarded to the question. Can be only integers, e.g. 1, 3. See [Tips&Tricks](Tips&Tricks.md) on *Grades, marks and points*.|
|`:MULTICHOICE:`| Type of question.|
|`{oldest[0]:s}`| Is the 1st child the oldest? It is of type `s` (i.e. `string`) and has the value ` "=" ` if the child is the oldest or ` "" ` otherwise.|
|`{name[0]:s` | Name of the 1st child.|
|` ~ `|Separator.|
|`{oldest[1]:s}`| Idem, for the 2nd child.|
|`{name[1]:s`|  |
|` ~ `|Separator.|
|`{oldest[2]:s}`| Idem, for the 3rd child.|
|`{name[2]:s}`| |
|`}}` | End of the embedded answer.|


[SHORTANSWER][cloze]

    {{1:SHORTANSWER:~={longest_name:s}}}

For variable `y['longest_name'] = 'Antoinette'`, in `PyClz01.xml` file we otain `{1:SHORTANSWER:~=Antoinette}`.



|Field| Significance |
|-----|--------------|
|`{{` | Begin of the embedded answer.|
|`1`  | Points awarded to the question. Can be only integers, e.g. 1, 3. See [Tips&Tricks](Tips&Tricks.md) on *Grades, marks and points*.|
|`:SHORTANSWER:`| Type of question.|
|` ~ `| Separates the answers.|
|` = `| Precedes the right answer.|
|` }}`| End of the embedded answer.|

**Note**: See [Tips&Tricks](Tips&Tricks.md) for a discussion on grades, marks and points in Moodle. 


### 5. Generate the quiz in *Moodle - cloze* format

    question_name = "PyClz00"          # will be followed by the question number
    quiz = MdlClz.generate_quiz(question_name, problem_fun, x_ranges, text)


The `question_name = "PyClz_" ` will generate the name of the question followed by its number, e.g. `PyCloze_001`. This name will identify each question in Moodle.

`quiz = MdlClz.generate_quiz(...)` uses the function `generate_quiz(...)` from the module `MdlClz` to generate the questions for the quiz.


### 6. [Optional] Show the inputs and the outputs of all questions

    test_nr = 0
    for x in MdlClz.cprod(x_ranges):
        print("Test: ", test_nr)
        print("Inputs:")
        print(x)
        print("Outputs:")
        print(problem_fun(x), "\n")
        test_nr += 1

The function `MdlClz.cprod` uses [product][itprod] from [itertools][it] to obtain the combinations of inputs. Prints the inputs and the outputs of `problem_fun(x)` for the input space.


[Import_questions]:https://docs.moodle.org/39/en/Import_questions#Importing_questions_from_an_existing_file

[cloze]:https://docs.moodle.org/39/en/Embedded_Answers_(Cloze)_question_type

[old_format]:https://docs.python.org/3/tutorial/inputoutput.html#old-string-formatting

[old_format1]:https://realpython.com/python-string-formatting/#1-old-style-string-formatting-operator

[dict]:https://docs.python.org/3/tutorial/datastructures.html#dictionaries

[str_format]:https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat

[width]:https://en.wikipedia.org/wiki/Printf_format_string#Width_field

[field]:https://en.wikipedia.org/wiki/Printf_format_string#Type_field

[string]:https://docs.python.org/3.2/library/string.html#format-specification-mini-language

[float]:https://docs.python.org/3.2/library/string.html#format-specification-mini-language

[itprod]:https://docs.python.org/2/library/itertools.html#itertools.product

[it]:https://docs.python.org/fr/3/library/itertools.html

[LatexEd]:https://latex.codecogs.com/eqneditor/editor.php
