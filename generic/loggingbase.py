import logging
import datetime


#create an instance of logger
logger=logging.getLogger('simple_logger')
current_time=datetime.datetime.now().strftime("%I-%M%p-%B-%d-%Y")
log_path='C://Users//chand//PycharmProjects//revisionpro//logs'+current_time

#create log handler
handler=logging.FileHandler(log_path+'.log')
handler.setLevel(logging.WARNING)

#create formatter and set it in handler
formatter=logging.Formatter('%(asctime)s - %(name)s %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


