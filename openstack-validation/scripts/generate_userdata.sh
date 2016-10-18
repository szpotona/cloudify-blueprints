#!/usr/bin/env bash

echo 'Setting name ${name}'

cat << EOF > /tmp/${name}
#!/bin/bash
touch /home/centos/userdata_finished
EOF



