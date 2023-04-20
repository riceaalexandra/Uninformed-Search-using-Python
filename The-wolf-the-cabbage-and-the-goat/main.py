from search import *
from vcl import VCL


def main():
    problema_vcl = VCL((1, 1, 1, 'STANGA', 0, 0, 0), (0, 0, 0, 'DREAPTA', 1, 1, 1))
    path = breadth_first_tree_search(problema_vcl).solution()
    print(path, '\n')


if __name__ == "__main__":
    main()
