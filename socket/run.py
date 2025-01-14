# Unix sockets are used to communicate between processes on the same machine.
import sys # which provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter, including the command-line arguments.

def main(argv):
    from transport.unixsocket import UNIXSocketTransport

    transport = UNIXSocketTransport()


    if argv[1] == 'server': # sys.argv is a list in Python, which contains the command-line arguments passed to the script.
        transport.run_server() #start a Unix socket server
    else:
        print (transport.run_cmd(' '.join(argv[1:])).to_json(indent=4)) #run a command on the server

if __name__ == '__main__':
    main(sys.argv)
