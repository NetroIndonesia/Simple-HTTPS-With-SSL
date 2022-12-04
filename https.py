import http.server, socketserver, socket, ssl

PORT = 443
HOST = socket.gethostname()

Handler = http.server.SimpleHTTPRequestHandler
https = socketserver.TCPServer(("0.0.0.0", PORT), Handler)
https.socket = ssl.wrap_socket(https.socket, keyfile='./key.pem', certfile='./cert.pem', server_side=True, ssl_version=ssl.PROTOCOL_TLSv1_2, ca_certs=None, do_handshake_on_connect=True, suppress_ragged_eofs=True, ciphers='ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSK')

print("Listening to port", PORT, "from", HOST)
https.server_forever()
