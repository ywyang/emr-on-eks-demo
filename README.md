# emr-on-eks-demo

此项目实现了使用EMR on EKS的Spark 任务，从S3存储桶中读取csv文件写入到MySQL中。

环境准备工作请参考[**环境准备**](https://github.com/ywyang/emr-on-eks-demo/blob/main/docs/init.md)

任务执行步骤请参考[**任务执行**](https://github.com/ywyang/emr-on-eks-demo/blob/main/docs/demo.md)

文件清单


| 文件名称 | 用途 |
| -- | :--- |
| [ny-taxi.csv](https://github.com/ywyang/emr-on-eks-demo/blob/main/input/ny-taxi.csv) | csv原始数据 |
| [spark-job.py](https://github.com/ywyang/emr-on-eks-demo/blob/main/source/spark-job.py) | 任务执行脚本（PySpark） |
| [mysql-connector-java-5.1.47-bin.jar](https://github.com/ywyang/emr-on-eks-demo/blob/main/source/mysql-connector-java-5.1.47-bin.jar) | MySQL  JDBC连接jar包 |
| [job-config.json](https://github.com/ywyang/emr-on-eks-demo/blob/main/source/job-config.json) | 任务定义文件 |
