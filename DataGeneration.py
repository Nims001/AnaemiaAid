import pandas as pd
import random

# Define function to generate random data for each patient
def generate_patient_data():
    # Gender: 0 = Female, 1 = Male
    gender = random.choice([0, 1])
    
    # Family history (1 = Parents/Siblings with SCD, 0 = No family history)
    family_history = random.choice([0, 1])  # Simplified for this example
    
    # Symptoms: 0 = no symptom, 1 = present
    pain_episodes = random.randint(0, 8) if family_history == 1 else random.randint(0, 4)
    jaundice = random.choice([0, 1]) if family_history == 1 else 0
    fatigue = random.choice([0, 1]) if family_history == 1 else 0
    
    # Blood test results (simplified ranges)
    if family_history == 1:  # SCD family history, patient likely has SCD
        hemoglobin = round(random.uniform(6.5, 9.5), 1)
        reticulocyte_count = round(random.uniform(4, 10), 1)
        bilirubin = round(random.uniform(2.0, 4.0), 1)
    else:  # No family history of SCD
        hemoglobin = round(random.uniform(12.0, 15.5), 1)
        reticulocyte_count = round(random.uniform(0.5, 2.5), 1)
        bilirubin = round(random.uniform(0.3, 1.2), 1)

    # Sickle Cell Disease status (0 = No SCD, 1 = Has SCD)
    has_scd = 1 if family_history == 1 else 0

    return {
        'Gender': gender,
        'Pain_Episodes': pain_episodes,
        'Jaundice': jaundice,
        'Fatigue': fatigue,
        'Hemoglobin_Level': hemoglobin,
        'Reticulocyte_Count': reticulocyte_count,
        'Bilirubin_Level': bilirubin,
        'Family_History': family_history,
        'Has_SCD': has_scd
    }

# Generate the dataset with 100 people
data = []
# 30 people with no SCD and no family history
for _ in range(30):
    data.append(generate_patient_data())

# 70 people with family history of SCD and possibly SCD
for _ in range(70):
    data.append(generate_patient_data())

# Create DataFrame
df = pd.DataFrame(data)

# Save to a CSV file
file_path = 'sickle_cell_disease_data.csv'
df.to_csv(file_path, index=False)

file_path
