def wrapper(f):
    def fun(list_of_nums):
        """
        7895462130      10
        9195969878      10
        9100256236      10
        07895462130     11
        09191919191     11
        919875641230    12
        +919875641230   13
        +919593621456   13
        """
        pass
        # Assignment

    return fun


@wrapper
def sort_phone(list_of_phone_numbers):
    print(*sorted(list_of_phone_numbers), sep="\n")


if __name__ == "__main__":
    # l = [input() for _ in range(int(input()))]
    nums = [
        "9195969878",
        "07895462130",
        "919875641230",
        "+919875641230",
        "09191919191",
        "9100256236",
        "+919593621456",
    ]
    sort_phone(nums)