def explain_results(data: dict):
    # Medical interpretations for a wide range of lab results
    interpretations = {
        "Hemoglobin": lambda val: "Low hemoglobin may indicate anemia, dehydration, or nutritional deficiencies." if float(val) < 13 else "Normal hemoglobin level. A measure of your red blood cell count.",
        "TSH": lambda val: "High TSH could suggest hypothyroidism, a condition where your thyroid is underactive." if float(val) > 4.5 else "Normal TSH range. Indicates normal thyroid function.",
        "WBC": lambda val: "Elevated WBC may indicate an infection, inflammation, or immune system disorder." if float(val) > 11 else "WBC is within normal limits. A marker of your immune system function.",
        "Platelets": lambda val: "Low platelet count could suggest a bleeding disorder or bone marrow issue." if float(val) < 150 else "Normal platelet count, ensuring proper blood clotting.",
        "RBC": lambda val: "Low RBC count could indicate anemia, malnutrition, or bone marrow problems." if float(val) < 4.7 else "Normal RBC count, supporting healthy oxygen transport in your blood.",
        "Cholesterol": lambda val: "High cholesterol could increase the risk of heart disease and stroke." if float(val) > 200 else "Cholesterol level is within the normal range, supporting cardiovascular health.",
        "Glucose": lambda val: "High glucose levels could indicate diabetes or a risk of developing it." if float(val) > 100 else "Normal glucose level, indicating proper blood sugar control.",
        "Creatinine": lambda val: "High creatinine levels could suggest kidney dysfunction or dehydration." if float(val) > 1.2 else "Normal creatinine levels, indicating good kidney health.",
        "Bilirubin": lambda val: "High bilirubin levels may indicate liver disease or a bile duct obstruction." if float(val) > 1.2 else "Normal bilirubin levels, indicating healthy liver function.",
        "LDL": lambda val: "High LDL (bad cholesterol) levels could increase the risk of heart disease." if float(val) > 100 else "LDL levels are within the normal range, promoting heart health.",
        "HDL": lambda val: "Low HDL (good cholesterol) levels may increase heart disease risk." if float(val) < 40 else "Normal HDL levels, supporting a lower risk of heart disease."
    }

    explanation = {}

    # Interpret each test result
    for key, val in data.items():
        explanation[key] = interpretations.get(key, lambda x: "No information available for this test.")(val)
    
    return explanation
