import os
import ollama

images = [file for file in os.listdir("./images") if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

for image in images:
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


