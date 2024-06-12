from django.shortcuts import render, HttpResponse
import joblib
import numpy as np
import pandas as pd

# Load model and preprocessor
model = joblib.load('static/linear_regression')
preprocessor = joblib.load('static/preprocessor')  # Assuming you saved the preprocessor

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def prediction(request):
    if request.method == "POST":
        try:
            gender = request.POST.get('gender')
            race_ethnicity = request.POST.get('race_ethnicity')
            parental_level_of_education = request.POST.get('parental_level_of_education')
            lunch = request.POST.get('lunch')
            test_preparation_course = request.POST.get('test_preparation_course')
            reading_score = float(request.POST.get('reading_score'))
            writing_score = float(request.POST.get('writing_score'))

            # Create a DataFrame for the new input
            input_data = pd.DataFrame({
                'gender': [gender],
                'race_ethnicity': [race_ethnicity],
                'parental_level_of_education': [parental_level_of_education],
                'lunch': [lunch],
                'test_preparation_course': [test_preparation_course],
                'reading_score': [reading_score],
                'writing_score': [writing_score]
            })

            # Apply the preprocessor to the new input data
            input_data_processed = preprocessor.transform(input_data)

            # Predict using the preprocessed data
            pred = round(model.predict(input_data_processed)[0])

            output = {"output": pred}
            return render(request, "prediction.html", output)
        except Exception as e:
            return HttpResponse(f"Error in processing request: {str(e)}")
    else:
        return render(request, 'prediction.html')
