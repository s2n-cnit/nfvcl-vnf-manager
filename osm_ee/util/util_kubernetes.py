from kubernetes import client, config
from kubernetes.client.rest import ApiException


def get_secret_data(name) -> dict:
    # assume that we are executing in a kubernetes pod
    try:
        config.load_incluster_config()
    except config.ConfigException:
        # we are not running in kubernetes
        return {}
    # Read the namespace from the service account
    current_namespace = open("/var/run/secrets/kubernetes.io/serviceaccount/namespace").read()

    v1 = client.CoreV1Api()
    try:
        secret = v1.read_namespaced_secret(name, current_namespace)
    except ApiException as e:
        if e.reason == 'Not Found':  # Backwards compatibility: we run in k8s but certs don't exist
            return {}
        else:
            raise
    return secret.data
