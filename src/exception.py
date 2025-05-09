import sys
from src.logger import logging


# function to decide how the error message will look like
def error_message_details(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    
   
    )
    return error_message

   
# class for custom error message
class CustomeException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_details=error_details)

# print the error message

    def __str__(self):
        return self.error_message


# testing part
# if __name__=="__main__":
    
#     try:
#         a=10/0
#     except Exception as e:
#         logging.info(" Divide by Zero error ocurred")
#         raise CustomeException(e,sys)
        
