import requests
import unittest
from urllib import parse
from time import sleep


class WeatherTest(unittest.TestCase):
    def setUp(self):
        self.url="http://www.sojson.com/open/api/weather/json.shtml"
        # self.proxies={"http":"http://125.118.146.222:6666"}
    def test_weather_beijing(self):
        data={"city":"北京"}
        city=parse.urlencode(data).encode("utf-8")

        r=requests.get(self.url,params=city)
        result=r.json()
        #设置断言
        self.assertEqual(result["status"],200)
        self.assertEqual(result["message"],'Success !')
        sleep(3)

    def test_weather_param_error(self):
        #参数异常
        data={"city":"666"}
        r=requests.get(self.url,params=data)
        result=r.json()

        self.assertEqual(result['message'],"Check the parameters.")
        sleep(3)

if __name__=="__main__":
    unittest.main()