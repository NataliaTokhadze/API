import requests
import csv

url = "https://the-cocktail-db3.p.rapidapi.com/45"

headers = {
	"X-RapidAPI-Key": "e4dae51515msh6f838bf6e9f69c1p1b221ejsn91ee8b271ba6",
	"X-RapidAPI-Host": "the-cocktail-db3.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

# print(response.json())

recipe = {
    "id": "45",
    "title": "Aperol spritz",
    "difficulty": "Easy",
    "portion": "Serves 6-8",
    "time": "Hands-on time 5 min",
    "description": "Get into the spirit of summer with this classic Italian recipe. Chilled prosecco and Aperol come together to create the beloved Aperol spritz.",
    "ingredients": [
        "750ml bottle of prosecco",
        "Bag of ice",
        "Bottle of Aperol",
        "Bottle of soda water",
        "Slice of orange"
    ],
    "method": [
        {"Step 1": "Chill the bottle of prosecco and Aperol in the fridge."},
        {"Step 2": "Fill 6 or 8 wine glasses or tall tumblers with a couple of ice cubes and roughly three parts prosecco to one part Aperol."},
        {"Step 3": "Add a splash of soda water and a slice of orange. Serve straightaway so that the fizz stays lively."}
    ],
    "image": "https://apipics.s3.amazonaws.com/coctails_api/45.jpg"
}

csv_filename = "recipe.csv"

with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(["Attribute", "Value"])
    
    for key, value in recipe.items():
        if isinstance(value, list):
            value = ', '.join(value)
        writer.writerow([key, value])
    
print(f"Done writing {c} entries to the csv file!")
csvfile.close()
