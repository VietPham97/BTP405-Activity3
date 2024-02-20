from http.server import HTTPServer, BaseHTTPRequestHandler
import mysql.connector

cnx = mysql.connector.connect(user='admin', password='password', host='localhost', database='NoteDB')
cursor = cnx.cursor()

table_description = (
    "create table if not exists `NOTE` ("
    "  `NOTE_ID` int auto_increment not null,"
    "  `TITLE` varchar(14) not null,"
    "  `CONTENT` varchar(50) not null,"
    "  PRIMARY KEY (`NOTE_ID`))"
)

cursor.execute(table_description)

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        cursor.execute("SELECT note_id, title, content FROM NOTE")
        for (note_id, title, content) in cursor:
            self.wfile.write("{}, {}, {}".format(note_id, title, content).encode('utf-8'))

    def do_DELETE(self):
        self._set_response()
        cursor.execute("DELETE FROM NOTE")
        cnx.commit()

    def do_PUT(self):
        self._set_response()
        cursor.execute("INSERT INTO NOTE (TITLE, CONTENT) values ('Python', 'Python is fun.')")
        cnx.commit()

    def do_POST(self):
        self._set_response()
        cursor.execute("UPDATE NOTE SET CONTENT = 'Python is amazing!' WHERE TITLE = 'Python'")
        cnx.commit()


def run(server_class=HTTPServer, handler_class=SimpleRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping httpd server..')


if __name__ == '__main__':
    run()

cursor.close()
cnx.close()
