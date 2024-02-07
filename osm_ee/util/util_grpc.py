from base64 import b64decode
import logging
import ssl
from .util_kubernetes import get_secret_data

logger = logging.getLogger("osm_ee.util_grpc")
SERVER_CERT_SECRET = "ee-tls"
CLIENT_CA_SECRET = "osm-ca"
SERVER_CERT_FILE = "/etc/ssl/ee-tls.crt"
SERVER_KEY_FILE = "/etc/ssl/ee-tls.key"
CLIENT_CA_FILE = "/etc/ssl/osm-ca.crt"


def create_secure_context() -> ssl.SSLContext:
    # retrieve certificates from secrets
    if not _retrieve_certs():
        logger.warning("TLS Certificates not found, starting gRPC server in unsecure mode")
        return None
    # create SSL context
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.verify_mode = ssl.CERT_REQUIRED
    ctx.load_cert_chain(SERVER_CERT_FILE, SERVER_KEY_FILE)
    ctx.load_verify_locations(CLIENT_CA_FILE)
    ctx.set_ciphers('ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20')
    ctx.set_alpn_protocols(['h2'])
    return ctx


def _retrieve_certs():
    _server_data = get_secret_data(SERVER_CERT_SECRET)
    lcm_ca = get_secret_data(CLIENT_CA_SECRET).get("ca.crt")
    if not (_server_data and lcm_ca):
        return False
    server_cert = _server_data.get("tls.crt")
    with open(SERVER_CERT_FILE, "w") as server_cert_file:
        server_cert_file.write(b64decode(server_cert).decode())
    server_key = _server_data.get("tls.key")
    with open(SERVER_KEY_FILE, "w") as server_key_file:
        server_key_file.write(b64decode(server_key).decode())
    with open(CLIENT_CA_FILE, "w") as client_ca_file:
        client_ca_file.write(b64decode(lcm_ca).decode())
    return True
