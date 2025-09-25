from django.http import JsonResponse
from django.shortcuts import render
from predictor.ML_Files.std_stress_predict import predict_std_stress_level, get_model_performance
from . forms import StudentStressLevelForm
def homepage(request):
    new_data = {}
    prediction = None
    probability = None
    
    if request.method == "POST":
        form = StudentStressLevelForm(request.POST)
        if form.is_valid():
            # Convert form data to dictionary matching your sample data structure
            new_data = {
                "anxiety_level": int(form.cleaned_data['anxiety_level']),
                "self_esteem": int(form.cleaned_data['self_esteem']),
                "mental_health_history": int(form.cleaned_data['mental_health_history']),
                "depression": int(form.cleaned_data['depression']),
                "headache": int(form.cleaned_data['headache']),
                "blood_pressure": int(form.cleaned_data['blood_pressure']),
                "sleep_quality": int(form.cleaned_data['sleep_quality']),
                "breathing_problem": int(form.cleaned_data['breathing_problem']),
                "noise_level": int(form.cleaned_data['noise_level']),
                "living_conditions": int(form.cleaned_data['living_conditions']),
                "safety": int(form.cleaned_data['safety']),
                "basic_needs": int(form.cleaned_data['basic_needs']),
                "academic_performance": int(form.cleaned_data['academic_performance']),
                "study_load": int(form.cleaned_data['study_load']),
                "teacher_student_relationship": int(form.cleaned_data['teacher_student_relationship']),
                "future_career_concerns": int(form.cleaned_data['future_career_concerns']),
                "social_support": int(form.cleaned_data['social_support']),
                "peer_pressure": int(form.cleaned_data['peer_pressure']),
                "extracurricular_activities": int(form.cleaned_data['extracurricular_activities']),
                "bullying": int(form.cleaned_data['bullying'])
            }
            
            # Print the data in console (same format as your sample)
            # print("New data received from form:")
            # print(new_data)
            
            # Call your prediction function
            pred_class, class_prob = predict_std_stress_level(new_data)
            prediction = pred_class
            probability = class_prob
            # DEBUG: Print raw prediction info
            print(f"Raw prediction class: {pred_class}")
            print(f"Raw prediction probability: {class_prob}")
            print(f"Type of pred_class: {type(pred_class)}")
            print("Prediction:", prediction, "Probability:", probability)
  
            # Return both prediction class and probability
            return JsonResponse({
            "prediction": int(pred_class),
            "probability": float(class_prob)
        })
       
            
        else:
            print("Form is not valid")
            print(form.errors)
            return JsonResponse({"error": "Form is not valid", "errors": form.errors}, status=400)

    else:
        form = StudentStressLevelForm()
    # print("Inside view function")
    # print(probability)
    # print(prediction)
    various_metrics = get_model_performance()
    # Convert to percentage + round
    formatted_metrics = {
        key: f"{round(value * 100, 2)}" for key, value in various_metrics.items()
    }

    context = {
        "metrics": formatted_metrics,
        "prediction": prediction,
        "probability": probability,
        "form": form,
    }
    return render(request, 'predictor/homepage.html', context)