from urllib import response
import requests
import xmltodict

from datetime_utils import formatted_date, formatted_time



class MeteoData:
    def __init__(self):
        self.url = f"https://vrijeme.hr/hrvatska_n.xml"
        self.data = None
        self.send_request()
    
    def send_request(self):
        response = requests.get(self.url)

        self.data = xmltodict.parse(response.content)

    def get_formatted_meteo_data(self):
        return{
            "location": self.data["Hrvatska"]["Grad autom='0'"]["GradIme"],
            "current temperature": self.data["Podatci"]["Temp"],
            "humidity":self.data["Podatci"]["Vlaga"],
            "pressure":self.data["Podatci"]["Tlak"],
            "last_refresh": f"{formatted_date()} {formatted_time()}"
        }





""" 
url = f"https://vrijeme.hr/hrvatska_n.xml"
response = requests.get(url)
data = xmltodict.parse(response.content)
print(data)
 """
