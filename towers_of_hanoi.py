def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    """
    return solver(num_disks, 'S', 'A', 'D')


def solver(num_disks, source, auxiliary, destination):

    if num_disks == 1:
        print("{} {}".format(source, destination))
        return

    solver(num_disks - 1, source, destination, auxiliary)
    print("{} {}".format(source, destination))
    solver(num_disks - 1, auxiliary, source, destination)


tower_of_Hanoi(3)
