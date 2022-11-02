import logging
import ssl

logger = logging.getLogger("osm_ee.util_grpc")

SERVER_CERT = "/etc/ssl/grpc-tls/tls.crt"
SERVER_KEY = "/etc/ssl/grpc-tls/tls.key"


def create_secure_context() -> ssl.SSLContext:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # ctx.verify_mode = ssl.CERT_REQUIRED
    try:
        ctx.load_cert_chain(str(SERVER_CERT), str(SERVER_KEY))
    except FileNotFoundError:
        logger.warning("TLS Certificate not found, starting gRPC server in unsecure mode")
        return None
    # TODO: client TLS 
    # ctx.load_verify_locations(str(trusted))
    ctx.set_ciphers('ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM:DHE+CHACHA20')
    ctx.set_alpn_protocols(['h2'])
    try:
        ctx.set_npn_protocols(['h2'])
    except NotImplementedError:
        pass
    return ctx