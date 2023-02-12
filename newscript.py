import os
hostname = input("Enter host name or IP: ")
response = os.system("ping -c 2 " + hostname)

if response == 0:
  print (hostname, 'Success')
else:
  print (hostname, 'Server doesn`t work')
