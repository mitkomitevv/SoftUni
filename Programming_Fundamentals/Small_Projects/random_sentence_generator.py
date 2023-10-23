import random

names = ["Ivan", "Maria", "Georgi", "Stefani", "Dimitar", "Viktoria", "Nikolai", "Elena", "Petar", "Mitko",
         "Alice", "James", "Emma", "John", "Sophia", "Robert", "Isabella", "William", "Olivia", "Michael"]

places = ["Sofia", "Plovdiv", "Varna", "Burgas", "Ruse", "Stara Zagora", "Pleven", "Dobrich", "Sliven", "Shumen",
          "New York", "Paris", "London", "Tokyo", "Sydney", "Berlin", "Rome", "Beijing", "Madrid", "Toronto"]

verbs = ["runs", "jumps", "sings", "dances", "writes", "reads", "speaks", "listens", "cooks", "eats",
         "sleeps", "walks", "plays", "works", "studies", "swims", "drives", "draws", "watches", "laughs"]

nouns = ["book", "pen", "computer", "dog", "city", "car", "tree", "ocean", "mountain", "shoe",
         "phone", "desk", "chair", "bird", "flower", "river", "sky", "cloud", "star", "apple"]

adverbs = ["quickly", "silently", "eagerly", "rarely", "often", "always", "sometimes", "loudly", "gently", "briskly",
           "slowly", "happily", "sadly", "gracefully", "easily", "hardly", "never", "usually", "recently", "suddenly"]

details = ["near the river", "at home", "in the park", "far from home", "in the office", "on the beach",
           "under the tree", "beside the lake", "on the mountain", "by the window", "across the street",
           "next to the school", "in front of the building", "behind the fence", "among the crowd",
           "above the clouds", "below the bridge", "along the road", "through the woods", "around the corner"]

def get_random_word(words):
    return random.choice(words)
input("Helo, this is your first random sentence! Please click [Enter].")


while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}")
    input("Click [Enter] to generate a new one.")
