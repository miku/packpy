
"""
  ___________ _____  
 |___  /_   _|  __ \ 
    / /  | | | |__) |
   / /   | | |  ___/ 
  / /__ _| |_| |     
 /_____|_____|_|   

Relevant PEP for ZIP support:

* PEP 273 -- Import Modules from Zip Archives (2001)
* PEP 338 -- Executing modules as scripts (2004)
* PEP 441 -- Improving Python ZIP Application Support (2013)
"""

import datetime
import sys

if __name__ == '__main__':
    print(__doc__)
    print('This is Python %s (%s)' % (sys.version, datetime.date.today()))
