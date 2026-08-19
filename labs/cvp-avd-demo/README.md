# CVP and AVD Demo, EVPN MLAG

> [!WARNING]
> This lab is in preview. It's fully functional, but breaking changes can happen.
> We are working hard on building the best lab collection and your feedback is always  appreciated.

Last reviewed: 18/08/2026

> Lab Credentials  
&nbsp;&nbsp;&nbsp;&nbsp;Username: arista  
&nbsp;&nbsp;&nbsp;&nbsp;Password: arista  

This lab intentionally ships without separate docs or slide content.

## Lab Inventory

This lab has following devices:

| Hostname | Type | OS | Management Address | Username | Password |
| -------- | ---- | -- | ------------------ | -------- | -------- |
| s01 | switch | cEOS-lab, 4.36.1F | 10.0.1.1 | arista | arista |
| s02 | switch | cEOS-lab, 4.36.1F | 10.0.1.2 | arista | arista |
| l01 | switch | cEOS-lab, 4.36.1F | 10.0.2.1 | arista | arista |
| l02 | switch | cEOS-lab, 4.36.1F | 10.0.2.2 | arista | arista |
| l03 | switch | cEOS-lab, 4.36.1F | 10.0.2.3 | arista | arista |
| l04 | switch | cEOS-lab, 4.36.1F | 10.0.2.4 | arista | arista |
| h01 | host | cEOS-lab, 4.36.1F | 10.0.3.1 | arista | arista |
| h02 | host | cEOS-lab, 4.36.1F | 10.0.3.2 | arista | arista |

> To access any device, use `ssh <username>@<hostname>` or simply type `<hostname>` to use the SSH alias.
