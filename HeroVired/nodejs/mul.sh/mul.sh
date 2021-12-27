#!/bin/bash
echo "Enter a Number" 
read n 
re='^[0-9]+$'
if ! [[ $n =~ $re ]] ; then
   echo "error: Not a number" >&2; exit 1
fi

echo "Enter Range" 
read r 
re='^[0-9]+$'
if ! [[ $r =~ $re ]] ; then
   echo "error: Not a number" >&2; exit 1
fi

i=0 
while [ $i -le $r ] 
do 
    echo " $n x $i = `expr $n \* $i`" 
    i=`expr $i + 1` 
done


