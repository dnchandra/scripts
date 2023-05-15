#!/bin/bash
echo -e "Hostname:"`hostname`
echo -e "Date:"`date`
echo -e "Uptime:"`uptime -p`
echo -e "Machine Type:"`vserver=$(lscpu | grep Hypervisor | wc -l); if [ $vserver -gt 0 ]; then echo "VM"; else echo "Physical"; fi`
echo -e "Version:"`cat /etc/redhat-release`
echo -e "Kernel:"`uname -r`
echo -e "Processor Name:"`awk -F':' '/^model name/ {print $2}' /proc/cpuinfo | uniq | sed -e 's/^[ ]*//'`
echo -e "System Main IP:"`hostname -I`
echo -e "Logged-in User:"`whoami`
echo -e "Ulimit open files:"`ulimit -n`
echo -e "Ulimit max user processes:"`ulimit -u`
echo -e "Ulimit POSIX message queues:"`ulimit -q`
echo -e "Manufacturer:"`cat /sys/class/dmi/id/chassis_vendor`
echo -e "Product Name:"`cat /sys/class/dmi/id/product_name`