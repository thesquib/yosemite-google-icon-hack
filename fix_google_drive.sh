#!/bin/bash
#Unfinished, do not run yet.
# DRIVE_LOCATION="/Applications/Google Drive.app"

# if [[ ("$#" -eq 1) && ($1 =~ .*Google\ Drive\.app) ]]; then
# 	DRIVE_LOCATION=$1
# fi

# RESOURCES=$DRIVE_LOCATION/Contents/Resources

# echo $RESOURCES

# if [[ ! -d $DRIVE_LOCATION ]]; then
# 	echo "Google Drive not found!"
# 	exit 1
# fi

# for x in mac-*2x.png; do echo ${x%@2x.png}; mv $x ${x%@2x.png}-inverse@2x.png; done
# for x in mac-*[0-8].png; do echo ${x%.png}; mv $x ${x%.png}-inverse.png; done
# for x in moving_mac-*; do mv $x  `echo $x | sed -e "s/-inverse//gI"`; done
# for x in moving_mac-*; do mv $x  `echo $x | sed -e "s/moving_//gI"`; done