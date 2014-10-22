Raspstat
=======

Python wrapper to get system stats in linux.

#Installation
Run `pip install raspstat`, or clone the repo and run `python setup.py install`.

#Usage:
```
import raspstat

ram = raspstat.getRam()
print 'Free RAM: '+str(ram[1]) + ' ('+str(ram[0]) + ')'
print 'Nr. of processes: ' + str(raspstat.getProcessCount())
print 'Up time: '+raspstat.getUpStats()[0]
print 'Nr. of connections: ' + str(raspstat.getConnections())
print 'Temperature in C: ' + str(raspstat.getTemperature())
print 'IP-address: ' + raspstat.getIpAddress()
print 'CPU speed: ' + str(raspstat.getCpuSpeed())
```
