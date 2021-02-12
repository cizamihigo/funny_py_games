from tkinter import Tk, messagebox, simpledialog

def know_job():
    task = simpledialog.askstring('What to do!', 'Do you want to encrypt (1) or decrypt (2)?')
    return task
def write_msg():
    msg = simpledialog.askstring('Message', 'Enter a secret Message: ')

    return msg
def is_even(number):
    return number%2 == 0
def get_even_l(message):
    even_l =[]
    for counter in range(0, len(message)):
        if is_even(counter):
            even_l.append(message[counter])
    return even_l
def get_odd_l(message):
    odd_l =[]
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_l.append(message[counter])
    return odd_l
def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = 'Bl al ciza' + message + 'TxV'
    even_letters = get_even_l(message)
    odd_letters = get_odd_l(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

root = Tk()
while True:
    task = know_job()
    if task == 'encrypt' or task == '1' :
        message = write_msg()
        encrypted = swap_letters(message)
        messagebox.showinfo('cypher text of the secret message is:', encrypted)
    elif task == 'decrypt' or task == '2' :
        message = write_msg()
        decrypted = swap_letters(message)
        messagebox.showinfo('plain text message is: ', decrypted)

    else:
        break
root.withdraw()