print('\033[1;34m\n Congratulations! Your Device Support This Tools\033[1;37m')
import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')

import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from RUN import Subscraption

        Subscraption()        

