#strdesc="This is a 40-year-old male with rectal pain, rectal bleeding, and some left-sided lower abdominal pain. The colonoscopy procedure and the risks, not limited to bleeding, perforation, infection, side effects from medication, need for surgery, etc., and were fully explained to the patient. An informed consent was taken. Moderate-sized, internal hemorrhoids. Mild diverticulosis."
#strdesc="Diagnosis of streptococcal pneumoniae confirmed"
import nltk
def codemapfunc(strdesc):
    if strdesc !="":
        data = nltk.word_tokenize(strdesc)
        tagged = nltk.pos_tag(data)
        extractcode=""
        for subtree in filter(lambda x: x[1]  in ('NN','NNP','JJ','JJR'), tagged):
           if subtree[0].lower() not in("diagnosis","other", "due"):
                if extractcode != "": 
                 extractcode = extractcode + "|" + "(\\b"+ subtree[0] + "\\b)"
                else:
                 extractcode = "(\\b"+ subtree[0] + "\\b)"
    return extractcode

import re
def KeywordHighlight(strdesc):
    liststrdes2=[]
    strdes1=codemapfunc(strdesc)
    regex = re.compile(strdes1, re.I)

    #(\bstreptococcal\b)|(\bpneumoniae\b) 
    i = 0; output = "<html>"
    for m in regex.finditer(strdesc):
        output += "".join([strdesc[i:m.start()],
                           "<strong><span style='color:green'>",
                           strdesc[m.start():m.end()],
                           "</span></strong>"])
        i = m.end()
    #print ("".join([output, strdesc[m.end():], "</html>"]))
    return  "".join([output, strdesc[m.end():], "</html>"])    
#KeywordHighlight(strdesc)
