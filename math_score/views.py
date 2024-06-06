from django.shortcuts import render, HttpResponse
import joblib

model = joblib.load('static/linear_regression')
# Create your views here.
def index(request):
    #return HttpResponse("This is the math score page")
    return render(request, 'index.html')

def about(request):
    #return HttpResponse("This is the about page")
    return render(request, 'about.html')

def contact(request):
    #return HttpResponse("This is the contact page")
    return render(request, 'contact.html')

def prediction(request):
    #return HttpResponse("This is the prediction page")
    if request.method == "POST":
       # print("enter into the post request")
        gender = int(request.POST.get('gender'))
        race_ethnicity = int(request.POST.get('race_ethnicity'))
        parental_level_of_education = int(request.POST.get('parental_level_of_education'))
        lunch = int(request.POST.get('lunch'))
        test_preparation_course = int(request.POST.get('lunch'))
        reading_score = int(request.POST.get('reading_score'))
        writing_score= int(request.POST.get('writing_score'))
        
        #print(gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score )
        
        pred = round(model.predict([[gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score]])[0])
        
       # print(pred)
        
        output = {
            "output": pred
        }
        
        return render(request,"prediction.html", output)
    else:
        return render(request, 'prediction.html')
