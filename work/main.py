import time
from work.page import InchLv


def main():
    start_time = time.time()
    print(InchLv.get_data())
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
