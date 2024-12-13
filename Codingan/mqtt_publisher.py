import paho.mqtt.client as mqtt

broker = "test.mosquitto.org"
port = 1883
topic = "test/topic"

# Membuat client
client = mqtt.Client()

# Menghubungkan ke broker
client.connect(broker, port)

# Mengirim pesan
client.publish(topic, "Hello, MQTT!")
print("Pesan dikirim ke topic:", topic)

# Disconnect
client.disconnect()
