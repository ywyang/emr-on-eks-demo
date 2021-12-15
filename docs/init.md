## 安装配置AWS CLI

\#卸载当前版本aws cli

which aws

sudo rm /usr/bin/aws

sudo rm /usr/bin/aws_completer

sudo rm -rf /usr/bin/v2 

\#安装最新版cli

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