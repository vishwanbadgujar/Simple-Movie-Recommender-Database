import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

data_file = "movies_data.json"

def read_stuff():
    if not os.path.isfile(data_file):
        return []
    try:
        with open(data_file, "r") as f:
            return json.load(f)
    except:
        return []

def save_stuff(items_here):
    with open(data_file, "w") as f:
        json.dump(items_here, f, indent=4)

def add_movie_now():
    mv_name = input("Movie name: ")
    mv_type = input("Genre: ")
    mv_text = input("Short description: ")

    bunch = read_stuff()
    next_id_num = len(bunch) + 1

    bunch.append({
        "id": next_id_num,
        "title": mv_name,
        "genre": mv_type,
        "desc": mv_text
    })

    save_stuff(bunch)
    print("\nAdded.\n")

def see_all():
    arr = read_stuff()
    if not arr:
        print("\nNothing saved.\n")
        return

    print("\nSaved Movies:")
    for x in arr:
        print(f"{x['id']}. {x['title']} | {x['genre']}")
    print()

def change_info():
    the_list = read_stuff()
    see_all()

    try:
        which_one = int(input("ID to update: "))
    except:
        print("\nInvalid.\n")
        return

    for thing in the_list:
        if thing["id"] == which_one:
            thing["title"] = input("New name: ")
            thing["genre"] = input("New genre: ")
            thing["desc"] = input("New description: ")
            save_stuff(the_list)
            print("\nUpdated.\n")
            return

    print("\nNot found.\n")

def wipe_movie():
    items_tmp = read_stuff()
    see_all()

    try:
        gone_id = int(input("ID to delete: "))
    except:
        print("\nInvalid.\n")
        return

    cleaned = []
    for i in items_tmp:
        if i["id"] != gone_id:
            cleaned.append(i)

    save_stuff(cleaned)
    print("\nDeleted.\n")

def suggest_movies():
    all_data = read_stuff()
    if len(all_data) < 2:
        print("\nAdd more movies first.\n")
        return

    see_all()

    try:
        pick_id = int(input("Pick movie ID: "))
    except:
        print("\nInvalid.\n")
        return

    picked_item = None
    for d in all_data:
        if d["id"] == pick_id:
            picked_item = d
            break

    if picked_item is None:
        print("\nNot found.\n")
        return

    txts = [i["desc"] for i in all_data]

    tf_obj = TfidfVectorizer(stop_words="english")
    tf_mat = tf_obj.fit_transform(txts)

    sim_mat = cosine_similarity(tf_mat)
    row_num = pick_id - 1
    pair_scores = list(enumerate(sim_mat[row_num]))

    pair_scores = sorted(pair_scores, key=lambda z: z[1], reverse=True)
    pair_scores = pair_scores[1:6]

    print(f"\nSimilar to '{picked_item['title']}':\n")
    for idx, val in pair_scores:
        print(f"{all_data[idx]['title']} (Match: {round(val, 2)})")
    print()

def main():
    while True:
        print("\n=== Movie App ===")
        print("1. Add movie")
        print("2. Show all")
        print("3. Update movie")
        print("4. Delete movie")
        print("5. Recommend similar movies")
        print("0. Exit")

        ch = input("Choose: ")

        if ch == "1":
            add_movie_now()
        elif ch == "2":
            see_all()
        elif ch == "3":
            change_info()
        elif ch == "4":
            wipe_movie()
        elif ch == "5":
            suggest_movies()
        elif ch == "0":
            break
        else:
            print("\nTry again.\n")

if __name__ == "__main__":
    main()