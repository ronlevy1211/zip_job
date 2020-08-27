cat /etc/os-release | grep ID= -m 1 | awk -F = '{ print "OS_Type:"$2}' && [[ -f /tmp/zip_job.py ]] && echo "zip_job.py exists." 

