#!/usr/bin/env bash

echo "Initializing DB creation"
read choice
if [ $choice == "s" ] || [ $choice == "S" ] ; then
    echo "Starting..."
    command psql modsi -f query.sql
fi
