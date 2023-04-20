from search import *
from vcl import VCL


def main():
    problema_vcl = VCL((3, 3, 'STANGA', 0, 0), (0, 0, 'DREAPTA', 3, 3))
    path = breadth_first_tree_search(problema_vcl).solution()
    print(path, '\n')


if __name__ == "__main__":
    main()
