
def hocusPocus(inputText):
    inputText = inputText.replace('A','4')
    inputText = inputText.replace('a', '@')
    inputText = inputText.replace('B', '8')
    inputText = inputText.replace('b', '6')
    inputText = inputText.replace('E', '3')
    inputText = inputText.replace('e', '3')
    inputText = inputText.replace('I', '1')
    inputText = inputText.replace('i', '1')
    inputText = inputText.replace('L', '7')
    inputText = inputText.replace('l', '7')
    inputText = inputText.replace('s', '5')
    inputText = inputText.replace('S', '5')
    inputText = inputText.replace('z', '2')
    inputText = inputText.replace('Z', '2')
    inputText = inputText.replace('o', '0')
    inputText = inputText.replace('O', '0')
    return inputText

def unhocusPocus(inputText):
    inputText = inputText.replace('4','A')
    inputText = inputText.replace('@', 'a')
    inputText = inputText.replace('8', 'B')
    inputText = inputText.replace('6', 'b')
    inputText = inputText.replace('3', 'e')
    inputText = inputText.replace('1', 'i')
    inputText = inputText.replace('7', 'l')
    inputText = inputText.replace('5', 's')
    inputText = inputText.replace('2', 'z')
    inputText = inputText.replace('0', 'o')
    return inputText

while True:
    mode = input('Would you like to hocus pocus some text today? Or would you like to unhocus pocus text? \n')
    if mode == 'hocus pocus':
        inputText = input('Enter the text you want to be hocus pocused here: ')
        print('Hocus... POCUS!!\n')
        print(hocusPocus(inputText))
        break
    elif mode == 'unhocus pocus':
        inputText = input('Enter the text you want to be unhocus pocused here: ')
        print('UNHOCUS!!! Pocus...\n')
        print(unhocusPocus(inputText))
        break
    else:
        print('Please reply with either "hocus pocus" or "unhocus pocus"')