#!/bin/bash

filename=$1
rm -r tmp
mkdir tmp

cp $filename tmp
#cp rockyou.txt tmp
cd tmp

while [ 1 ]
do
    file $filename

    file $filename | grep "bzip2"
    if [ "$?" -eq "0" ]
    then
        echo "This is a Bzip!"
        mv $filename $filename.bz2
        bunzip2 $filename.bz2
        filename=$(ls *)
        # echo $filename
    fi

    file $filename | grep "Zip"
    if [ "$?" -eq "0" ]
    then
        echo "This is a zip!"
        mv $filename $filename.zip
        #$password = fcrackzip -v -D -u -p rockyou.txt $filename | grep " == "| cut -d' ' -f5
        password=$(fcrackzip -v -D -u -p ../rockyou.txt $filename.zip | grep " == "| cut -d' ' -f5)
        # echo $password
        unzip -P $password $filename.zip
        rm $filename.zip
        filename=$(ls *)
        # echo $filename
    fi
    
    file $filename | grep "gzip"
    if [ "$?" -eq "0" ]
    then
        echo "This is a Gzip!"
        mv $filename $filename.gz
        gunzip $filename.gz
        filename=$(ls *)
        # echo $filename
    fi
done
