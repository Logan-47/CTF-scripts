#!/usr/bin/python

# -append : append images horizontally
# +append : append images vertically
import os
start = 1
last = 22
counter = 1
cmd=''
cmd+='convert '
for x in range(start,last):
    if x <10:
       
        cmd+='1_0'+str(x)+'.jpg '
    else:
        cmd+='1_'+str(x)+'.jpg '


cmd+=" +append output"+str(counter)+".jpg"

os.system(cmd)
counter += 1
while(last != 442):
    cmd=''
    cmd+='convert '
    start = last
    last += 21
    
    for x in range(start,last): 
         
        cmd+='1_'+str(x)+'.jpg '
   
    cmd+=" +append output"+str(counter)+".jpg"
    os.system(cmd)
  
    counter += 1
#final image
cmd=''
cmd+='convert '
for x in range(1,22):
    cmd+='output'+str(x)+'.jpg '

cmd+=" -append flag.jpg"

os.system(cmd)
print("check flag.jpg")
