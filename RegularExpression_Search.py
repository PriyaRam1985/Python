
#Using Regular Expression with Search
import re
pattern = r"\d{3}-\d{2}-\d{4}"  
text = "My SSN is 123-45-6789."
match = re.search(pattern, text)
if match:
    print("SSN found:", match.group())
