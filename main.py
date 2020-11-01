#import dns
#import dns.resolver
#import geoip2
#from geoip2 import database
import requests

#result = dns.resolver.resolve('tutorialspoint.com', 'A')
#for ipval in result:
 #   ip = ipval.to_text()


# to get the no of cooklies --


session = requests.Session()
response = session.get('https://tutorialspoint.com')
demo = session.cookies.get_dict()


print("no of cookies :",len(demo))


if "_ga" in demo:
    print('google anltics used')

# to find out google anlytics are used or not --





# to get the geo location of the given ip -- 


#reader = geoip2.database.Reader('/GeoLite2-City_20200804/GeoLite2-City.mmdb')
#response = reader.city(ip)
#print(response.country.iso_code)


#to get the ip from the given domain -- 
 
#result = dns.resolver.resolve('tutorialspoint.com', 'A')
#for ipval in result:
 #   ip = ipval.to_text()


 
#result = dns.resolver.resolve('tutorialspoint.com', 'A')
#for ipval in result:
 #   ip = ipval.to_text()
