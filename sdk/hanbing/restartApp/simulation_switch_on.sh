#!/bin/sh
pkill sem
name1=$(pidof y2)
name2=$(pidof y2)
if [ -n "$name1" ] || [ -n "$name2" ]; then
echo "Device is running"
exit 0
else
echo "Device is not run, start simulation timer"
/robot/sem &
exit 1
fi

