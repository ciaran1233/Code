alphabet = 'abcdefghijklmnopqrstuvwxyz'
# print(alphabet[0])
# print(alphabet[6])
# print(alphabet[9])
key =3
newMessage = ''


message = input('please enter a message:')



# character= input ('please enter a character')
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
# print(position)
        newPosition = (position + key)%26
# print(newposition)
        newCharacter = alphabet[newposition]
        print('The new character is:',newCharacter)
        newMessage += newCharacter

    else:
        newMessage += character
# print('your new message is ',newMessage)