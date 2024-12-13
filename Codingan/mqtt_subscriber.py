import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
port = 1883
topic = "test/topic"

def on_message(client, userdata, message):
    print(f"Pesan diterima: {message.payload.decode()} di topic {message.topic}")

# Membuat client
client = mqtt.Client()

# Mengatur callback untuk menerima pesan
client.on_message = on_message

# Menghubungkan ke broker
client.connect(broker, port)

# Berlangganan ke topic
client.subscribe(topic)
print("Berlangganan ke topic:", topic)

# Memulai loop untuk mendengarkan pesan
client.loop_forever()

