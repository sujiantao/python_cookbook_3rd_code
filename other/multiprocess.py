from concurrent.futures import ProcessPoolExecutor

from pymongo import MongoClient

from conf import run_config

client = MongoClient(run_config.MONGODB_URI)
db = client[run_config.MONGODB_DB]
t1 = 1


def run():
    with ProcessPoolExecutor(max_workers=3) as executor:
        executor.submit(process_one)
        executor.submit(process_one)
    print("done")


def process_one():
    # print(id(t1))
    print(t1 + 1)
    print(id(client))
    print(id(db))
    print(t1)


if __name__ == "__main__":
    run()

