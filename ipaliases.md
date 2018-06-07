Creating Interface aliases (ip4) and assigning multiple ip6 addresses

If those create aliases scripts didn't work for you (like they didn't for me), you can follow these steps to create a single IPv4 alias and assign multiple IPv6 addresses for a particular interface (ipv4 alias is the same as assigning multiple ipv6 addresses https://superuser.com/a/477765/801942). If you need multiple aliases, you can repeat these steps for each interface. 

Use whatever IP you need for each interface. We're using:

10.200.1.1#/23 and fc01:dead:beef:1::1#/64 for traffic server A
10.200.1.2#/23 and fc01:dead:beef:1::2#/64 for traffic server B
If you ever mess up just go nuclear on the network configuration to start over:
sudo service network restart
sudo systemctl restart networking (only for centos7+)

Using ip:
Configure your interface if it's not already there (check with sudo ip addr)
sudo ip addr add 10.200.1.1/23 dev eth#
sudo ip -6 addr add fc01:dead:beef:1::1/64 dev eth#
sudo ip link set up
If you run sudo ip addr, you should see for your configured interface:
A big UP
An inet (ip4) address
An inet6 (ip6) address
Configure this for both traffic servers and see that you can communicate across both protocols by running ping and ping6
ping 10.200.1.#
ping fc01:dead:beef:1::#
You can use tcpdump on the other side to doubly ensure that interface is correctly getting those pings
Configure an aliased IPv4 address
sudo ip addr add 10.200.1.#1/23 dev eth# label eth#:1
Add another IPv6 address
sudo ip -6 addr add fc01:dead:beef:1::#1/64 dev eth#
If you run sudo ip addr again, you should now also see for your configured interface:
A secondary inet address with your label name at the end of that entry
Another, global inet6 entry with your configured ip6 address
Use ping and ping6 again to see if both sides can communicate on those addresses
Using ifconfig:
Configure your interface if it's not already there (check with ifconfig)
sudo ifconfig eth# up 10.200.1.#/23
sudo ifconfig eth# inet6 add fc01:dead:beef:1::#/64
If you run ifconfig, you should see for your configured interface:
An entry for your configured interface (which means it's up)
An inet (ip4) address with netmask 255.255.254.0 (for a /23 prefix)
An inet6 (ip6) address
Configure this for both traffic servers and see that you can communicate across both protocols by running ping and ping6
ping 10.200.1.#
ping fc01:dead:beef:1::#
You can use tcpdump on the other side to doubly ensure that interface is correctly getting those pings
Configure an aliased IPv4 address
sudo ifconfig eth#:1 up 10.200.1.#1/23
Add another IPv6 address
sudo ifconfig eth# inet6 add fc01:dead:beef:1::#1/64
If you run ifconfig again, you should now also see for your configured interface:
Another interface entry named eth1:1 with the configured ip4 address
Another, global inet6 entry for your original interface
Use ping and ping6 again to see if both sides can communicate on those addresses
