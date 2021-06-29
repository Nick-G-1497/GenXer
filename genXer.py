import numpy
# import pandas
import random
from datetime import datetime
import string
import sys
import time
from loadbar import LoadBar



if __name__=="__main__":
  special = ';;>,/{[]}-_=+'
  letters= string.ascii_lowercase
  upper = string.ascii_uppercase
  number = '1234567890'
  seed =  int(input("Insert Seed: " )) % 69
  length = int(input("Password Length: "))

  aggregate = letters + number + special + upper

  art = '''=======================================\n
        GenXer - a mediocre password generator\n 
                      .-'-'`-.               .-'`-`-.
                  .-'-       \             /       -`-.
                  /    -.    - \           / -    .-    \
                /_/___ __.'-\  \        /  /-`.__ ___\_\
                /./ \_ \___ / \  |      |  / \ ___/ _/ \.\
                \/      /_ \  /  |      |  \  / _\      \/
                |  __\/   /./   |      |   \.\   \/__  |
                \  \_\  .'      |      |      `.  /_/  /
              _/ \____.'       /        \       `.____/ \_
            /'        \      /'|        |`\      /        `\
            |           \    /  |        |  \    /           |
            \/           \  \   |        |   /  /           \/
          /              `\ \   \      /   / /'              \
          /                 | \  |      |  / |                 \
        /   /              \    |      |    /              \   \
      .-'  ,'       \        \   \      /   /        /       `,  `-.
    |'  ./          `\       \   |    |   /       /'          \.  `|
    \   |'            \      `   |    |   '      /            `|   /
      `-/\     ./      |`\     \  |    |  /     /'|      \.     /\-'
        ||`---'        |  \     . |    | .     /  |        `---'||
        \\             /   \    | \    / |    /   \             //
        ||           /\_   \    \|    |/    /   _/\           ||
        \ \         /|  `\_|\    '    `    /|_/'  |\         / /
          | `\        |      |    \    /    |      |        /' |
          |   \       |      |     \  /     |      |       /   |
          |'  |        \      \    |  |    /      /        |  `|
          \   |         `-.    \   |  |   /    .-'         |   /
    -----._\__._           \   |   |  |   |   /           _.__/_.-----
                `-.         |  |   |  |   |  |         .-'
                            |  \   |  |   /  |
                            |  _|  |  |  |_  |
                            / /||..|  |..||\ \
        :F_P:            .' |/||||/  \||||\| `.            :F_P:
        ---._________.---'   ` \|''    ``|/ '   `---._________.---

        \n\n What a fucking bleak world we live in?


  '''

  # ------------------------------------------------
  # Art Work Performed by Lisa Mathews:
  # This ASCII pic can be found at
  # https://asciiart.website/index.php?art=people/naked%20ladies

  print(art)

  random.seed(seed)

  passwords= []

  for i in range(0,length):

      p = ''.join([random.choice(aggregate) for n in range(length)])
      passwords.append(p)
  

  bar = LoadBar(max=100)
  bar.start()
  for i in range(100):
      time.sleep(random.choice([.01,.001,.1,1]))
      bar.update(step=i)
  bar.end()
  
  print('\n\n==========================================================\n\n')
  print('Pick the one most likely to get your identity stolen\n\n\n')
  for password in passwords:
    print('\n' + password + '\n')      
