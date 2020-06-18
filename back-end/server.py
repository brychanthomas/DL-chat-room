# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import cgi

import database, html_conversion as htmlc

hostName = "localhost"
serverPort = 8080

messagesDB = database.DB('data/messages.db')

with open("index.html", 'r') as indexFile:
    webpage = indexFile.read()


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            output = webpage
            self.wfile.write(output.encode())
        if 'get-messages' in self.path: #get messages from DB
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            output = ''
            messages = messagesDB.get_new_messages()
            messages = htmlc.conversion(messages)
            output += messages
            self.wfile.write(output.encode())

    def do_POST(self):
        if self.path.endswith('/new-message/'):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_message = fields.get('message')
                username = fields.get('username')
                messagesDB.add_message(username[0], new_message[0])
                print(new_message[0],'<-- Test(new_post[0])')
            self.send_response(201)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            output = ''
            output += 'Success!'
            self.wfile.write(output.encode())

        
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
