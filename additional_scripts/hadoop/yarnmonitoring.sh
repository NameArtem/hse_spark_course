#!/bin/bash
#Мониторинг приложений на Yarn

if [ "$#" -lt 1 ]; then
  echo "Usage: $0  <max_life_in_mins>"
  exit 1
fi

yarn application -list 2>/dev/null | grep "application_" | grep "RUNNING" | grep "default" | awk '{print $1}' > job_list.txt

for jobId in `cat job_list.txt`
do
finish_time=`yarn application -status $jobId 2>/dev/null | grep "Finish-Time" | awk '{print $NF}'`

if [ $finish_time -ne 0 ]; then
  echo "App $jobId is not running"
  exit 1
fi

time_diff=`date +%s`-`yarn application -status $jobId 2>/dev/null | grep "Start-Time" | awk '{print $NF}' | sed 's!$!/1000!'`
time_diff_in_mins=`echo "("$time_diff")/60" | bc`

echo "App $jobId is running for $time_diff_in_mins min(s)"

if [ $time_diff_in_mins -gt $1 ]; then
  echo "Moving app $jobId to strategic queue"
yarn application -movetoqueue $jobId -queue strategic
echo "Yarn job $jobId is moved to strategic queue as it is taking more than 60 mins to complete in default queue" | mail -s "Alert : Yarn Queue Management" NSC-BIGINSIGHTS-INFRASTRUCTURE@nationwide.com
else
  echo "App $jobId should continue to run"
fi

done