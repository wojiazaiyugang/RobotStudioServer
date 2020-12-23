#!/bin/sh
pkill sem
name1=$(pidof y2)
name2=$(pidof DeviceDriverMain)
if [ -n "$name1" ] || [ -n "$name2" ]; then
exit 0
else
exit 1
fi

