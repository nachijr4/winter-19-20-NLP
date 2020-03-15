import spacy

model = spacy.load('en_core_web_sm')

text = '''It began as the Computing, Tabulating & Recording Company (C-T-R) founded by Herman Hollerith in the late 1800s. Their first large contract was to provide tabulating equipment for the tabulation 
and analysis of the 1890 US census. 
The company grew quickly and, in the early 1920s the name was changed to IBM.'''

doc = model(text)
