from logger import logging

def add(a, b):
    logging.debug("The additon operation is taking place")
    return  a+b

logging.debug("The additon function is called")
add(10,5)