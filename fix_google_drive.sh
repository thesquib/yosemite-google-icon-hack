#!/bin/bash
#Unfinished, do not run yet.
DRIVE_LOCATION="/Applications/Google Drive.app"

if [[ ("$#" -eq 1) && ($1 =~ .*Google\ Drive\.app) ]]; then
	DRIVE_LOCATION=$1
fi

RESOURCES=$DRIVE_LOCATION/Contents/Resources

echo $RESOURCES

if [[ ! -d $DRIVE_LOCATION ]]; then
	echo "Google Drive not found!"
	exit 1
fi

cd "$RESOURCES"
for x in mac-*-inverse*.png; do 
	mv "$x" "moving_$x"
done

for x in mac-*2x.png; do 
	NEW_NAME="${x%@2x.png}-inverse@2x.png"
	echo "$x -> $NEW_NAME"
	mv "$x" "$NEW_NAME"
done

for x in mac-*[0-8].png; do
	NEW_NAME="${x%.png}-inverse.png"
	echo "$x -> $NEW_NAME"
	mv "$x" "${x%.png}-inverse.png"
done

for x in moving_mac-*; do
	NEW_NAME=`echo "$x" | sed -e "s/-inverse//gI" -e "s/moving_//gI"`
	echo "$x -> $NEW_NAME"
	mv "$x" "$NEW_NAME"
done
