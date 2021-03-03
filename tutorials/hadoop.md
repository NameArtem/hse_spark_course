hadoop fs –usage ls

hadoop fs –ls

hadoop fs –ls /

hadoop fs –mkdir /user

sudo –u hdfs hadoop fs –mkdir /user

hadoop fs –copyFromLocal Sample1.txt /user

hadoop fs –put Sample2.txt /user

hadoop fs –moveFromLocal Sample3.txt /user

hadoop fs –du /user

hadoop fs –df

hadoop fs –expunge

hadoop fs –cat /user

hadoop fs –cp /user_from /user_to

hadoop fs –mv /user_from /user_to

hadoop fs –rm -r /user

hadoop fs –copyFromLocal /user /user_local

hadoop fs –get /user /user_local

hadoop fs –touchz /user

hadoop fs –setrep –w 1 /user/

sudo –u hdfs hadoop fs –chgrp –R GROUPNAME /user

sudo –u hdfs hadoop fs –chown –R GROUPNAME /user
