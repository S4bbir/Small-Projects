import time

phrase = "Python is the best coding language."
word_count = len(phrase.split())

print(f"Type this fast: \n{phrase}\n")
input(f"Press enter to start.")

start_time = time.time()
attempt = input(f"Type here: ")
end_time = time.time()

time_taken = (end_time - start_time) / 60
wpm = round(word_count / time_taken, 2)

if attempt == phrase or attempt == phrase.lower():
    print(f"\nSuccess! Your speedL {wpm} WPM")
else:
    print(f"\nTry again.")