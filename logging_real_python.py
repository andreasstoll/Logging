#Quelle: https://realpython.com/python-logging/

import logging

logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S') 

def foo():
    logging.warning('foo aufgerufen')
    print("hallo")


foo()



