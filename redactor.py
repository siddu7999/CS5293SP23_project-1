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
    spacyinfo = nlp(data)
    for name in spacyinfo.ents:
        if name.label_ == 'PERSON':
            s.append(name)
            data = data.replace(str(name), redact*len(str(name)))
    stats("names", str(len(s)))
    return data

def redacted_dates(data):
    extracted_data = commonregex.date.findall(data)
    for date in extracted_data:
        data = data.replace(date, redact)
    stats("dates", str(len(extracted_data)))
    return data

def redacted_phones(data):
    extracted_data = commonregex.phone.findall(data)
    for num in extracted_data:
        data = data.replace(num, redact)
    stats("phones", str(len(extracted_data)))
    return data

def redacted_genders(data):
    extracted_data = re.findall(r"\b(He|he|She|she|His|his|Her|her|himself|Himself|Herself|herself|mother|brother|sister|son|daughter|uncle|aunt|nephew|niece|male|female|actor|actress|boy|girl|man|woman|Mr.|Ms.)\b", data)
    for genders in extracted_data:
        data = data.replace(genders, redact)
    stats("genders", str(len(extracted_data)))
    return data

def redact_address_data(data):
    z=[]
    nlp = spacy.load("en_core_web_sm")
    spacydata = nlp(data)
    for addr in spacydata.ents:
        if addr.label_ == 'GPE':
            z.append(addr)
            data= data.replace(str(addr),redact*len(str(addr)))
    stats("address",str(len(z)))
    return data
def stats(name,writtendata):
    statsfile = open(stats_path,"a")
    statsfile.write("\n Redacted " + name + "=" + writtendata )
    statsfile.close()

v = []
v= sys.argv
#print(sys.argv)
in_path = v.index('--input')+1
out_path = v.index('--output')+1
stat_path = v.index('--stats')+1
files= glob.glob(v[in_path])


stats_path=v[stat_path]

if os.path.exists(stats_path):
    os.remove(stats_path)

for file in files:

    data=open(file,'r', encoding='utf').read()
    if len(data) == 0:
        print("File not open")
    elif len(data) != 0:
        print("File opened Successfully")
        statsfile = open(stats_path,"a")
        statsfile.write("\n"+str(file))
        statsfile.close()
        if '--names' in v:
            data = redacted_names(data)
        if '--dates' in v:
            data = redacted_dates(data)
        if '--phones' in v:
            data= redacted_phones(data)
        if '--address' in v:
            data =redact_address_data(data)
        if '--genders' in v:
            data =redacted_genders(data)
        statsfile = open(stats_path,"r")
        filecont=statsfile.read()    
        redacted_path= v[out_path]+str(file)+".redacted"
        if os.path.exists(redacted_path):
            os.remove(redacted_path)
        redacted=open(redacted_path,"w")
        redacted.write(data)
        redacted.close()
