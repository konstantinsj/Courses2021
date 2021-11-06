import time
from work.page import InchLv


def main():
    start_time = time.time()
    page = InchLv()
    result = page.get_data(subdistricts="Pļavnieki", deal_type="rent")
    page.close()
    print(result)
    with open("result.txt", mode="w", encoding="utf-8") as w:
        w.writelines(str(result))
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
