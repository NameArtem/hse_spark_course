#!/bin/bash
#set -x
#Возвращает активные namenode FQDN в stdout
portName=":8020"

#проверяем выполняемость в hdfs 
if [ ! -z "$HADOOP_HOME" ]; then
    set PATH=$PATH:$HADOOP_HOME/bin
fi

isBinaryAccessible=`which hdfs > /dev/null 2>&1`
status=$?

if [ $status -ne 0 ]; then
    echo "Could not locate hdfs executable. Please set HADOOP_HOME properly or add hdfs binary in your default PATH"
    exit 1
fi        

adminuser=`hdfs getconf -confKey dfs.cluster.administrators`
if [ $? -ne 0 ]; then   
    echo "User $USER doesn't have execute permission as hdfs admin OR cluster is not accessible from this host"
    exit 1
fi

haClusterName=`hdfs getconf -confKey dfs.nameservices`

if [ $? -ne 0 -o -z "$haClusterName" ]; then
    echo "Unable to fetch HA ClusterName"
    exit 1
fi

nameNodeIdString=`hdfs getconf -confKey dfs.ha.namenodes.$haClusterName`


for nameNodeId in `echo $nameNodeIdString | tr "," " "`
do
    status=`hdfs haadmin -getServiceState $nameNodeId`
    if [ $status = "active" ]; then 
        nameNode=`hdfs getconf -confKey dfs.namenode.https-address.$haClusterName.$nameNodeId`
        if [ -z "$portName" ] ; then
            echo $nameNode
            exit 0;
        else
            echo `echo $nameNode|cut -d":" -f1`$portName
            exit 0;
        fi
    fi
done
