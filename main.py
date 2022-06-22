from requests import delete


clients = "pablo, ricardo, "
clients = clients.upper()

def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        print("Client is already created")


def list_clients():
    global clients
    print(clients.upper())


def update_client(client_name):
    global clients
    if client_name in clients:
        updated_client_name = input("What is the updated client name: ").upper()
        clients = clients.replace(client_name + ", ", updated_client_name + ", ")
    elif client_name not in clients:
        _client_not_found()


def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name +  ", ", "")
    else:
        _client_not_found()


def _add_coma():
    global clients
    clients += ", "


def _print_welcome():
    print("Welcome to Platzi Ventas")
    print("*" * 50)
    print("What do you like to do today?")
    print("[C]reate client")
    print("[U]pdate client")
    print("[D]elete client")


def _get_client_name():
    return input("What is the client name: ").upper()


def _client_not_found():
    return print("Client is not in clients list")


if __name__ == "__main__":
    _print_welcome()

    command = input().upper()
    if command == "C":
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == "D":
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == "U":
        client_name = _get_client_name()
        update_client(client_name)
        list_clients()
    else:
        print("Invalid command")

