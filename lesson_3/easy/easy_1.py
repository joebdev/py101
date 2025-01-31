# 1. 
# Yes, because numbers[6] doesn't exist

# 2. 
str1 = 'Come over here!'
str2 = "What's up, Doc?"

print(str1.endswith('!'))
print(str2.endswith('!'))

# 3. 
famous_words = "seven years ago..."
whole_quote = "Four score and " + famous_words
string_quote = f'Four score and {famous_words}'

# 4. 
munsters_description = "the Munsters are CREEPY and Spooky."
print(munsters_description.capitalize())

# 5. 
munsters_description = "The Munsters are creepy and spooky."
munsters_description.swapcase()

# 6. 
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

print("Dino" in str1)
print("Dino" in str2)

# 7. 
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")
print(flintstones)

# 8. 
flintstones.extend(["Hoppy", "Some Other Dino" ])
print(flintstones)

# 9.
advice = "Few things in life are as important as house training your pet dinosaur."
find_house = advice.index('house')
print(find_house)
print(advice[0:39])
# or
print(advice.split("house")[0])

# 10. 
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace('important', 'urgent'))