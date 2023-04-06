# CS5293SP23-Project0

The main aim of this project is to use Python and Text Analytics concepts to redact sensitive data such as names, gender, dates, mobile numbers, and postal addresses by building a system that takes the text documents as input and then detects and redacts the sensitive entities. This makes sure that the data in the output file(with .redacted extension) has no confidential data. 
#Used Packages:
sys (import sys)
commonregex (import commonregex)
spacy (import spacy)
nltk
pyap (import pyap)
re (import re)
os (import os)
glob (import glob)
#How to install:
pipenv install nltk (To install the Natural Language Toolkit (NLTK) package within a pipenv virtual environment.)
sudo apt install python3-nltk
pipenv install commonregex (used to install the CommonRegex package within a pipenv virtual environment).
pipenv install spacy (used to install the spacy package within a pipenv virtual environment.)
python -m spacy download en_core_web_sm (used to download a pre-trained English language model for spacy).
#How to run:
The following command is used to run the redactor code:
pipenv run python redactor.py --input '*.txt' --names --dates --phones --genders --address --output 'project1/files/' --stats stderr
The following command is used to run the test codes:
pipenv run python -m pytest
#Functions:
##redacted_names(data):
In order to store the detected names, the function first constructs an empty list s. Then, it imports the spacy English language model using en_core_web_sm and uses it to extract named entities from the incoming string data.
The replace function is used to replace each instance of a named entity in the input string data with an asterisk of the same length for each named entity that is recognized as a person (i.e., possessing the label "PERSON"). Redaction is done by multiplying the string "redact" by the length of the string for the recognized entity. The function calls another function stats to count the number of identified names in the s list after processing all named entities. After that, the updated string data is returned.
##redacted_dates(data):
The redacted dates function accepts a string of data as input, and then extracts all of the dates from the text using a regular expression from the commonregex library. It then substitutes a redacted value for each extracted date.
The function calls a stats function after all the dates have been redacted in order to capture some statistics regarding the redaction procedure. The stats function is used in this instance to keep track of how many dates were censored. The function then returns the redacted string data as output.
##redacted_phones(data):
A string of data is passed into the redacted_phones function, and all of the phone numbers are extracted using a regular expression from the commonregex package. Then, a redacted value is used to replace each extracted phone number. Finally, the redacted string data is returned as output from the function.
##redacted_genders(data):
Using a regular expression, the redacted genders function takes a string of data as input and extracts words that frequently refer to gender-specific pronouns, titles, or familial relationships. It specifically searches for the phrases "He", "She", "His", "Her", "mother", "brother", "sister", "son", "daughter", "uncle", "aunt", "nephew", "niece", "male", "female", "actor", "actress", "boy", "girl", "man", "woman", "Mr.", and "Ms.". Following their extraction, the function substitutes each of these words with a redacted value. Then the stats function is called an Finally, the redacted string data is returned as output from the function.
##redact_address_data(data):
The spaCy library is used by the redact address data function to extract all geographical entities (GPE) from a string of data that is provided as input. GPE stands for geopolitical entities, which include states, cities, and nations.
The function substitutes a redacted value for each GPE entity it discovers (the value of the redact variable is not shown in the code provided). A string of asterisks (*) with the same length as the original value serves as the redacted value. Then the stats function is called to record the statistics and finally, the redacted string data is returned as output from the function.
##stats(name, written data):
The script iterates through each input file, reading each one and determining whether or not it is empty. If the file is not empty, it writes the file name to the statistics file and, using the command-line options, applies several redaction functions to the file's contents. The script reads the contents of the statistics file when redaction is finished and saves them in a variable named "filecount." Then it generates a new output file with the name of the input file and the extension ".redacted".

#TEST FUNCTIONS:
##def test_redacted_names():
This test case checks if the redacted_names() function correctly replaces the name in the input string with black boxes, thereby protecting the privacy of the person whose name is mentioned. If the test passes, it indicates that the function is working correctly for this specific input case.
##def test_redacted_dates():
The test function generates a sample text string with a date and an anticipated output string that preserves the time but redacts the date using black boxes (). The redacted dates() function's output is compared to the expected output string using the assert statement in the test function. The test will fail if the function's output differs from what was anticipated.
##def test_redacted_genders():
This test case checks if the redacted_genders() function correctly replaces gender pronouns in the input string with block characters. If the test passes, it indicates that the function is working correctly for this specific input case.
##def test_redact_address_data():
The address is covered up by full block characters in the expected output string and the sample text string produced by the test function. The assert statement in the test function compares the output of the redact address data() method to the expected output string. If the function's output deviates from what was expected, the test will fail.
##TestRedaction(unittest.TestCase):
This code defines a unit test class called TestRedaction that inherits from the unittest.TestCase class.Within the TestRedaction class, there is a single test function called test_stats() that tests a function that is not specified in this code snippet. Overall, this code provides a skeleton for creating a unit test class and test functions for a specific function that needs to be tested.
#Format of the stats output file:
The output file of the stats function gives the number of each redacted entities. The    format of the output file is as follows :
Redacted names =
Redacted dates =
Redacted genders =
Redacted phones =
Redacted addresses =


#Bugs and Assumptions :
The redacted_names() function uses spacy's named entity recognition (NER) to identify names in the input data. However, NER is not perfect and may miss or incorrectly identify names.
The stats() function assumes that the stats file has already been created and can be appended to. If the stats file does not exist, this function will not work properly.
The code assumes that the input files are readable and non-empty. If an input file is not readable or empty, this may cause errors in reading the data. And it also assumes that the output directory exists and is writable. If the output directory does not exist or is not writable, the code will not be able to write the redacted data to the output file.
The code assumes that there are no errors in the implementation of the glob module for finding input files. If there are errors in this implementation, the code may not find the correct input files to process.

