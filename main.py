import os
import ollama
import pandas as pd


images = [file for file in os.listdir("./images") if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

print(f" List of availible images to analyse: {images}")

#printing list of images to analyse with index values
print("Index  | Image name                   |")
for image in images:
    index = images.index(image)+1
    print(f"   {index}   | {image}")



def analysingfood(image):
    print(f"Analysing Image: {image}")
    response = ollama.chat(
    model="llava:7b",
        messages = [{
            "role": "user",
            "Content": "Find a meal and described what it contains only, not other descriptions required ",
        "images": [f"./images/{image}"]
        }])
    meal_description = response["message"]["content"]
    print(f"Meal Description: ", meal_description)
    res_calories = ollama.chat(
        model="llama3.1:8b",
        messages=[{
            "role": "user",
            "content": f"Read ingredients and estimate calories and return it as json: {meal_description}"
        }])
    calories_response = res_calories["message"]["content"]
    print(f"Calories for the meal: {image} is: {calories_response}")

while True:
    try:
        selection = int(input("Select the image to analyse:"))
        if selection & 1 < selection < (len(images) + 1):
            analysingfood(images[selection - 1])
            break
    except ValueError:
        print("Select a index # number only")
        print(len(images))
