import threading
from underthesea import pos_tag
import json
import math

input_content = "Rút kinh nghiệm tổ chức lễ hội bánh dân gian Nam bộ."

config = "config.json"
file_config = open(config)
data = json.load(file_config)
data_prepare = data["data_prepare"]

valid = [
    "N",
    "V",
    "A"
]


# get valid words in array
def get_valid_words(content):
    words = pos_tag(content)
    valid_words = []
    for word in words:
        type_of_word = word[1],
        content_of_word = word[0],

        if type_of_word[0] in valid:
            if len(content_of_word[0]) > 1:
                valid_words.append(str.lower(str(content_of_word[0])))

    return valid_words


# All document in dataset
num_documents = 800


def tf(t, d):
    return d.count(t)


def df(t):
    count = 0
    for item in data_prepare:
        path = item["path_file"]
        data_categories = json.load(open(path, encoding='utf-8'))
        documents = data_categories["documents"]
        for document in documents:
            words = document["words"]
            if t in words:
                count = count + 1
    return count


def idf(t):
    term = df(t)
    return math.log((num_documents + 1) / (term + 1), 10)


category_result = ""
score_result = 0


class WorkerThread(threading.Thread):
    def __init__(self, data, category):
        threading.Thread.__init__(self)
        self.data = data
        self.category = category

    def run(self):
        data_categories = json.load(open(self.data, encoding='utf-8'))
        documents = data_categories["documents"]
        score = 0
        for document in documents:
            words = document["words"]
            input_words = get_valid_words(input_content)
            for t in input_words:
                tf_idf = tf(t, words) * idf(t)
                score = score + tf_idf
        print(self.category)
        print(score)


t1 = WorkerThread("data-prepare/business.json", "business")
t2 = WorkerThread("data-prepare/car.json", "car")
t3 = WorkerThread("data-prepare/education.json", "education")
t4 = WorkerThread("data-prepare/health.json", "health")
t5 = WorkerThread("data-prepare/law.json", "law")
t6 = WorkerThread("data-prepare/science.json", "science")
t7 = WorkerThread("data-prepare/sport.json", "sport")
t8 = WorkerThread("data-prepare/travel.json", "travel")
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
