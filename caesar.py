from helpers import alphabet_position, rotate_character
new_text = str(input("Type a message:"))
rotate = int(input("Please enter rotation:"))
return_text = ""
#enter_text = x.upper
dictionary = 'abcdefghijklmnopqrstuvwxyz'
#dictionary = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
#'n','o','p','q','r','s','t','u','v','w','x','y','z']*2
dictionary2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#dictionary2 =list(map(str.upper, dictionary))

dictionary3 = ["!", ",", "?", "'", ".", "(", ")", ]
for i in new_text:
    if i in dictionary:
        new_index = (dictionary.find(i)+rotate) %26
            #print (new_index)
        return_text += dictionary[new_index]
    
    elif i in dictionary2:
        new_index = (dictionary2.find(i)+rotate) %26
        return_text += dictionary2[new_index]
    else:
        return_text += i
#s = ""
#s = s.join(return_text)
print(return_text)    return
