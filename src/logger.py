import logging

logging.basicConfig(
    filename="../log.txt",     # File name
    filemode="w",           # Overwrite every run
    level=logging.DEBUG,    # Log everything DEBUG and above
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log(ltype, message):
    if ltype == "debug":
        logging.debug(message)
    elif ltype == "info":
        logging.info(message)
    elif ltype == "warn":
        logging.warning(message)
    elif ltype == "error":
        logging.error(message)
    else:
        logging.error(f"{ltype} is not supported, please use debug, info, warn or error.")

#logging.debug("Debug")
#logging.info("Info")
#logging.warning("Warning")
