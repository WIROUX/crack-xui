import shodan
import re
import requests as req
regex = (r"\d")
def get_shodan_data_xui(): #Get data from shodan(query is XUI)
    api , data_list= shodan.Shodan("FBCWUSFYaT6Jo6eQAzkzVK5PKvkbQeDh") ,[]
    result = api.search("xui")
    for device in result['matches']:
        if 'HTTP/1.1 200 OK' in device['data']:
            data = {
                'ip': device['ip_str'],
                'hostname': device['hostnames'][0] if device['hostnames'] else '',
            }
            data_list.append(data)
    for data in data_list:
        ip_all = [(f"IP: {data['ip']}")]
        ip = data['ip']+':54321'
        try:
            r = req.get(ip)
            if r.status_code == 200:
                print(ip)
        except:
            print('not work:',ip)
