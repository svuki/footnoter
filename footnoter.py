#!/usr/bin/python

import re
import sys

footnotes = []
footnote_template = "<p id=\"footnote{0}\"> <a href=\"#super{0}\"><sup>{0}</sup></a>{1}</p>"
superscript_template = "<a href=\"#footnote{0}\"><sup id=\"super{0}\">{0}</sup></a>"
footnote_regex = r"@@(.*?)@@"

def generate_footnote (contents, n):
    """Returns the foonote HTML for the Nth footnote."""
    return str.format(footnote_template, n, contents)

def generate_superscript (n):
    """Returns the superscript HTML for the Nth footnote."""
    return str.format (superscript_template, n)

def extract_footnotes( line ):
    """Replaces all matches of FOOTNOTE_REGEX with superscript HTML. Stores the
    footnote in FOOTNOTES."""
    global footnotes
    match = re.search(footnote_regex, line)
    if match:
        #store the text of the foonote
        footnotes += match.groups(0)
        new_line = re.sub(footnote_regex, generate_superscript(len (footnotes)), line)
        #recurse in case the line has multiple footnotes
        return extract_footnotes(new_line)
    else:
        return line

### Begin Script:


if (len(sys.argv) == 3):
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
else:
    print("""Usage: footnoter [INPUTE FILE] [OUTPUT FILE]""")
    sys.exit(2)

with open(input_filename, 'r') as input_f, open(output_filename, 'w') as output_f:
          for line in input_f:
              ret = extract_footnotes(line)
              output_f.write(extract_footnotes(ret))
          #Now write out the footnotes
          for i in [generate_footnote(footnotes[x], x + 1) for x in range(len (footnotes))]:
              output_f.write(i)
sys.exit(0)
