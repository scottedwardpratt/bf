#!/bin/bash
\rm -f mutcalc_results/*.txt
nevents=1000
for((i=0;i<4;i++))
do 
	i0=`expr ${i} \* ${nevents}`
	if=`expr ${i} \* ${nevents} + ${nevents}`
	bf_fromhydro ${i} ${i0} ${if}
	\cp -f mutcalc_results/*.txt mutcalc_input/ 
done