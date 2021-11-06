import time
from work.page import InchLv


def main():
    start_time = time.time()
    page = InchLv()
    print(page.get_data())
    page.close()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
