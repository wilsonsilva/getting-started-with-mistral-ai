from helper import load_mistral_api_key, mistral
load_mistral_api_key()

medical_notes = """
A 60-year-old male patient, Mr. Johnson, presented with symptoms
of increased thirst, frequent urination, fatigue, and unexplained
weight loss. Upon evaluation, he was diagnosed with diabetes,
confirmed by elevated blood sugar levels. Mr. Johnson's weight
is 210 lbs. He has been prescribed Metformin to be taken twice daily
with meals. It was noted during the consultation that the patient is
a current smoker.
"""

prompt = f"""
Extract information from the following medical notes:
{medical_notes}

Return json format with the following JSON schema: 

{{
        "age": {{
            "type": "integer"
        }},
        "gender": {{
            "type": "string",
            "enum": ["male", "female", "other"]
        }},
        "diagnosis": {{
            "type": "string",
            "enum": ["migraine", "diabetes", "arthritis", "acne"]
        }},
        "weight": {{
            "type": "integer"
        }},
        "smoking": {{
            "type": "string",
            "enum": ["yes", "no"]
        }}
}}
"""

response = mistral(prompt, is_json=True)
print(response)

# {"age": 60, "gender": "male", "diagnosis": "diabetes", "weight": 210, "smoking": "yes"}
