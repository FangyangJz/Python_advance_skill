import sys
import socket
# import getopt
import argparse
import threading
import subprocess

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


# def usage():
#     print("BHP Net Tool\n")
#     print("Usage: ex04_netcat.py -t target_host -p port\n")
#     print("-l --listen \t - listen on [host]:[port] for incoming connections")
#     print("-e --execute=file_to_run \t - execute the given file upon receiving a connection")
#     sys.exit(0)


def main():
    global listen, port, execute, command, upload_destination, target
    # if not len(sys.argv[1:]):
    #     usage()
    parser = argparse.ArgumentParser()
    parser.description = "This is a hand design netcat"
    parser.add_argument(
        "-l", "--listen",
        help="listen on [host]:[port] for incoming connections",
        type=
    )


if __name__ == "__main__":
    main()
