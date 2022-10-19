**<h1>Networking Basics II</h1>**
  
  ***0. Change your home IP***
  
  Changes IP of the hosts, because our checker runs on docker, and docker lacks respect for host file modification...lol
  we have to copy the contents of the host file to a new file and update it and copy back to the host file.
  
  ***1. Show attached IPs***

**Ifconfig** is used to configure the kernel-resident network interfaces. It is used at boot time to set up interfaces as necessary. After that, it is usually only needed when debugging or when system tuning is needed. If no arguments are given, ifconfig displays the status of the currently active interfaces.
If you run ifconfig it displays ip addresses, netmasks... etc.
Here we only want to display the IPv4 IPs.
We will use grep and the search pattern will be using ERE(Extended Regular expression) so certain characters could act as quantifiers.
Our search pattern should only match non-empty spaces.
**Grep** and **awk** can be used at the same time to narrow down the search enhance results. 
**Grep** is a simple tool to use to quickly search for matching patterns.
**awk** is more of a programming language which processes a file and produces an output depending on the input values.
