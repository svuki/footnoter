# footnoter
This programs allows for easy hyperlinked footnotes in markdown files. 
The usage is 
```
python footnoter SOURCE-FILE TARGET-FILENAME
```

Be default the footnote pattern is @@footnote [footnote text here]@@. The program will extract the footnote text out, replace it with a hyperlinked superscript to the fotnote text which will be placed at the bottom of the document. " 
## Examples

Passed the file:

```code MARKDOWN
# Title

Here is a line @@footnote And this is its footnote.@@
```

The output is:

```code MARKDOWN
# Title

Here is a line <a href="#footnote1"><sup id="super1">0</sup></a>
<p id="footnote1"> <a href="#super1"><sup>0</sup></a>And this is its footnote.</p>
```


