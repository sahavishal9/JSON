import os
import json

def validateJSON(f):
    try:
        data=json.load(f)
    except ValueError as err:
        return False
    return True

from collections.abc import Iterable
def map_in_depth(f, l):
  return [(map_in_depth(f, e) if isinstance(e, Iterable) and not isinstance(e, (str,bytes)) else f(e)) for e in l]


def parsing(data):
    d=dict()
    for k,v in data.items():
        if isinstance(v,str): 
            d[k]=data[k][::-1]
        elif isinstance(v,(int,float)):
            d[k]=data[k]**2
        elif isinstance(v,list): 
            x=map_in_depth(lambda x: x**2 if isinstance(x,(int,float)) else x[::-1], v)
            d[k]=x
    print("-------------Original Data----------")
    print(data)
    print("-------------Updated Data----------")
    print(d)
    logger.info(f"Upadte Data : {d} ")
    

def Logging():
    import logging
    # Create and configure logger
    logging.basicConfig(filename="newlog.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    # Creating an object
    logger = logging.getLogger()
     
    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    
    return logger 


if __name__=="__main__":
    logger= Logging()
    path=input()
    if os.path.isfile(path):
        logger.info("'Path is Valid'")
        f = open(path,)
        if validateJSON(f):
            logger.info("'JSON file  is Valid'")
            f.close()
            f = open(path,)
            data=json.load(f)
            logger.info("'JSON file  parsing started...'")
            parsing(data)
            logger.info("'JSON file  successfully updated.'")
        else:
            logger.error("JSON file is not valid")
    else:
        logger.error("Please! Enter right path.")
