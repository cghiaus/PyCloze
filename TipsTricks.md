# Tips and Tricks

*`.xml`file*

Moodle does not check the .xml file; you can visualize it in a browser.

After a question was answered in Moodle, you cannot delete it but you can correct it. Do not make tests with more than about 25 questions if you want to have a managable number of questions to correct manually.

Always previsualize the test after importing it in Moodle. During the visualzation of the test in Moodle, check the answers of the test in  `Quiz administration / Question bank / Questions : Select category [adequate category]` by pusing the button `Fill in correct responses`. 

*Python code §3 and §4*

In §4, in `text`, use `$$` not `$` to include LaTex code.

In §4 `text`, use two slashes for Greek letters; e.g. `$$\\varepsilon$$` not `$$\varepsilon$$`.

Check the correspondece between variable mapping in  §3 `problem_text =`and  the formatted variables from §4 `test`, e.g. `"name_1": x[0][0]` in `problem_text` in §3 and `%(name_1` in `text` in §4.

You can use Greek letters for variables, e.g. λ2, θ. You can type them in IPython like \lambda followed by [TAB] or copy them from a text editor.
To insert an image from a web site in Moodle Markdown in §4 `text`:

`<img src="http://i.creativecommons.org/l/by/4.0/88x31.png"
alt="CC" width="58" hight="17">`

<img src="http://i.creativecommons.org/l/by/4.0/88x31.png"
alt="CC" width="58" hight="17">
