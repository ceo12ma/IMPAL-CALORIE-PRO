from xmlrpc.server import SimpleXMLRPCServer

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

# Membuat server RPC
server = SimpleXMLRPCServer(("localhost", 8000))
print("Server berjalan di localhost:8000")

# Mendaftarkan fungsi untuk RPC
server.register_function(add_numbers, "add")
server.register_function(subtract_numbers, "subtract")

# Menjalankan server
server.serve_forever()
