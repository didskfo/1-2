from keypad import constantList

def constant(consnum):
    try:
        if consnum == constantList[0]:
            text = '3.141592'
        elif consnum == constantList[1]:
            text = '3E+8'
        elif consnum == constantList[2]:
            text = '340'
        elif consnum == constantList[3]:
            text = '1.5E+8'
    except:
        text = 'Error!'
    return text