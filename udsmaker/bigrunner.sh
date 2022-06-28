#! /bin/bash
nproc=24
nruns=60
for ((i=0;i<${nproc};i+=1))
do
	firsti=`expr ${i} \* ${nruns}`;
	lasti=`expr ${firsti} + ${nruns} - 1`;
	rm -f logfiles/hydro2uds_${firsti}_${lasti}.txt;
	echo starting runs with firsti=${firsti}, lasti=${lasti};
	`./runner.sh ${firsti} ${lasti} > logfiles/hyro2uds_${firsti}_${lasti}.txt &` ;
done
