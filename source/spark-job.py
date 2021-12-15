import argparse
import logging
from operator import add
from random import random
import os

from pyspark.sql import SQLContext,SparkSession

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def doexec() :

    spark = SparkSession.builder.appName("spark demo").getOrCreate()
    try:
        text = spark.read.format('csv').options(header='true', inferSchema='true').load('s3://<your s3 bucket name>/input/ny-taxi.csv')
    except Exception as e:
        print("---------read csv file error-------------",e)
    #print(text)

    #write to mysql
    try:
        text.select('id','vendor_id').write.format('jdbc').options(
            url='jdbc:mysql://<your rds mysql connect string>:3306/emroneksdemo?&useSSL=false',
            driver='com.mysql.jdbc.Driver',
            dbtable='taixinfo',
            user='<your db username>',
            password='<your db password>'
        ).mode('append').save()
    except Exception as e:
        print("---------write mysql  error-------------",e)


if __name__ == "__main__":
    doexec()