from browsermobproxy import Server, Client
server = Server(r"C:\Program Files (x86)\browsermob-proxy-2.1.4\bin\browsermob-proxy",)
server.start()
client = Client("localhost:8080")
print(client.port)
print(server.port)
client.new_har('google')
print(client.har)