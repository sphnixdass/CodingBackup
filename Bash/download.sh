#!/bin/bash

#http://kjv.wordfree.net/bibles/app/audio/1/2/37.mp3
baseurl=http://kjv.wordfree.net/bibles/app/audio/1

currentpath = pwd
# myuser="$(curl https://www.wordproject.org/bibles/audio/01_english/b02.htm | grep ".mp3" | awk -F  "=" '/1/ {print $3}' | awk -F  ">" '/1/ {print $1}')"

# # echo $myuser

# for item in $myuser
# do
# #   count=$((count+1))
# #   echo $count $item
# echo wget $item
#     wget $item
# done


for i in {1..200}
do

   mkdir -p $i

    for j in {1..200}
        do
        mkdir -p $i"/"$j
            echo $baseurl"/"$i"/"$j".mp3"
            wget $baseurl"/"$i"/"$j".mp3" -P $i"/"$j
        done
    
done
