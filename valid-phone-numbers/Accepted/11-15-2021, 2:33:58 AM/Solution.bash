// https://leetcode.com/problems/valid-phone-numbers

# Read from the file file.txt and output all valid phone numbers to stdout.
cat file.txt | grep -P '(^\(\d{3}\) \d{3}-\d{4}$)|(^\d{3}-\d{3}-\d{4}$)' 
