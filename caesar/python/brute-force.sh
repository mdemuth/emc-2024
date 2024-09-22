#!/usr/bin/env bash

for i in $(seq 0 25);
do
    cat $1 | ./caesar.py $i
    echo ""
done