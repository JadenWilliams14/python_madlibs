# Python Mad Libs Warm-Up Activity

# The Game will repeat until it is broken out of
while True:

    # Welcome message
    print("\nWelcome to Python Mad Libs!")
    print("Answer the following questions to create your very own silly story.\n")

    # Gather user inputs
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    # Build the story using an f-string
    story = (
        f"Today, I saw a {adjective} {noun} that decided to {verb} {adverb}.\n"
        "I couldn't believe my eyes!"
    )

    # Display the completed story
    print("\nHere is your story:")
    print(story)
    play_again = input("Do you want to play again? (If so, type yes): ")

    # leaves the while loop if the user answers anything besides 'yes'
    if play_again != 'yes':
        break

print('\nFarewell! Thank you for playing!')
