import random
import time

EMOJIS = [
    "🔥", "💀", "😂", "😳", "😱", "✨",
    "🚀", "🤡", "🐱", "🐶", "🌟", "🎤",
]

CATEGORIES = {
    "1": {
        "name": "Funny News",
        "subjects": [
            "A random kid",
            "A confused uncle",
            "A cat wearing sunglasses",
            "A talking potato",
            "Waleed",
            "A smart refrigerator",
        ],
        "actions": [
            "is dancing like a robot",
            "is running like Naruto",
            "is arguing with a lamp",
            "is trying to fly",
            "is eating samosas in slow motion",
            "is teaching maths to aliens",
        ],
        "places": [
            "on the moon",
            "inside a fridge",
            "in a moving bus",
            "at the barber shop",
            "outside KFC",
            "in a haunted classroom",
        ],
    },
    "2": {
        "name": "Political News",
        "subjects": [
            "Nawaz Sharif",
            "Imran Khan",
            "Donald Trump",
            "Joe Biden",
            "General Asim Munir",
            "Bilawal Bhutto",
        ],
        "actions": [
            "is giving an unexpected speech",
            "is launching a new political party",
            "is stuck in traffic",
            "is arguing with reporters",
            "is announcing a new policy",
            "is drinking chai peacefully",
        ],
        "places": [
            "at Parliament",
            "at a press conference",
            "at the Prime Minister House",
            "in Dubai",
            "at a jalsa",
            "at the border",
        ],
    },
    "3": {
        "name": "Celebrity News",
        "subjects": [
            "Shahrukh Khan",
            "Salman Khan",
            "Virat Kohli",
            "Cristiano Ronaldo",
            "Elon Musk",
            "Taylor Swift",
        ],
        "actions": [
            "is launching a new product",
            "is dancing on stage",
            "is shocking fans",
            "is giving autographs",
            "is training for a movie",
            "is trending on social media",
        ],
        "places": [
            "in Mumbai",
            "in Hollywood",
            "inside a stadium",
            "on Instagram Live",
            "at an award show",
            "in Dubai Mall",
        ],
    },
    "4": {
        "name": "Animal News",
        "subjects": [
            "A cat",
            "A dog",
            "A lion",
            "A goat",
            "A dancing monkey",
            "A flying pigeon",
        ],
        "actions": [
            "is stealing food",
            "is scaring everyone",
            "is doing backflips",
            "is sleeping peacefully",
            "is chasing a bike",
            "is teaching tricks to humans",
        ],
        "places": [
            "in the zoo",
            "on the rooftop",
            "on the road",
            "in the park",
            "in a classroom",
            "at a wedding",
        ],
    },
}


def build_headline(category):
    subject = random.choice(category["subjects"])
    action = random.choice(category["actions"])
    place = random.choice(category["places"])
    emoji = random.choice(EMOJIS)
    return f"{subject} {action} {place} {emoji}"


def show_menu():
    print("\nRandom News Headline Generator")
    print("Choose a category:")
    for key, category in CATEGORIES.items():
        print(f"{key}. {category['name']}")


def choose_category():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()
        if choice in CATEGORIES:
            return CATEGORIES[choice]
        print("Invalid choice. Please select a number between 1 and 4.")


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"yes", "y"}:
            return True
        if answer in {"no", "n"}:
            return False
        print("Please answer yes or no.")


def save_headline(headline):
    saved_at = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open("headlines.txt", "a", encoding="utf-8") as file:
        file.write(f"Saved on {saved_at}:\n{headline}\n\n")
    print("Headline saved successfully!")


def main():
    while True:
        category = choose_category()
        headline = build_headline(category)

        print("\nGenerated headline:")
        print(headline)

        if ask_yes_no("\nDo you want to save this headline? (yes/no): "):
            save_headline(headline)
        else:
            print("Headline not saved.")

        if not ask_yes_no("\nDo you want to generate another headline? (yes/no): "):
            break

    print("Thanks for using the Random News Headline Generator!")


if __name__ == "__main__":
    main()
