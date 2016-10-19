#!/usr/bin/env bash

name=$(ctx source instance runtime_properties name)
ctx logger info 'Setting name ${name}'
cat << EOF > /tmp/${name}
#!/bin/bash
touch /home/centos/userdata_finished
EOF



