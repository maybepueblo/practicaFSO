#!/bin/bash

DIRS="/home /etc /var/www /opt"
BACKUP_PATH="/home/vmuser/backup"

sudo mkdir -p "$BACKUP_PATH"

FECHA=$(date +"%Y-%m-%d")

for dir in $DIRS; do
    DESTINY="$BACKUP_PATH/$FECHA-$(basename "$dir")"
    if [ -d "$DESTINY" ]; then
        echo "$DESTINY exists, no copy"
    else
        sudo cp -r "$dir" "$DESTINY"
        echo "backup $dir completed in $DESTINY"
    fi
done

sudo find $BACKUP_PATH -mindepth 1 -maxdepth 1 -type d -mtime +7 -exec rm -rf {} \;

sudo find /var/log -type f -name "*.log" -mtime +7 -exec rm -f {} \;

echo "Maintenance done"

