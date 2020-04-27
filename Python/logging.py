import logging
logging.basicConfig(filename="" ,level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
# logging.DEBUG
# logging.INFO
# logging.WARNING
# logging.ERROR
# logging.CRITICAL
logging.debug('start of program')
def factorial(n):
    logging.debug('start of factorial(%s)' %(n))
    total = 1
    for i in range(1,n+1):
        total *=i
        logging.debug('i is %s,total is %s' %(i,total))
    logging.debug('return value is %s' %(total))    
    return total    

print(factorial(5))        
