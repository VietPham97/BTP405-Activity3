# BTP405 - Activity 3
Student Name: Viet Pham

## Tools and Technologies
- Programming Language: Python
- Database: MySQL
- Version Control: Git
- Containerization: Docker
- API Testing: curl / Invoke-RestMethod (Windows)

## Config MySQL Docker
```
docker pull container-registry.oracle.com/mysql/community-server:latest
```
```
docker run --name=mysql1 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password --restart on-failure -d container-registry.oracle.com/mysql/community-server:latest
```

GET Request:
```
def do_GET(self):
    self._set_response()
    cursor.execute("SELECT note_id, title, content FROM NOTE")
    for (note_id, title, content) in cursor:
        self.wfile.write("{}, {}, {}".format(note_id, title, content).encode('utf-8'))
```
Test command (Windows PowerShell):
```
Invoke-RestMethod -Uri localhost:8080 
```
Test command (curl):
```
curl 127.0.0.1:8080 
```

DELETE Request:
```
def do_DELETE(self):
    self._set_response()
    cursor.execute("DELETE FROM NOTE")
    cnx.commit()
```
Test command (Windows PowerShell):
```
Invoke-RestMethod -Uri localhost:8080 -Method DELETE 
```
Test command (curl):
```
curl -X DELETE 127.0.0.1:8080 
```

PUT Request:
```
def do_PUT(self):
    self._set_response()
    cursor.execute("INSERT INTO NOTE (TITLE, CONTENT) values ('Python', 'Python is fun.')")
    cnx.commit()
```
Test command (Windows PowerShell):
```
Invoke-RestMethod -Uri localhost:8080 -Method PUT 
```
Test command (curl):
```
curl -X PUT 127.0.0.1:8080 
```

POST Request:
```
def do_POST(self):
    self._set_response()
    cursor.execute("UPDATE NOTE SET CONTENT = 'Python is amazing!' WHERE TITLE = 'Python'")
    cnx.commit()
```
Test command (Windows PowerShell):
```
Invoke-RestMethod -Uri localhost:8080 -Method POST 
```
Test command (curl):
```
curl -X POST 127.0.0.1:8080 
```

Build a docker image:
```
docker build -t vietpham/notetaker:v1 .
``` 
Run a docker container:
```
docker run -p 8080:8080 vietpham/notetaker:v1
```
