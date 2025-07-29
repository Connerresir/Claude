import keyring

class Credentials:
    def set_credential(self, service_name, username, password):
        keyring.set_password(service_name, username, password)
        print(f"Credential for {username} on {service_name} has been set.")

    def get_credential(self, service_name, username):
        return keyring.get_password(service_name, username)
