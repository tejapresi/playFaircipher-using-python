def playfair(text,keyword):

    result = ""
    #adding x if adjacent characters in the text    
    if(len(text) != len(set(text))):

        #iterating for loop from 0 to len(text)-1 (exclusive)
        for i in range(len(text)-1):
           #if two adjacent characters same
           if text[i] == text[i+1]:
               #add character x between them
               text = text[:i+1]+'x'+text[i+1:]

    #if length of text is not even then add z at end to ease the making of pairs
    if len(text)%2 != 0:
            text += 'x'
                
            
            
    #converting the text to upper case
    text =text.upper()


    #alphabets which are not in keyword
    alphabets = [chr(i) for i in range(65,91) if chr(i) not in keyword]

    #empty list key
    key = []

    #iterating through keyword to remove duplicate characters
    for k in keyword:
        #if k not in key
        if k not in key:
            #append the k in key
            key.append(k)
    
    #empty table (5x5) required        
    table = []
    #empty list ele
    ele = []

    ignore = True
    
    #iterating through key    
    for k in key:
        #if k not in table
        if k not in table:
            #if k not in ele and k is not space
            if k not in ele and k != ' ':
                # k is I/J
                if k == 'I' or k == 'J':
                    #if ignore is True
                    if ignore:
                        #append the k in ele
                        ele.append(k)
                        #assign False to ignore
                        ignore = False
                    #else once I/J is added to table no need to add other one
                    else:
                        #continue
                        continue
                #otherwise append all characters
                else:
                    #append k to ele
                    ele.append(k)
                
        #if len(ele) is 5 
        if(len(ele) == 5):
            #append ele to table
            table.append(ele)
            #empty the ele list
            ele = []

    #iterating through alphabets
    for alpha in alphabets:
        #if alpha is J
        if alpha == 'J':
            #continue
            continue
        #if len(ele) less than 5
        if len(ele) < 5:
            #append alpha to ele
            ele.append(alpha)
        #if len(ele) is 5
        if len(ele) == 5:
            #append ele to table
            table.append(ele)
            #empty the ele 
            ele = []
            
    #printing playfair table
    for i in table:
        print(*i)

    #convert the text into pairs
    pairs = []

    #iterating loop from 0 to len(text) with step count of 2
    for i in range(0,len(text),2):
        #append text[i:i+2] to pairs
        pairs.append(text[i:i+2])

    #printing pairs
    print(pairs)

    #iterating through each pair
    for pair in pairs:

        #store the coordinates of each letter in cord1 and cord2
        cord1 = []
        cord2 = []

        #iterate through pair
        for char in pair:

            #assign 0 to row_val and col_val
            row_val = col_val = 0

            #iterate through the table to find the coordinates of each letter in pair

            #iterate throught rows
            for row in range(5):
                #iterate through columns
                for col in range(5):
                    #if char is I and char not in table
                    if char == 'I' and 'I' not in table:
                        #assign J to char
                        char = 'J'
                        
                    #if char is J and char not in table
                    if char == 'J' and char not in table:
                        #assign I to char
                        char = 'I'
                        
                    #if the current row and col in table contains char
                    if table[row][col] == char:
                        
                        #store row and col values in row_val and col_val
                        row_val, col_val = row, col
                        #if cord1 is empty
                        if not cord1:
                            #store the row_val and col_val in cord1
                            cord1.append(row_val)
                            cord1.append(col_val)
                        #else
                        else:
                            #store the row_val and col_val in cord2
                            cord2.append(row_val)
                            cord2.append(col_val)

                            #if the two characters in same row move to the next right character
                            if(cord1[0] == cord2[0]):
                                result += table[cord1[0]][(cord1[1]+1)%5]
                                result += table[cord2[0]][(cord2[1]+1)%5]
                                result += " "
                            #else if two characters in same column move to the next below character
                            elif(cord1[1] == cord2[1]):
                                result += table[(cord1[0]+1)%5][cord1[1]]
                                result += table[(cord2[0]+1)%5][cord2[1]]
                                result += " "
                            #else store the corresponding column values of each other in same row
                            else:
                                result += table[cord1[0]][cord2[1]]
                                result += table[cord2[0]][cord1[1]]
                                result += " "
    #return result
    return result

#taking input for text
text = input("Enter text: ").upper()
#taking input for keyword
keyword = input("Enter key: ").upper()

#storing the cipher text
result = playfair(text,keyword).replace(' ','')

#printing the plain text and it's corresponding cipher text
print(f"Plain text -> Cipher text:")
print(f"{text}->{result}")
