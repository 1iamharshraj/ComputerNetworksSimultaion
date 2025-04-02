
def get_ip_class(ip):
    first_octet = int(ip.split('.')[0])

    if 1<= first_octet <= 126:
        return "A","255.0.0.0","1.0.0.0-126.255.255.255"
    elif 128 <= first_octet <= 191:
        return "B","255.255.0.0","128.0.0.0-191.255.255.255"
    elif 192 <= first_octet <= 223:
        return "C","255.255.255.0","192.0.0.0-223.255.255.255"
    elif 223 <= first_octet <= 239:
        return "D (Multicast)", "N/A","224.0.0.0-239.255.255.255"
    elif 240 <= first_octet <= 255:
        return "E (Experimental)","N/A","240.0.0.0-255.255.255.255"
    else:
        return "Invalid","N/A","N/A"

ip_address = "192.168.1.1"

ip_class , subnet_mask, ip_range = get_ip_class(ip_address)


print(ip_address)
print(ip_class)
print(subnet_mask)
print(ip_range)