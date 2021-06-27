import numpy
# import pandas
import random
from datetime import datetime
import string
import sys


if __name__=="__main__":
  special = ';;>,/{[]}-_=+'
  letters= string.ascii_lowercase
  upper = string.ascii_uppercase
  number = '1234567890'
  seed =  int(sys.argv[1]) % 69
  length = int(sys.argv[2])

  aggregate = special + letters + upper + number

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

  password = ''

  for i in range(0,length):

      password=''.join([random.choice(aggregate) for n in range(length)])
      
  print('\n' + password + '\n')

      
