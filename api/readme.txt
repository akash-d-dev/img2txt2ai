python3 -m venv venv
.\venv\Scripts\activate

-create temp folder on same lvl as main-

pip3 install -r requirements.txt

uvicorn main:app --reload
or 
uvicorn main:app --host 192.168.56.1 --port 8000  
or 
uvicorn main:app --host 192.168.137.1 --port 8000

^
|
main network url 