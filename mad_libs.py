# Python Mad Libs Warm-Up Activity
# import to use random on list of words.
import random

# The Game will repeat until it is broken out of
while True:

    # Welcome message
    print("\nWelcome to Python Mad Libs!")
    print("Answer the following questions to create your very own silly story.\n")

    # Gather user inputs
    adjective = input("Enter a comma seperated list of adjectives: ")
    noun = input("Enter a comma seperated list of nouns: ")
    verb = input("Enter a comma seperated list of verbs: ")
    adverb = input("Enter a comma seperated list of adverbs: ")

    # Build the story using an f-string
    # random.choice is selecting a random option from the list that is created by splitting on the commas
    story = (
        f"Today, I saw a {random.choice(adjective.split(','))} {random.choice(noun.split(','))} that decided to {random.choice(verb.split(','))} {random.choice(adverb.split(','))}.\n"
        "I couldn't believe my eyes!"
    )

    # Display the completed story
    print("\nHere is your story:")
    print("""
*************************************************************
          """)
    print(story)
    print("""
*************************************************************
          """)

    # Take user input on if they want to play again
    play_again = input("Do you want to play again? (If so, type yes): ")

    # leaves the while loop if the user answers anything besides 'yes'
    if play_again != 'yes':
        break

print('\nFarewell! Thank you for playing!')
