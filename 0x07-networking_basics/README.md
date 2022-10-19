**<h1>Networking Basics I</h1>**

***OSI (Open Systems Interconnection)***

is an abstract model to describe layered communication and computer network design.
The idea is to segregate the different parts of what make communication possible.
There are 7 layers. Descending order:- Application, Presentation, Session, Transport, Network, Data Link and Physical.

***Types of Networks***

**LAN** connect local devices together.
**WAN** connects LANs together. 
WANs are operating over the **Internet**.

***MAC and IP Address***

**MAC Address** is unique identifier of a network interface.
**IP Address** Is a number that network devices use to connect to networks.

***TCP and UDP***

**TCP** is a protocol that is transferring data in a slow way but surely.
**UDP** is a protocol that is transferring data in a fast way and might loss data along in the process

***TCP and UDP ports***

A TCP/UDP network device has 65535 ports. 
Some of them are officially reserved for a specific usage.
Some of them are known to be used for a specific usage (but nothing is officially declared).
The rest are free of use.
IP+Port=Socket.

***The Internet Control Message Protocol (ICMP)***

is a protocol in the Internet protocol suite. 
It is used by network devices, to check if other network devices are available on the network. 
The command **ping** uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network.
