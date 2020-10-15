# Tips and Triks

Moodle does not check the .xml file; you can visualize it in a browser.

In §4, in `text =`, use `$$` not `$` to include LaTex code.

In §4 `text =` (Markdown for Moodle), use two slashes for Greek letters; e.g. `$$\\varepsilon$$` not `$$\varepsilon$$`.

Check the correspondece between variable mapping in  §3 `problem_text =`and  the formatted variables from §4 `test`, e.g. `"name_1": x[0][0]` in `problem_text` in §3 and `%(name_1` in `text` in §4.

You can use Greek letters for variables, e.g. λ2, θ. You can type them in IPython like \lambda followed by [TAB] or copy them from a text editor.

Do not make tests with more than about 50 questions if you are not **sure** that the test is correct. If there is a mistake in the algorithm, in Moodle you may change manually the results for each question; it would be difficult to do this for more than about 50 questions.

Always previsualize the test after importing it in Moodle. During the visualzation of the test in Moodle, check the answers of the test in  `Quiz administration / Question bank / Questions : Select category [adequate category]` by pusing the button `Fill in correct responses`. 