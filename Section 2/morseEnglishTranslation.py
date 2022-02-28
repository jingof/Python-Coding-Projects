def Solution(morseToEnglish,textToTranslate):

    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
    if morseToEnglish == False:
        newList = [morse[ord(c.upper())-ord('A')] if c.isalpha() else " " if c == " " else ".-.-.-" if c == '.' else "invalid" for c in textToTranslate]
        if "invalid" in newList:
                return "Invalid Morse Code Or Spacing"
        value = " ".join(newList)
        return value
    else:     
        textToTranslate = textToTranslate.split("   ")
        string = ""
        for word in textToTranslate:
            wordL = word.split(" ")
            
            for l in wordL:
                if l in morse:
                    ind = morse.index(l)
                    c = letters[ind]
                    string+= c.lower()
                elif l == ".-.-.-":
                    string+= '.'
                else:
                    return "Invalid Morse Code Or Spacing"
            string += " "
        print(string)
        return string



        
        
    pass

#string = "- …. . .-- .. --.. .- .-. -.. --.- ..- .. -.-. -.- .-.. -.-- .--- .. -. -..- . -.. - …. . --. -. --- -- . … -… . ..-. --- .-. . - …. . -.-- …- .- .--. --- .-. .. --.. . -.. .-.-.-"
string = "This is it."
#Solution(False,string)
print(len(string))

string2 = "- .... .   .-- .. --.. .- .-. -..   --.- ..- .. -.-. -.- .-.. -.--   .--- .. -. -..- . -..   - .... .   --. -. --- -- . ...   -... . ..-. --- .-. .   - .... . -.--   ...- .- .--. --- .-. .. --.. . -.. .-.-.-"
Solution(True,string2)
#the wizard quickly jinxed the gnomes before they vaporized.