#!/bin/bash
\rm -f mutcalc_results/*.txt
\rm -f crap.log
nevents=3
for((i=0;i<4;i++))
do 
	i0=`expr ${i} \* ${nevents}`
	if=`expr ${i} \* ${nevents} + ${nevents}`
	echo i=${i}, i0=${i0}, if=${if}
	bf_fromhydro ${i} ${i0} ${if}
	\cp -f mutcalc_results/*.txt mutcalc_input/
done