from http.server import HTTPServer, CGIHTTPRequestHandler

port = input("Port: ")

if port == "":
	print("Port will be 8080.")
	port = "8080"

try:
	server_data = ("localhost", int(port))	
except:
	print("Port will be 8080.")
	server_data = ("localhost", 8080)	

server = HTTPServer(server_data, CGIHTTPRequestHandler)
server.serve_forever()