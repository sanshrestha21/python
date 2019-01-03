text="welcome"
pattern="welcame"

tlen=len(text)
plen=len(pattern)

i=0

if(tlen==plen):
    if(text[i]==pattern[i] and text[plen-1]==pattern[plen-1]):
        print ("match")
    else:
        print ("not matched")