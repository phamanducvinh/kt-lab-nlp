from underthesea import pos_tag
import numpy
import json

# Get all path of categories
config = "config.json"
file_config = open(config)
data = json.load(file_config);

# Get data
categories = data["categories"]
numCategories = len(categories)
numDocuments = data["documents"]

# get valid words in array
def get_valid_words(content):
    words = pos_tag(content, format='N')
    valid_words = []
    for word in words:
        type_of_word = word[1],
        content_of_word = word[0],

        if type_of_word[0] != "CH":
            if len(content_of_word[0]) > 1:
                valid_words.append(str.lower(str(content_of_word[0])))

    return valid_words

for item in categories:
    category = item["category"]
    path_file = item["path_file"]

    data_of_category = json.load(open(path_file, encoding='utf-8'))
    documents = data_of_category["documents"]

    documents_json = []
    for document in documents:
        content = document["content"]
        if len(content) > 1000:
            valid_words = get_valid_words(content)
            obj = {
                "category": category,
                "words": valid_words
            }
            documents_json.append(obj)
    with open(f"${category}.json", "w", encoding='utf-8') as f:
        f.write(json.dumps({
            "documents": documents_json
        }, ensure_ascii=False))
