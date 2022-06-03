
word1 = str(input('Correct word: ')).lower()          #correct word
word2 = str(input('Word to be examined: ')).lower()   #correct?

def function(fword1=str(), fword2=str(), fisLonger=bool()): #function
    match = str('')
    differ = str('')

    index = int(-1)
    j = int()
    
    isMatch = bool()
    foundCharMatch = bool()

    for i in range(0,len(fword1)):
        foundCharMatch = False
        j = index
        
        while foundCharMatch == False and  j<len(fword2)-1:
            j = j+1
            
            if fword1[i] == fword2[j]:          #if two letter matches in the words
                match = match+fword2[j]
                foundCharMatch = True
                index = j
                
            else:
                differ = differ+fword2[j]+',' #forgot/plus characters before find the word
                            
        if foundCharMatch == False:           #if didn't find the next letter
            isMatch = False
            break

    index = index+1 
    j = index 
    
    while len(fword2) > index:               #forgot/plus characters after find the word
        differ = differ+fword2[j]+','
        index = index+1
        j = j+1
    
    if fword1 == match:
        isMatch = True
        
    print()
    
    if fisLonger == True and isMatch == True and len(differ)/2 < len(fword1):
        print('These words are maybe the same: ' + fword1)
        if len(differ) == 2:                                              #one wrong character
            print("But you don't need to this character: " + differ[:-1])   
        else:                                                             #more wrong characters
            print("But you don't need to these characters: " + differ[:-1])
            
    elif fisLonger == False and isMatch == True and len(differ)/2 < len(fword1):
        print('These words are maybe the same: ' + fword2)
        if len(differ) == 2:                                              #one character is missing
            print('But you forgot this character: ' + differ[:-1])   
        else:                                                             #more characters are missing
            print('But you forgot these characters: ' + differ[:-1])
    else:
        print()
        print('These words are not the same!') 
        
#end of function -------------------------------------------


if word1 == word2:                             #two words are the same
    print()
    print('This is correct: "' + word1 + '" :)')

elif len(word1) == len(word2):                 #swaped two characters ||  one character is wrong
    match = str('')
    differ1 = str('')
    differ2 = str('')
    
    for i in range(0,len(word1)):
        if word1[i] == word2[i]:
            match = match+word1[i]
        else:
            differ1 = differ1+word1[i]
            differ2 = differ2+word2[i]

    if len(differ1) == 1:                                            #one character is wrong
        print()
        print('These words are maybe the same: ' + word1)
        print("But you wrote '" + differ2 + "', instead of: '" + differ1 + "'")
        
    elif len(differ1) == 2 and differ1[0] == differ2[1] and differ1[1] == differ2[0]:     #swaped characters
            print()
            print('These words are maybe the same: ' + word1)
            print('But you swaped these characters: ' + differ1[0] + ',' + differ1[1])
            
    else:
        print()
        print('These words are not the same!') 

elif len(word1) > len(word2):                  #miss few letter 
    isLonger=bool(False)
    function(word2, word1, isLonger)    

else:                                          #you wrote more letter  
    isLonger=bool(True)
    function(word1, word2, isLonger)           

input('Press enter to exit the program!')