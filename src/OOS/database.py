import pymongo


def insert_one(input, output, database):
    try:
        input_data = {"input": input, "output": output}
        database.insert_one(input_data)
    except:
        return "The data had been inserted into the database."
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
        database.dete_one({"input": input})
        return "Delete successfully."
    except:
        return "Delete failed."


if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://8.219.62.112:27017/")
    mydb = myclient["OSS"]
    mycol = mydb["data"]
    print(find_all(mycol))
    insert_one("6-7-8-9", "output", mycol)
    print(find_one("6-7-8-9", mycol))
