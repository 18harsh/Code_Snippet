import socket
import threading
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

PORT = 5555
SERVER = socket.gethostbyname(socket.gethostname())
HEADER = 2048
FORMAT = 'utf-8'


try:
	s.bind((SERVER,PORT))
except socket.error as e:
	print(str(e))

currentId = "0"
pos = ["0:50,50", "1:100,100"]

def threaded_client(conn,addr):
	print(f"[NEW CONNECTION] {addr} connected.")
	global currentId, pos
	conn.send(str.encode(currentId))
	currentId = '1'
	reply = ''
	while True:
		try:
			data = conn.recv(HEADER)
			reply=data.decode(FORMAT)
			if not data:
				conn.send(str.encode("Goodbye"))
				break
			else:
				print("Recieved: "+ reply)
				arr = reply.split(":")
				id = int(arr[0])
				pos[id] = reply
				if id == 0: nid = 1
				if id == 1: nid = 0

				reply = pos[nid][:]
				print("sending: " + reply)

			conn.sendall(str.encode(reply))
		except:
			pass
	print("Connection Closed")
	conn.close()		


def start():
	s.listen(2)
	print(f"[LISTENING] Server is listening on {SERVER}")
	while True:
		conn, addr = s.accept()
		thread = threading.Thread(target=threaded_client, args=(conn, addr))
		thread.start()
		print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()	