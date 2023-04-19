import pymongo


def insert_one(input, output, database):
    input_data = {"input": input}
    count = database.count_documents(input_data)
    print(count)
    input_data["count"] = count
    input_data["output"] = output
    database.insert_one(input_data)
    return "The data has been inserted into the database successfully."


def find_all(database):
    data_set = []
    try:
        for data in database.find():
            # print(data)
            data_set.append({data["input"], data["output"]})
        return data_set
    except:
        return "Query failed."


def find_one(input, database):
    data = database.find_one({"input": input})
    return {data["input"], data["output"]}


def delete_one(input, database):
    try:
        database.delete_one({"input": input})
        return "Delete successfully."
    except:
        return "Delete failed."


if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://8.219.62.112:27017/")
    mydb = myclient["OSS"]
    mycol = mydb["data"]
    # insert_one("6-7-8-10", "out", mycol)
    delete_one("6-7-8-10", mycol)
    print(find_all(mycol))
    # print(find_one("6-7-8-9", mycol))
