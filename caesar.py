from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
new_text = str(input("Type a message:"))
rotate = int(input("Please enter rotation:"))
return_text = []
#enter_text = x.upper
dictionary = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
,'o','p','q','r','s','t','u','v','w','x','y','z']
dictionary = dictionary + list(map(str.upper, dictionary))
dictionary2 = ["!", ",", " ", "?", "'", ".", "(", ")", ]
for i in new_text:
    for j in dictionary:
        if i == j:
            new_index = dictionary.index(j) + rotate
            #print (new_index)
            return_text.append (dictionary[new_index])
    for k in dictionary2:
        if i == k:
            return_text.append(i)
s = ""
s = s.join(return_text)
print(s)
    return
