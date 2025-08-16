from random import randint

print("🎯 Welcome to Guess The Number Game!")
print("I have picked a number between 1 and 100. Can you guess it?")

# Generate a random number between 1 and 100
random_number = randint(1, 100)
# print(random_number)  # Uncomment for debugging

guesses = 0

while True:
    user_input = input("Enter your guess (1-100): ")
    guesses += 1

    # Check if input is numeric
    if not user_input.isdigit():
        print("❌ Please enter a valid number!")
        continue

    # Convert input to integer
    guess = int(user_input)

    # Check range
    if guess < 1 or guess > 100:
        print("⚠️ Enter a number between 1 and 100.")
        continue

    # Compare guesses
    if guess == random_number:
        print(f"✅ You win! 🎉 You guessed the number {guess} correctly in {guesses} attempts.")
        break
    elif guess > random_number:
        print("📉 Too high! Try a smaller number.")
    else:
        print("📈 Too low! Try a larger number.")
