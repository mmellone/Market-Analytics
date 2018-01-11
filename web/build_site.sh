#!/bin/bash

CWD=$(pwd)

# Copy files into apache root directory
echo Copying files to document root
# rsync -rtv $CWD /var/www/html
rm /var/www/html/*
cp * /var/www/html/

# Restart apache
echo Restarting Apache
service apache2 restart

echo Finished!
