#!/bin/bash

grep "Failed password" /var/log/auth.log > failed_logins.txt

echo "Failed login entries collected."
