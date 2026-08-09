import csv
import random

diet_needs = [
    "weight_loss", "weight_gain", "bulking", 
    "maintaining_balanced_diet", "diabetes", 
    "high_bp", "high_cholesterol"
]

meal_types = ["breakfast", "lunch", "snack", "dinner"]

base_dishes = {
    "breakfast": [
        {"name": "Steamed Chila with Tomato Chutney", "base": "Rice flour, Tomato, Garlic", "type": "veg", "meat": "none"},
        {"name": "Fara (Steamed Rice Dumplings) with Green Chutney", "base": "Rice flour, Coriander, Chili", "type": "veg", "meat": "none"},
        {"name": "Muthia (Steamed Seasoned Dough) with Sesame Chutney", "base": "Rice flour, Sesame, Spices", "type": "veg", "meat": "none"},
        {"name": "Bore Basi with Onion and Green Chili", "base": "Fermented Rice, Onion, Chili", "type": "veg", "meat": "none"},
        {"name": "Angakar Roti with Mashed Eggplant", "base": "Rice flour, Eggplant, Onion", "type": "veg", "meat": "none"},
        {"name": "Hathphodwa with Dal", "base": "Rice flour, Lentils", "type": "veg", "meat": "none"},
        {"name": "Sabudana Khichdi with Peanuts", "base": "Sago, Peanuts, Potatoes", "type": "veg", "meat": "none"},
        {"name": "Bara (Urad Dal Vada)", "base": "Urad Dal, Spices", "type": "veg", "meat": "none"}
    ],
    "lunch": [
        {"name": "Rice + Dubki Kadi + Bhindi Sabzi", "base": "Rice, Besan, Curd, Okra", "type": "veg", "meat": "none"},
        {"name": "Rice + Aamat + Lal Bhaji", "base": "Rice, Mixed Veg, Bamboo shoot, Red Amaranth", "type": "veg", "meat": "none"},
        {"name": "Roti + Bafauri Curry + Kumhra Sabzi", "base": "Wheat, Chana Dal, Pumpkin", "type": "veg", "meat": "none"},
        {"name": "Rice + Kochai Patta Curry + Mooli Bhaji", "base": "Rice, Taro Leaves, Radish Leaves", "type": "veg", "meat": "none"},
        {"name": "Rice + Rakhiya Badi + Karela Sabzi", "base": "Rice, Ash Gourd, Urad Dal, Bitter Gourd", "type": "veg", "meat": "none"},
        {"name": "Roti + Jimikand Curry + Palak Sabzi", "base": "Wheat, Yam, Spinach", "type": "veg", "meat": "none"},
        {"name": "Rice + Bamboo Shoot (Karel) Sabzi + Urad Dal", "base": "Rice, Bamboo Shoot, Urad Dal", "type": "veg", "meat": "none"},
        {"name": "Roti + Desi Chicken Curry + Onion Salad", "base": "Wheat, Chicken, Onion, Spices", "type": "non-veg", "meat": "chicken"},
        {"name": "Rice + Machli (Local Fish) Curry + Tomato Chutney", "base": "Rice, Local Fish, Tomato, Mustard", "type": "non-veg", "meat": "fish"},
        {"name": "Rice + Egg Curry + Chech Bhaji", "base": "Rice, Egg, Local Greens", "type": "non-veg", "meat": "egg"},
        {"name": "Rice + Arhar Dal + Munga (Drumstick) Sabzi", "base": "Rice, Pigeon Pea, Drumstick", "type": "veg", "meat": "none"}
    ],
    "snack": [
        {"name": "Steamed Bafauri", "base": "Chana Dal, Spices", "type": "veg", "meat": "none"},
        {"name": "Murra (Puffed Rice) with Roasted Chana", "base": "Puffed Rice, Chickpeas", "type": "veg", "meat": "none"},
        {"name": "Roasted Mahua with Nuts", "base": "Mahua flowers, Almonds", "type": "veg", "meat": "none"},
        {"name": "Baked Dehati Vada", "base": "Urad Dal, Spices", "type": "veg", "meat": "none"},
        {"name": "Lai Badi (Dry Puffed Rice Badi)", "base": "Puffed Rice, Spices", "type": "veg", "meat": "none"},
        {"name": "Khurmi", "base": "Wheat, Jaggery", "type": "veg", "meat": "none"}
    ],
    "dinner": [
        {"name": "Multigrain Roti + Chana Dal + Kanda Bhaji", "base": "Wheat, Millet, Chana Dal, Sweet Potato Leaves", "type": "veg", "meat": "none"},
        {"name": "Rice + Rakhiya Badi + Palak Sabzi", "base": "Rice, Ash Gourd, Spinach", "type": "veg", "meat": "none"},
        {"name": "Roti + Dubki Kadi + Roasted Papita Sabzi", "base": "Wheat, Besan, Curd, Papaya", "type": "veg", "meat": "none"},
        {"name": "Rice + Fish Curry (Miroshi) + Onion Salad", "base": "Rice, Fish, Onion, Spices", "type": "non-veg", "meat": "fish"},
        {"name": "Roti + Munga Sabzi + Masoor Dal", "base": "Wheat, Drumstick, Lentils", "type": "veg", "meat": "none"},
        {"name": "Rice + Bafauri Sabzi + Cucumber Salad", "base": "Rice, Chana Dal, Cucumber", "type": "veg", "meat": "none"},
        {"name": "Roti + Chicken Curry (Low Oil) + Tomato Chutney", "base": "Wheat, Chicken, Tomato", "type": "non-veg", "meat": "chicken"}
    ]
}

def adjust_for_diet(dish, meal_type, diet_need, unique_seed):
    random.seed(unique_seed)
    
    if meal_type in ["breakfast", "snack"]:
        cal = random.randint(200, 350)
    else:
        cal = random.randint(400, 650)

    protein = cal * 0.15 / 4
    carbs = cal * 0.55 / 4
    fat = cal * 0.30 / 9
    fiber = random.randint(5, 12)
    gi = "Medium"
    sodium = "Medium"
    cholesterol = "Medium"
    exercise = "30 min moderate walking"
    warning = "No special warnings."
    instructions = "Cook using traditional methods with moderate oil. Steam where possible."
    dish_name = dish['name']

    if diet_need == "weight_loss":
        cal = int(cal * 0.8)
        carbs = cal * 0.4 / 4
        protein = cal * 0.3 / 4
        fat = cal * 0.3 / 9
        gi = "Low"
        exercise = "45 min cardio + HIIT"
        instructions = "Use minimal oil. Bake or steam instead of frying to reduce calorie intake."
        warning = "Monitor energy levels; do not skip meals."
        if "Rice" in dish_name and "Brown" not in dish_name and "Puffed" not in dish_name:
            dish_name = dish_name.replace("Rice", "Brown Rice")

    elif diet_need == "weight_gain":
        cal = int(cal * 1.3)
        carbs = cal * 0.5 / 4
        protein = cal * 0.2 / 4
        fat = cal * 0.3 / 9
        exercise = "30 min light strength training"
        instructions = "Add a spoonful of traditional ghee for healthy fats and extra calories."

    elif diet_need == "bulking":
        cal = int(cal * 1.4)
        protein = cal * 0.35 / 4
        carbs = cal * 0.45 / 4
        fat = cal * 0.20 / 9
        exercise = "60 min heavy strength training"
        instructions = "Increase portion sizes of protein sources. Include extra protein elements."

    elif diet_need == "diabetes":
        carbs = cal * 0.4 / 4
        protein = cal * 0.3 / 4
        fat = cal * 0.3 / 9
        fiber += 5
        gi = "Low"
        exercise = "20 min post-meal walking"
        instructions = "Ensure high fiber pairing. Do not overcook vegetables to maintain Low GI."
        warning = "Check fasting glucose regularly; avoid if post-meal exceeds 180 mg/dL."
        if "Rice" in dish_name and "Brown" not in dish_name and "Puffed" not in dish_name:
            dish_name = dish_name.replace("Rice", "Millet")
        if "Jaggery" in dish['base']:
            return None # Skip Khurmi for diabetes

    elif diet_need == "high_bp":
        sodium = "Low"
        exercise = "30 min light cardio + breathing exercises"
        instructions = "Do not add salt while eating. Use local herbs for flavor instead of sodium."
        warning = "Strictly avoid pickles, papads, and processed items with this meal."

    elif diet_need == "high_cholesterol":
        cholesterol = "Low"
        fat = cal * 0.2 / 9
        carbs = cal * 0.55 / 4
        protein = cal * 0.25 / 4
        fiber += 3
        exercise = "45 min steady state cardio"
        instructions = "Steam or boil instead of frying. Use zero cholesterol oils sparingly."
        warning = "Avoid adding butter or ghee to this meal."
        if "Egg" in dish_name:
            dish_name = dish_name.replace("Egg", "Egg White")

    elif diet_need == "maintaining_balanced_diet":
        gi = "Medium"
        sodium = "Medium"
        exercise = "30 min mixed activity"
        instructions = "Maintain a balanced portion of macros according to standard Chhattisgarh thali."

    # Validate macros ±10%
    actual_cals = (protein * 4) + (carbs * 4) + (fat * 9)
    if abs(actual_cals - cal) > cal * 0.1:
        # adjust carbs to fit
        carbs = (cal - (protein * 4) - (fat * 9)) / 4

    protein = max(round(protein, 1), 1.0)
    carbs = max(round(carbs, 1), 1.0)
    fat = max(round(fat, 1), 1.0)
    
    return {
        "calories": cal,
        "protein_g": protein,
        "carbs_g": carbs,
        "fat_g": fat,
        "fiber_g": fiber,
        "glycemic_index": gi,
        "sodium_level": sodium,
        "cholesterol_impact": cholesterol,
        "allergens": "None" if dish['type'] == "veg" else ("Fish" if dish['meat'] == "fish" else "Egg" if dish['meat'] == "egg" else "None"),
        "instructions": instructions,
        "exercise": exercise,
        "warning": warning,
        "dish_name": dish_name,
        "base_ingredients": dish['base'],
        "diet_type": dish['type'],
        "meat_type": dish['meat']
    }

header = [
    "state", "diet_need", "meal_type", "dish", "calories", "protein_g", 
    "carbs_g", "fat_g", "fiber_g", "glycemic_index", "sodium_level", 
    "cholesterol_impact", "allergens", "base_ingredients", "diet_type", 
    "meat_type", "instructions", "exercise", "warning"
]

rows = []
seen_dishes = set()

# We need exactly 200 rows.
target = 200
idx = 0
attempts = 0

while len(rows) < target and attempts < 10000:
    diet = diet_needs[idx % len(diet_needs)]
    meal = meal_types[(idx // len(diet_needs)) % len(meal_types)]
    
    dish_template = random.choice(base_dishes[meal]).copy()
    
    data = adjust_for_diet(dish_template, meal, diet, attempts)
    attempts += 1
    
    if data is None:
        continue
        
    # Check uniqueness
    row_signature = f"{diet}_{meal}_{data['dish_name']}_{data['calories']}"
    if row_signature in seen_dishes:
        continue
        
    seen_dishes.add(row_signature)
    
    row = [
        "Chhattisgarh",
        diet,
        meal,
        data["dish_name"],
        data["calories"],
        data["protein_g"],
        data["carbs_g"],
        data["fat_g"],
        data["fiber_g"],
        data["glycemic_index"],
        data["sodium_level"],
        data["cholesterol_impact"],
        data["allergens"],
        data["base_ingredients"],
        data["diet_type"],
        data["meat_type"],
        data["instructions"],
        data["exercise"],
        data["warning"]
    ]
    rows.append(row)
    idx += 1

with open("c:\\Users\\kanag\\Desktop\\Hack project 1\\chhattisgarh_diet.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print("Created 200 rows in chhattisgarh_diet.csv")
