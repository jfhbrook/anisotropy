#!/usr/bin/bash


. /u1/uaf/holbrook/.profile
cd /scratch/holbrook/fea

logfile="babbysit.log"
lockfile="sim.lock"

if [ -f $lockfile ]; then
    if [ "$(ps -p `cat $lockfile` | wc -l)" -gt 1 ]; then
        "Dude, it's already running! wtf" >> $logfile
        exit
    fi
fi

nohup comsol -np 4 matlab -ml -nodesktop -ml -nosplash -mlr "worker($@)" >> $logfile &
comPID=$!
echo "Comsol Matlab PID: $comPID " >> $logfile
echo $comPID > $lockfile

#as long as it's supposedly running....
while [ -f $lockfile ]; do
    sleep 10m #we don't need to check THAT often... 
    #checks for the existence of a segfault
    if [`tail -n 2 $logfile | grep -c 'Segmentation fault'`] ; then
        echo "Sumbitch segfaulted! Restarting..." > $logfile
        nohup comsol -np 4 matlab -ml -nodesktop -ml -nosplash -mlr "worker($@)" >> $logfile &
        comPID=$!
        echo $comPID > $lockfile
        echo "restarted.\n" >> $logfile
    #maybe the program's done running?
    elif [ "$(ps -p `cat $lockfile` | wc -l)" -lt 2 ]; then
        echo "PROCESS STOPPED WITHOUT A SEGFAULT--MAYBE ITS DONE!" >> $logfile
        cat $logfile | mutt -s'Hey, stuff happened.' josh.holbrook@gmail.com
        exit
    fi
done

