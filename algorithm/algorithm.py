text=raw_input("Enter Text: ")

pattern=raw_input("Enter Pattern: ")

text=text.lower()
pattern=pattern.lower()

tlen=len(text)
plen=len(pattern)

i=0

if(tlen==plen):
    if(text[i]==pattern[i] and text[plen-1]==pattern[plen-1]):
        match=True
        for x in range(1,plen-1):
            if(text[x]!=pattern[x]):
                match=False
        if(match==True):
            print("match")
        else:
            print("not matched")
    else:
        print("not matched")
    
else:
    print("not matched")
    