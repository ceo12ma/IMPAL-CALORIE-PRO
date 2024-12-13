import xmlrpc.client

# Terhubung ke server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Memanggil fungsi RPC
print("Penjumlahan: 5 + 3 =", proxy.add(5, 3))
print("Pengurangan: 10 - 7 =", proxy.subtract(10, 7))
