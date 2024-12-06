"""
This code contains some bugs and some errors.  
Find them and fix them.  
When you are done the program will print a message.
Write the message at the bottom of the code before submission
"""
def extract_and_rearrange(string): #Fixed function name typo(missing "def") and incorrect name
    str_1 = "".join(reversed(string[0:4])).capitalize() #Fixed reversed and split logic,corrected slicing, and capitalization
    str_2 = "".join(string[6:13].split('ro')) #Fixed split method typo from 'splt' to 'split'
    str_3 = "".join("".join(reversed(string[14:20])).split(string[17])) #Fixed variable name and method chaining, corrected slicing and list handling
    str_4 = "".join(string[21:29].split(string[23:28])) #Fixed slicing and string handing

    return str_1 + " " + str_2 + " " + str_3 + " " + str_4 #fixed syntax error: missed + before str_4

def ultra_extract_and_rearrange(string): #Fixed name typo,added : at the end of def
    first_transform = extract_and_rearrange(string) #Fixed syntax error: 'extrct' to 'extract'
    return first_transform

print(ultra_extract_and_rearrange("egthb quirock nwoGrb forijmpxv")) #Fixed the call of function and remove extra quotes
#Message: Htge quick brown fox