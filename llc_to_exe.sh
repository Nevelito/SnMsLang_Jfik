#!/bin/bash

llc program.ll -o program.s
gcc program.s -no-pie -o program
./program