#!/bin/bash
dirfolbackup="/hdd2/Backup/Coding/"
dirfolOrg="/hdd/Backup/Coding/"
dirfol="arduino/ledpush/ledpush/" && tempfilename="ledpush.ino" && mkdir -p $dirfolbackup$dirfol && cp $dirfolOrg$dirfol$tempfilename $dirfolbackup$dirfol$tempfilename
dirfol="arduino/led/" && tempfilename="led.ino" && mkdir -p $dirfolbackup$dirfol && cp $dirfolOrg$dirfol$tempfilename $dirfolbackup$dirfol$tempfilename
dirfol="Bash/pingtime/" && tempfilename="pingTime.sh" && mkdir -p $dirfolbackup$dirfol && cp $dirfolOrg$dirfol$tempfilename $dirfolbackup$dirfol$tempfilename
dirfol="Bash/urldownload/" && tempfilename="bashdownload.sh" && mkdir -p $dirfolbackup$dirfol && cp $dirfolOrg$dirfol$tempfilename $dirfolbackup$dirfol$tempfilename
dirfol="Bash/" && tempfilename="BackUp.sh" && mkdir -p $dirfolbackup$dirfol && cp $dirfolOrg$dirfol$tempfilename $dirfolbackup$dirfol$tempfilename
dirfol="Bash/" && tempfilename="download.sh" && mkdir -p $dirfolbackup$dirfol && cp $dirfolOrg$dirfol$tempfilename $dirfolbackup$dirfol$tempfilename
dirfol="c#/helloworld/" && tempfilename="" && mkdir -p $dirfolbackup$dirfol && cp -R $dirfolOrg$dirfol$tempfilename $dirfolbackup$dirfol$tempfilename
dirfol="C/" && tempfilename="" && mkdir -p $dirfolbackup$dirfol && cp -R $dirfolOrg$dirfol$tempfilename $dirfolbackup$dirfol$tempfilename
dirfol="C++/" && tempfilename="" && mkdir -p $dirfolbackup$dirfol && cp -R $dirfolOrg$dirfol$tempfilename $dirfolbackup$dirfol$tempfilename
dirfol="Cuda/" && tempfilename="" && mkdir -p $dirfolbackup$dirfol && cp -R $dirfolOrg$dirfol$tempfilename $dirfolbackup$dirfol$tempfilename
dirfol="esp/" && tempfilename="" && mkdir -p $dirfolbackup$dirfol && cp -R $dirfolOrg$dirfol$tempfilename $dirfolbackup$dirfol$tempfilename






