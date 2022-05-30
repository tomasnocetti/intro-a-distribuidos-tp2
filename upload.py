from threading import Thread
from client.client_upload import ClientUploadConnection
from client.client_utils import build_upload_parser
from transport_tcp.connection import Connection

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65433  # The port used by the server
BUFFER_SIZE = 508


def main():
    args = build_upload_parser().parse_args()

    server_port = int(args.port)
    source_file_path = args.src
    file_name_dst = args.name

    print("[ INFO ] - Got server port: {}".format(server_port))
    print("[ INFO ] - Got source file path: {}".format(source_file_path))
    print("[ INFO ] - Got file name: {}".format(file_name_dst))

    connection = Connection.connect(HOST, server_port)
    print("[ INFO ] - Nueva conexión generada con el servidor")

    client_upload = ClientUploadConnection(
        connection,
        file_name_dst,
        source_file_path
    )

    thread = Thread(target=client_upload.run)
    thread.start()
    user_input = input()

    while user_input != "q":
        user_input = input()

    print(
        "[ INFO ] - Comienzo cierre de conexión con servidor."
        "Joineando threads."
    )
    client_upload.close()
    thread.join()
    print("[ INFO ] - Thread joineados exitosamente! Terminando programa.")

    return 0


main()


# def main():
#     # while(True):
#     # s.sendto(b"NCLIENTE NUEVO", (HOST, PORT))
#     connection = Connection.connect(HOST, PORT)
#     print("[ NUEVA CONEXION ]")
#     sleep(100000)
#     print(str(connection))
#     # (recvData, serverAddress) = s.recvfrom(BUFFER_SIZE)

#     # Poner validacion de que solo el servidor me mande mensajes

#     # s.sendto(b"C", (HOST, PORT))
#     # (recvData, serverAddress) = s.recvfrom(BUFFER_SIZE)

#     # print("[ PROTOCOL ACK ] - ", str(recvData))


# main()
# print(f"Received {data!r}")
