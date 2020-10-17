# Tips and Tricks

- author: [Christian Ghiaus](mailto:cghiaus@gmail.com)
- institution: [INSA Lyon](https://www.insa-lyon.fr), France
- date: 2020

## `.xml`file

Moodle does not check the .xml file; you can visualize it in a browser.

After a question was answered in Moodle, you cannot delete it but you can correct it. Do not make tests with more than about 25 questions if you want to have a managable number of questions to correct manually.

Always previsualize the test after importing it in Moodle. During the visualzation of the test in Moodle, check the answers of the test in  `Quiz administration / Question bank / Questions : Select category [adequate category]` by pusing the button `Fill in correct responses`. 

## Quiz text (§3 and §4 in PyCloze__.py file)

Check the correspondece between variable mapping in  §3 `problem_text`and the formatted variables from §4 `test`, e.g. in PyCloze00.py, between `"name_1": x[0][0]` in `problem_text` in §3 and `%(name_1)s` in `text` in §4.

In §4, in `text`, use `$$` not `$` to include LaTeX code.

In §4, in `text`, use two slashes for Greek letters; e.g. `$$\\varepsilon$$` not `$$\varepsilon$$`.

You can use Greek letters for variables, e.g. λ2, θ. Type them in IPython like \lambda followed by [TAB] or copy them from a text editor.

To insert an image from a web site in Moodle Markdown in §4 `text` write:

`<img src="http://i.creativecommons.org/l/by/4.0/88x31.png"
alt="CC" width="88" hight="31">`

<img src="http://i.creativecommons.org/l/by/4.0/88x31.png"
alt="CC" width="58" hight="17">

## Grades, marks and points

A quiz is composed of a number of questions. Each question is composed of a number of answers. A quiz has a grade, a question has a mark, and an answer has a number of points.

### Grades

A quiz has a **maximum grade**, e.g. 6, 10 or 20. 

To set the maximum grade of a quiz,
- in `Home / My courses / ... My course`. select the quiz.
- in `Administration / Quiz Administration / Edit quiz: Maximum grade`, type 6, 10 or 20[CR], and `Save`.

### Marks

Each question in the quiz has a number of **marks** that add up to the `Total of marks` of the quiz.
To set the maximum marks for each question in the quiz,
- in `Home / My courses / ... My course`. select the quiz.
- in `Administration / Edit quiz`, type the marks for each question.

### Points

Each answer in a question has a number of **points** awarded. To check the number of points for a question,
- in `Home / My courses / ... My course`, select the quiz.
- in `Administration / Edit quiz`, push the magnifier button on the line of the question.
- the number of points is shown after `Marked out of`.

or
- in `Home / My courses / ... My course`, select the quiz.
- in `Administration / Quiz Administration / Question bank / Questions: Select a category`.
- in `Edit: Preview`, the number of points is shown after `Marked out of`.

The points awarded for a correct answer are indicated in the embedded answer of the cloze question, e.g. {1:NUMERICAL:=20:2} means 1 point for the numerical answer 20 with an error of +/- 2 (see *§4 Write a text of the cloze question in Markdown* in [Tutorial_py2xml.md](Tutorial_py2xml.md)). The points can be only integers.
