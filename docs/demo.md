#EMR on EKS Demo

#环境准备：
● EKS 集群        * 1
● RDS MySQL 实例  * 1

#创建数据库和表
mysql -u admin -p -h <your db connect string>
create database emroneksdemo;
create table taixinfo (id varchar(16), vendor_id int);

#创建命名空间
kubectl create namespace emrjobdemo

#设置访问权限
eksctl create iamidentitymapping \
    --cluster emroneks \
    --namespace emrjobdemo \
    --service-name "emr-containers"

#创建虚拟集群
aws emr-containers create-virtual-cluster \
    --name virtualemrcluster \
    --container-provider '{
        "id":   "emroneks",
        "type": "EKS",
        "info": {
            "eksInfo": {
                "namespace": "emrjobdemo"
            }
        }
    }'

#更新任务执行策略
aws emr-containers update-role-trust-policy --cluster-name emroneks  --namespace emrjobdemo --role-name emr_eks_runjob_role

eksctl utils associate-iam-oidc-provider --cluster emroneks --approve
#查看虚拟集群
aws emr-containers list-virtual-clusters

#修改读取csv 文件的s3路径
aws s3 cp emr-on-eks-demo/source/spark-job.py s3://<your s3 bucket name>/input/

#编辑任务定义
vim emr-on-eks-demo/source/job-config.json

#运行任务
aws emr-containers start-job-run --cli-input-json file://./emr-on-eks-demo/source/job-config.json

#查看数据库中数据
mysql -u admin -p -h <your db connect string>