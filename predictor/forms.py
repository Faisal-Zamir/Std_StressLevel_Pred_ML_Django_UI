from django import forms

class StudentStressLevelForm(forms.Form):
    # Mental Health Tab
    ANXIETY_CHOICES = [(i, str(i)) for i in range(1, 21)]  # 1-20
    ESTEEM_CHOICES = [(i, str(i)) for i in range(1, 11)]   # 1-10
    DEPRESSION_CHOICES = [(i, str(i)) for i in range(1, 11)]  # 1-10
    MENTAL_HISTORY_CHOICES = [
        (0, 'No history'),
        (1, 'History present')
    ]
    
    # Physical Health Tab
    HEADACHE_CHOICES = [
        (0, 'Never'),
        (1, 'Rarely'),
        (2, 'Sometimes'),
        (3, 'Often'),
        (4, 'Always')
    ]
    
    BLOOD_PRESSURE_CHOICES = [
        (0, 'Normal'),
        (1, 'Elevated'),
        (2, 'High')
    ]
    
    SLEEP_QUALITY_CHOICES = [(i, str(i)) for i in range(1, 11)]  # 1-10
    
    BREATHING_CHOICES = [
        (0, 'None'),
        (1, 'Mild'),
        (2, 'Moderate'),
        (3, 'Severe')
    ]
    
    # Environment Tab
    NOISE_LEVEL_CHOICES = [
        (1, 'Quiet'),
        (5, 'Moderate'),
        (10, 'Noisy'),
        (20, 'Very Noisy')
    ]
    
    LIVING_CONDITIONS_CHOICES = [
        (4, 'Excellent'),
        (3, 'Good'),
        (2, 'Fair'),
        (1, 'Poor')
    ]
    
    SAFETY_CHOICES = [
        (4, 'Very Safe'),
        (3, 'Safe'),
        (2, 'Neutral'),
        (1, 'Unsafe'),
        (0, 'Very Unsafe')
    ]
    
    BASIC_NEEDS_CHOICES = [
        (4, 'Fully Met'),
        (3, 'Mostly Met'),
        (2, 'Partially Met'),
        (1, 'Rarely Met')
    ]
    
    BULLYING_CHOICES = [
        (0, 'Never'),
        (1, 'Rarely'),
        (2, 'Sometimes'),
        (3, 'Often')
    ]
    
    # Academic Tab
    ACADEMIC_PERFORMANCE_CHOICES = [
        (5, 'Excellent'),
        (4, 'Good'),
        (3, 'Average'),
        (2, 'Below Average'),
        (1, 'Poor')
    ]
    
    STUDY_LOAD_CHOICES = [(i, str(i)) for i in range(1, 11)]  # 1-10
    
    TEACHER_RELATIONSHIP_CHOICES = [
        (4, 'Excellent'),
        (3, 'Good'),
        (2, 'Neutral'),
        (1, 'Poor'),
        (0, 'Very Poor')
    ]
    
    FUTURE_CAREER_CHOICES = [
        (1, 'None'),
        (3, 'Mild'),
        (6, 'Moderate'),
        (9, 'Severe')
    ]
    
    SOCIAL_SUPPORT_CHOICES = [
        (4, 'Excellent'),
        (3, 'Good'),
        (2, 'Moderate'),
        (1, 'Poor'),
        (0, 'None')
    ]
    
    PEER_PRESSURE_CHOICES = [
        (1, 'None'),
        (3, 'Mild'),
        (6, 'Moderate'),
        (9, 'High')
    ]
    
    EXTRACURRICULAR_CHOICES = [
        (0, 'None'),
        (1, '1-2 activities'),
        (2, '3-4 activities'),
        (3, '5+ activities')
    ]
    
    # Mental Health Fields
    anxiety_level = forms.ChoiceField(choices=ANXIETY_CHOICES, label="Anxiety Level (1-20)")
    self_esteem = forms.ChoiceField(choices=ESTEEM_CHOICES, label="Self Esteem (1-10)")
    mental_health_history = forms.ChoiceField(choices=MENTAL_HISTORY_CHOICES, label="Mental Health History")
    depression = forms.ChoiceField(choices=DEPRESSION_CHOICES, label="Depression Level (1-10)")
    
    # Physical Health Fields
    headache = forms.ChoiceField(choices=HEADACHE_CHOICES, label="Headache Frequency")
    blood_pressure = forms.ChoiceField(choices=BLOOD_PRESSURE_CHOICES, label="Blood Pressure")
    sleep_quality = forms.ChoiceField(choices=SLEEP_QUALITY_CHOICES, label="Sleep Quality (1-10)")
    breathing_problem = forms.ChoiceField(choices=BREATHING_CHOICES, label="Breathing Problems")
    
    # Environment Fields
    noise_level = forms.ChoiceField(choices=NOISE_LEVEL_CHOICES, label="Noise Level in Environment")
    living_conditions = forms.ChoiceField(choices=LIVING_CONDITIONS_CHOICES, label="Living Conditions")
    safety = forms.ChoiceField(choices=SAFETY_CHOICES, label="Feeling of Safety")
    basic_needs = forms.ChoiceField(choices=BASIC_NEEDS_CHOICES, label="Basic Needs Met")
    bullying = forms.ChoiceField(choices=BULLYING_CHOICES, label="Bullying Experience")
    
    # Academic Fields
    academic_performance = forms.ChoiceField(choices=ACADEMIC_PERFORMANCE_CHOICES, label="Academic Performance")
    study_load = forms.ChoiceField(choices=STUDY_LOAD_CHOICES, label="Study Load (1-10)")
    teacher_student_relationship = forms.ChoiceField(choices=TEACHER_RELATIONSHIP_CHOICES, label="Teacher-Student Relationship")
    future_career_concerns = forms.ChoiceField(choices=FUTURE_CAREER_CHOICES, label="Future Career Concerns")
    social_support = forms.ChoiceField(choices=SOCIAL_SUPPORT_CHOICES, label="Social Support")
    peer_pressure = forms.ChoiceField(choices=PEER_PRESSURE_CHOICES, label="Peer Pressure")
    extracurricular_activities = forms.ChoiceField(choices=EXTRACURRICULAR_CHOICES, label="Extracurricular Activities")