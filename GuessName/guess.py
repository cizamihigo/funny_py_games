import random

lives = 10
words = ['pays','jeu','montagne','ville','amusant','rigoureux','voyou','course','aide','selection','edition','fichier','depart']
mot_secret = random.choice(words)
# cl_len =len(mot_secret)
# cl_le = '?'*cl_len
# lis_cle_le = list(cl_le)
clue = []
# At first sight every charcater is unknown means
unkownchar = len(mot_secret)
# print(lis_cle_le)
index = 0
while index <len(mot_secret):
    clue.append('?')
    index += 1
heart = u' \u2765 '
# print(heart)
correct_guess = False

def my_clue(geuss, mot_secret, clue, unkownchar):
    index = 0
    # guu[cl_len] = list('')
    # if index == 0:
    #     guu[cl_len+1] =''
    while index < len(clue) :
        if guess == mot_secret[index]:
            clue[index] = geuss
            unkownchar -= 1
            # guu[index] = guess
        index += 1
    return unkownchar
    # if guu == lis_cle_le:
    #     print("Completed")
while lives > 0:
    print(clue)
    print('Left Lives: ' + heart * lives)
    guess =input('Guess a letter or the whole word:  ')

    if guess == mot_secret :
        correct_guess = True
        print("This is amazing!!!!")
        break
    if guess in mot_secret :
        # my_clue(guess, mot_secret, clue,unkownchar)
        unkownchar = my_clue(guess, mot_secret, clue, unkownchar)
    else:
        print("Incorrect. Try again but you lose one life")

        lives = lives - 1
    if unkownchar == 0 :
        print("You won\n********\n")
        break
if correct_guess:
    print("You won")
else:
    print("No Way you can't WIN")


