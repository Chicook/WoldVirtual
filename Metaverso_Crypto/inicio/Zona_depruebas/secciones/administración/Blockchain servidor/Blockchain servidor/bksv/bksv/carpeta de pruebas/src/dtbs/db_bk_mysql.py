## desarrollar mas adelante MySQL en desarrollo una blockchain con su base de datos interna ##

# from decouple import config 
# import pymysql 
# 
# def get_connetion():
#     try: 
#        return pymysql.connet(
#            host=config('MYSQL_HOST'),
#            user=config('MYSQL_USER'),
#            password=config('MYSQL_PASSWORD'),
#            db=config('MYSQL_DB'),
#        )
#     except Exception as ex:
#         print(ex)

#   from decouple import config

import pymysql
import traceback

# Logger
from src.utils.Logger import Logger


def get_connection():
    try:
            return pymysql.connect(
                        host=config('MYSQL_HOST'),
                                    user=config('MYSQL_USER'),
                                                password=config('MYSQL_PASSWORD'),
                                                            db=config('MYSQL_DB')
                                                                    )
                                                                        except Exception as ex:
                                                                                Logger.add_to_log("error", str(ex))
                                                                                        Logger.add_to_log("error", traceback.format_exc())