#!/bin/bash

cat $1.dot | docker container run --rm -i vladgolubev/dot2png > $1.png
