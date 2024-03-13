 - Steps to start txt2ai -

python3 -m venv venv

cd .\venv\Scripts\activate

1) create temp folder on same lvl as main-
2) rename sample temp to temp
3) rename Constants.txt to Constants.py and add API keys
pip3 install -r requirements.txt

uvicorn main:app --host localhost --port 8888  

forward port to 8888, change visibility to public


-----------------------------------------------------------------
uvicorn main:app --reload
or 
or
uvicorn main:app --host 192.168.56.1 --port 8000  
or 
uvicorn main:app --host 192.168.137.1 --port 8000

^
|
main network url 


pktriot.exe start



packetriot - 
lucid-wave-72717.pktriot.net



Tunnel configuration:
  Hostname: lucid-wave-72717.pktriot.net
  Server: asia-southeast-48343.packetriot.net
  IPv4: 206.189.80.59
  IPv6: 2400:6180:0:d1::7a9:1

Start the tunnel and visit URL to check its working:
  pktriot --config C:\Users\Asus\.pktriot\config.json start
  https://lucid-wave-72717.pktriot.net

Detailed help and step-by-step tutorials:
  https://docs.packetriot.com
  https://packetriot.com/tutorials.

Need more support?
  Email: support@packetriot.com
  Twitter: @packetriot (please follow us, we like new friends :)


C:\Users\Asus>pktriot.exe edit --name 'txt2ai'
Tunnel name updated


pktriot.exe tunnel http add --domain lucid-wave-72717.pktriot.net --destination localhost --http 8008 --letsencrypt