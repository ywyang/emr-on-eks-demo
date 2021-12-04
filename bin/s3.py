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
    #text = spark.read.text("s3n://emr-on-eks-camp/input/demo.txt")
    try:
        text = spark.read.format('csv').options(header='true', inferSchema='true').load('s3://emr-on-eks-camp/input/ny-taxi.csv')
    except Exception as e:
        print("---------read csv file error-------------",e)
    print(text)

    #files = os.system('find / -name "*.jar"')
    #files.write.format("json").save("s3://emr-on-eks-camp/output/jar")
    # write to s3
    #text.write.format("json").save("s3://emr-on-eks-camp/output/xxx")

    #write to mysql
    try:
        text.select('id','vendor_id').write.format('jdbc').options(
            url='jdbc:mysql://camp-demo.cmf4ifsiftsb.rds.cn-northwest-1.amazonaws.com.cn:3306/demo?&useSSL=false',
            driver='com.mysql.jdbc.Driver',
            dbtable='taix',
            user='admin',
            password='2021.Com'
        ).mode('append').save()
    except Exception as e:
        print("---------write mysql  error-------------",e)
        #e.write.format("json").save("s3://emr-on-eks-camp/output/except")
    #print(text.to)
    #spark.read.format('csv').options(header='true', inferSchema='true').load('s3://emr-workshop-yyw/input/tripdata.csv')

    #countsByAge = data.groupBy("id").count()
    #countsByAge.show()

    # Saves countsByAge to S3 in the JSON format.
    #countsByAge.write.format("json").save("s3a://emr-workshop-yyw/emroneks/")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--partitions', default=2, type=int,
        help="The number of parallel partitions to use when calculating pi.")
    parser.add_argument(
        '--output_uri', help="The URI where output is saved, typically an S3 bucket.")
    args = parser.parse_args()

    doexec()