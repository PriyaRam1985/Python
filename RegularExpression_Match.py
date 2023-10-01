
#Matching: Checking if a string matches a pattern.
import re
pattern = r"ab*c"
text = "abc, ac, abbbc"
match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
