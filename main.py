import random
import time


# CATEGORY LISTS


all_emojis = [
    "🔥", "💀", "😂", "😳", "😱", "✨",
    "🚀", "🤡", "🐱", "🐶", "🌟", "🎤",
]

# ----- FUNNY -----
subjects_funny = [
    "A random kid",
    "A confused uncle",
    "A cat wearing sunglasses",
    "A talking potato",
    "Waleed",
    "A smart refrigerator",
]

actions_funny = [
    "is dancing like a robot",
    "is running like Naruto",
    "is arguing with a lamp",
    "is trying to fly",
    "is eating samosas in slow motion",
    "is teaching maths to aliens",
]

places_funny = [
    "on the moon",
    "inside a fridge",
    "in a moving bus",
    "at the barber shop",
    "outside KFC",
    "in a haunted classroom",
]

# ----- POLITICAL -----
subjects_political = [
    "Nawaz Sharif",
    "Imran Khan",
    "Donald Trump",
    "Joe Biden",
    "General Asim Munir",
    "Bilawal Bhutto",
]

actions_political = [
    "is giving an unexpected speech",
    "is launching a new political party",
    "is stuck in traffic",
    "is arguing with reporters",
    "is announcing a new policy",
    "is drinking chai peacefully",
]

places_political = [
    "at Parliament",
    "at a press conference",
    "at the Prime Minister House",
    "in Dubai",
    "at a jalsa",
    "at the border",
]

# ----- CELEBRITY -----
subjects_celebrity = [
    "Shahrukh Khan",
    "Salman Khan",
    "Virat Kohli",
    "Cristiano Ronaldo",
    "Elon Musk",
    "Taylor Swift",
]

actions_celebrity = [
    "is launching a new product",
    "is dancing on stage",
    "is shocking fans",
    "is giving autographs",
    "is training for a movie",
    "is trending on social media",
]

places_celebrity = [
    "in Mumbai",
    "in Hollywood",
    "inside a stadium",
    "on Instagram Live",
    "at an award show",
    "in Dubai Mall",
]

# ----- ANIMAL -----
subjects_animal = [
    "A cat",
    "A dog",
    "A lion",
    "A goat",
    "A dancing monkey",
    "A flying pigeon",
]

actions_animal = [
    "is stealing food",
    "is scaring everyone",
    "is doing backflips",
    "is sleeping peacefully",
    "is chasing a bike",
    "is teaching tricks to humans",
]

places_animal = [
    "in the zoo",
    "on the rooftop",
    "on the road",
    "in the park",
    "in a classroom",
    "at a wedding",
]

def funny_news():
    subject = random.choice(subjects_funny)
    action = random.choice(actions_funny)
    place_or_thing = random.choice(places_funny)
    emoji = random.choice(all_emojis)
    headline = f"\n{subject} {action} {place_or_thing} {emoji}"
    print(headline)
    return headline

def political_news():
    subject = random.choice(subjects_political)
    action = random.choice(actions_political)
    place_or_thing = random.choice(places_political)
    emoji = random.choice(all_emojis)
    headline = f"\n{subject} {action} {place_or_thing} {emoji}"
    print(headline)
    return headline

def celebrity_news():
    subject = random.choice(subjects_celebrity)
    action = random.choice(actions_celebrity)
    place_or_thing = random.choice(places_celebrity)
    emoji = random.choice(all_emojis)
    headline = f"\n{subject} {action} {place_or_thing} {emoji}"
    print(headline)
    return headline

def animal_news():
    subject = random.choice(subjects_animal)
    action = random.choice(actions_animal)
    place_or_thing = random.choice(places_animal)
    emoji = random.choice(all_emojis)
    headline = f"\n{subject} {action} {place_or_thing} {emoji}"
    print(headline)
    return headline

def save_headline(headline):
    time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("headlines.txt", "a", encoding="utf-8") as file:
        file.write(f"Saved on {time1}:\n")
        file.write(headline + "\n")
    print("Headline saved successfully! 💾")

# Start random news generator
last_headline = ""

while True:
    print("\nWelcome to the Random News Headline Generator!")
    print("Please choose a category (1-4):")
    print("1.Funny News \n2.Political news \n3.Celebrity News \n4.Animal News")
    choice = int(input("Enter the number of your choice (1-4): ").strip())

    if choice == 1:
        last_headline = funny_news()

    elif choice == 2:
        last_headline = political_news()

    elif choice == 3:
        last_headline = celebrity_news()

    elif choice == 4:
        last_headline = animal_news()

    else:
        print("Invalid choice. Please select a number between 1 and 5.")
        continue

    save_headline_option = input("\nDo you want to save the last generated headline? (yes/no): ").strip()
    if save_headline_option.lower() == "yes":
        if last_headline == "":
            print("\n⚠ No headline generated yet! Generate one first.")
        else:
            save_headline(last_headline)
    else:
        print("Headline not saved.....As you wish!")

    another = input("\nDo you want to generate another headline? (yes/no): ").strip()
    if another.lower() == "no":
        break

print("Thanks for using the Random News Headline Generator!. Have a great day!")
