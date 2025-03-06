# iptables

Ref:-
1. https://www.youtube.com/watch?v=6Ra17Qpj68c


## Commands

#### Flush

```sh
sudo iptables -F
```

List 
```sh
sudo iptables -L
sudo iptables -L --line-numbers
```

```sh
sudo iptables --policy INPUT ACCEPT
sudo iptables --policy INPUT DROP
```

-I  =  insert at top
-A  = append at bottom


Drop connection from a host
```sh
sudo iptables -I INPUT -s 10.0.0.1 -j DROP
```

Drop connection from a subnet
```sh
sudo iptables -I INPUT -s 10.0.0.1/24 -j DROP
```

Prevent access to port 80
```sh
sudo iptables -I INPUT -p tcp --dport 80 -j DROP
```

Allow only a specific IP to access port 80
```sh
sudo iptables -I INPUT -p tcp --dport 80 -s 197.211.11.6 -j ACCEPT
```

Delete iptable rule at line number
```sh
sudo iptables -D INPUT 1
```

Drop all outgoing connections to port 443 of target server
```sh
sudo iptables -I OUTPUT -p tcp --dport 443 -j DROP
```


https://youtu.be/NAdJojxENEU

Redirect traffic comming from port 80 to port 8080 on same machine
```sh
sudo iptables --tables NAT --apppend PREROUTING --protocol tcp --dport 80 --jump REDIRECT --to 8080
```

DNAT forwarding to different machine
```sh
sudo iptables ---tables nat --append PREROUTING --protocol tcp --destination 192.168.254.47 --dport 80 --jump DNAT --to-destination 192.168.254.10:8080
```

```sh
sudo iptables --tables nat --append POSTROUTING --protocol tcp --destination 192.168.254.10 --dport 8080 --jump SNAT --to-source 192.168.254.47
```

```sh
sudo iptables --table nat --list
```


## Untested

2. **Enable IP Forwarding**: Ensure that IP forwarding is enabled on your server. Edit the `/etc/sysctl.conf` file to set `net.ipv4.ip_forward` to 1:

    ```bash
    sudo nano /etc/sysctl.conf
    ```

    Add the following line to the file if it's not already there:

    ```plaintext
    net.ipv4.ip_forward = 1
    ```

    Save the file and apply the changes:

    ```bash
    sudo sysctl -p
    ```

3. **Set Up Port Forwarding**: Use `iptables` to set up port forwarding:

    ```bash
    sudo iptables -t nat -A PREROUTING -p tcp --dport 99 -j DNAT --to 10.6.1.5:55
    sudo iptables -A FORWARD -p tcp -d 10.6.1.5 --dport 55 -j ACCEPT
    ```

    This command tells `iptables` to redirect incoming traffic on port 99 to port 55 of the private IP address (10.6.1.5).

4. **Save Your `iptables` Rules**: To make sure these rules persist after a server reboot, you need to save your `iptables` configuration:

    ```bash
    sudo service iptables save
    ```

    Or, on some distributions, you might use:

    ```bash
    sudo iptables-save > /etc/iptables/rules.v4
    ```

5. **Test Port Forwarding**: To ensure that the port forwarding is working as expected, you can use a tool like `telnet` or `nc` (netcat) from a remote system to test if you can access port 99 on your public IP, and it gets forwarded to port 55 on the private IP:

    ```bash
    telnet your_public_ip 99
    ```

    Replace `your_public_ip` with the actual public IP of your server.

