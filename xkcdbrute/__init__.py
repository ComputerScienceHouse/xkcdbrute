import xkcdbrute.brutus
import xkcdbrute.caesar
import sys


def run_client():
    if len(sys.argv) > 1:
        server = sys.argv[1]
        brutus.main(server)

def run_server():
    caesar.main()

