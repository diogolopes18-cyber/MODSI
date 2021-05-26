#!/usr/bin/env bash

echo "Initializing Postgres table creation"
echo "Wish to proceed? [Y/n]"
read choice
if [ $choice = "Y" ] || [ $choice = "y" ] ; then
    echo "Creating..."
    command psql --host=database --username=postgres --dbname=modsi -f create_db.sql
    command psql --host=database --username=postgres --dbname=modsi
    else
        echo "Invalid Option"
        exit
fi