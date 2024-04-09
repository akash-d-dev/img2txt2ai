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

