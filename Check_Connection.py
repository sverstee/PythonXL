import socket

def is_connected():
    print("testing connection")
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

    ## Call is connected
    ## is_connected()

    if __name__ == '__main__':
        is_connected()
        print("Testing Connection)")
        "This only executes when %s is executed rather than imported" % __file__
