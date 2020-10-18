# Moodle quiz with cloze questions generated in Python

Author: [Christian Ghiaus](mailto:cghiaus@gmail.com)

[INSA Lyon](https://www.insa-lyon.fr), France, 2020

This tutorial shows how to create a quiz in [Moodle 3](https://docs.moodle.org/39/en/Main_page) with embedded answers ([cloze][cloze] question) imported as a [random question][random_q] from an `.xml` file generated in [Python 3](https://www.python.org).

Requirements: 
1. Acces to Moodle in editing mode.
2. Availability of the file `PyCloze00.xml`.

______________________________________
**Typical workflow:**
1. Create the questions in Python and save them in an `.xml` file.
2. Create and set up a **quiz** in Moodle.
3. Create a **category** for the specific **question** of the **quiz** in the **question bank**.
4. Import the `.xml` file into the **question bank** in the **category** of the quiz corresponding to the type of question.
5. **Preview** the questions of a **category** in the **question bank**. If there are errors in the questions:
    - **Delete** the questions from the **category**.
    - Correct the questions in Python (see [Tutorial_py2xml.md](Tutorial_py2xml.md)). 
    - Go to step 4.
6. **Add a random question** to the quiz.
7. **Preview** an existing quiz.
______________________________________

In the following, the Moodle commands are in **bold** and the context in Moodle is `highlighted`. The actions are in `My Course` in the context `Home / My courses / ... My course`.

## 1. Create the questions in Python and save them in an .xml file

See [Tutorial_py2xml.md](Tutorial_py2xml.md) to create the questions in Python and save them as `PyCloze00.xml` file. For this tutorial, use the file `PyCloze00.xml` as provided.

## 2. Create and set up a quiz in Moodle

`Home / My courses / ... My course`

- **Turn editing on**.
- **Add an actvity or resource**.
- Chose **quiz**.
- **Name** the quiz *PyCloze*, select the [quiz settings](https://docs.moodle.org/39/en/Quiz_settings) (**Timing**, **Grade**, etc.), then **Save and return to course**.

## 3. Create a category for the quiz in the question bank

`Home / My courses / ... My course`

- Select the quiz *PyCloze*.

`Home / My courses / ... My course/PyCloze`

- Select **Question bank / Categories**

`Home / My courses / ... My course / PyCloze / Question bank / Categories`

- **Add category** **Name**: *PyCloze random questions* for **Parent category** *Default for PyCloze*.
- Push **Add category** button.


## 4. Import the .xml file into the question bank in the corresponding category

From `My course`:

`Home / My courses / ... My course`

- Select the quiz *PyCloze*, **Question bank**, **[Import][Import_mdl]**.
- In **File format**, chose **Moodle XML format**.
- Attention: in **General**, select **Import category** *PyCloze random questions*.
- In **Import questions from file**, drag & drop the file `PyCloze00.xml`, then push **Import** button.


`Home / My courses / ... My course / General / PyCloze / Question bank / Import`

The imported questions are displayed. At the bottom of the page, push **Continue** button.


## 5. Preview a question in the question bank

`Home / My courses / ... My course / General / PyCloze / Question bank / Questions`

- **Select the category**: *PyCloze random questions (6)*.
- Under **Actions**, push **Edit** and select **Preview**.
- Push **Fill in the correct responses** button and check the view of the question.
- Push **Close preview** button.

### Delete imported questions

`Home / My courses / ... My course / General / PyCloze / Question bank / Questions`

- **Select a category:** *PyCloze random questions (6)*.
- Tick the box next to **Question name / ID number** to select all questions.
- Push **Delete** button at the bottom of the list of questions.


### Correct the questions in Python

See the [Tutorial_py2xml.md](Tutorial_py2xml.md) to correct the questions in Python and save them as `PyCloze00.xml`.


## 6. Add a random question from the question bank to the quiz

`Home / My courses / ... My course / General / PyCloze`

- **Edit quiz**.

`Home / My courses / ... My course / General / PyCloze / Edit quiz`

- **Add** and select **A random question**.
- Select **Category** *PyCloze random questions (6)*.
- Push **Add random question** button.
- You can preview the questions by pushing **the magnifying glass**.
- Select the mark for the question and the grade for the quiz. See [TipsTricks](TipsTricks.md) on grades, marks and points in Moodle. 
- **Save** the quiz.


## 7. Preview an existing quiz

`Home / My courses / ... My course`

- Chose the test *PyCloze*.
- Push **Preview quiz now** button.

[cloze]:https://docs.moodle.org/39/en/Embedded_Answers_(Cloze)_question_type

[random_q]:https://docs.moodle.org/39/en/Random_question_type

[Import_mdl]:https://docs.moodle.org/39/en/Import_questions#Importing_questions_from_an_existing_file

