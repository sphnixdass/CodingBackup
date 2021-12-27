#!/bin/bash
while sleep 1; do
    clear;
    ping -c 1 www.google.com | grep 'time=' | awk '{print $8}';
done