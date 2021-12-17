## 安装配置AWS CLI


#安装最新版cli

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

unzip awscliv2.zip

sudo ./aws/install -i /usr/bin -b /usr/bin

aws --version

## 配置aws cli

 aws configure 

## 安装eksctl

curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp

sudo mv /tmp/eksctl /usr/local/bin

eksctl version

## 安装kubectl

\#安装kubectl 1.21（需和EKS版本匹配）

curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.21.2/2021-07-05/bin/linux/amd64/kubectl

 

chmod +x kubectl

mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$PATH:$HOME/bin

echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc

kubectl version --short --client



## 创建EKS集群

eksctl create cluster \
        --name emroneks \
        --version 1.21 \
        --region cn-northwest-1 \
        --managed \
        --nodegroup-name ng-emroneks \
        --node-type t3.large \
        --nodes 3 \
        --nodes-min 1 \
        --nodes-max 4

## 配置EKS集群

eksctl utils associate-iam-oidc-provider --cluster emroneks --approve



## 创建策略

emronekspolicy.json

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams",
                "logs:CreateLogGroup",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws-cn:logs:*:*:*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": "*"
        }
    ]
}
```

```
aws iam create-policy --policy-name emroneks-policy --policy-document file://emronekspolicy.json
```

role-trust-policy.json
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "emr-containers.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```
aws iam create-role --role-name emr_eks_runjob_role --assume-role-policy-document file://role-trust-policy.json

myaccount_id=`aws sts get-caller-identity --query Account --output text`

aws iam attach-role-policy --policy-arn arn:aws:iam::$myaccount_id:policy/emroneks-policy --role-name emr_eks_runjob_role

