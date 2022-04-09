from IPython.display import clear_output


t=['0','1','2','3','4','5','6','7','8','9']

def display_board(t):
    clear_output
    print(t[1]+'|'+t[2]+'|'+ t[3])
    print(t[4]+'|'+t[5]+'|'+ t[6])
    print(t[7]+'|'+t[8]+'|'+ t[9])