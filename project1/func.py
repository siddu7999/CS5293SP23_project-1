import sys
import commonregex
import spacy
from nltk import word_tokenize, ne_chunk, pos_tag
import pyap
import re
from nltk.tree import Tree
import os
import glob



redact = '\u2588'

def redacted_names(data):
    s = []
    nlp = spacy.load("en_core_web_sm")
    spacydata = nlp(data)
    for name in spacydata.ents:
        if name.label_ == 'PERSON':
            s.append(name)
            data = data.replace(str(name), redact*len(str(name)))
    return data

def redacted_dates(data):
    extracted_data = commonregex.date.findall(data)
    for date in extracted_data:
        data = data.replace(date, redact)
    return data

def redacted_phones(data):
    extracted_data = commonregex.phone.findall(data)
    for num in extracted_data:
        data = data.replace(num, redact)
    return data

def redacted_genders(data):
    extracted_data = re.findall(r"\b(He|he|She|she|His|his|Her|her|himself|Himself|Herself|herself|mother|brother|sister|son|daughter|uncle|aunt|nephew|niece|male|female|actor|actress|boy|girl|man|woman|Mr.|Ms.)\b", data)
    for genders in extracted_data:
        data = data.replace(genders, redact)
    return data

def redact_address_data(data):
    z=[]
    nlp = spacy.load("en_core_web_sm")
    spacydata = nlp(data)
    for addr in spacydata.ents:
        if addr.label_ == 'GPE':
            z.append(addr)
            data= data.replace(str(addr),redact*len(str(addr)))
    return data
