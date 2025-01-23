import urllib.request as urllib2
import json

while True:
    ip = input("Introduce tu IP: ")
    url = "http://ip-api.com/json/"
    
    try:
        response = urllib2.urlopen(url + ip)
        data = response.read()
        values = json.loads(data)
        
        if values["status"] == "success":
            print("IP: " + values["query"])
            print("City: " + values["city"])
            print("ISP: " + values["isp"])
            print("Country: " + values["country"])
            print("Region: " + values["regionName"]) 
            print("Timezone: " + values["timezone"])
        else:
            print("Error: " + values["message"])
    
    except Exception as e:
        print(f"Error al realizar la solicitud: {e}")
        break
