import time
import sys

# Comprehensive database mapping regions across India to health risks and prevention guidelines
HEALTH_DATABASE = {
    "Delhi": {
        "region": "North India",
        "risk": "Dengue Fever & Air Quality Issues",
        "prevention": [
            "Clear out standing water from coolers, pots, and tyres weekly.",
            "Always sleep under a mosquito net or use insect repellents.",
            "Wear long-sleeved clothes during high-mosquito seasons."
        ],
        "quiz_q": "Where do Dengue-carrying mosquitoes lay their eggs?",
        "quiz_options": ["A) In clean, stagnant water", "B) In flowing river water", "C) In dry soil"],
        "quiz_a": "A"
    },
    "Mumbai": {
        "region": "West India",
        "risk": "Malaria & Waterborne Infections (Monsoon Risks)",
        "prevention": [
            "Avoid walking through stagnant floodwaters to prevent leptospirosis.",
            "Ensure open household water storage containers are tightly covered.",
            "Wash hands thoroughly with soap after coming from outdoors."
        ],
        "quiz_q": "What is the best way to prevent waterborne infections during monsoons?",
        "quiz_options": ["A) Drinking water directly from tap", "B) Boiling drinking water or using filters", "C) Eating uncovered street food"],
        "quiz_a": "B"
    },
    "Hyderabad": {
        "region": "South India",
        "risk": "Typhoid & Gastrointestinal Infections",
        "prevention": [
            "Drink only boiled, filtered, or safe bottled water.",
            "Always wash hands with soap for 20 seconds before eating food.",
            "Avoid eating raw or uncovered food items from street vendors."
        ],
        "quiz_q": "How long should you scrub your hands with soap to kill most germs?",
        "quiz_options": ["A) 2 seconds", "B) 5 seconds", "C) 20 seconds"],
        "quiz_a": "C"
    },
    "Kolkata": {
        "region": "East India",
        "risk": "Cholera & Vector-borne Diseases",
        "prevention": [
            "Ensure all food is freshly cooked and consumed while hot.",
            "Keep community surroundings clean and report choked drains.",
            "Use chlorinated or properly treated water for cooking and cleaning."
        ],
        "quiz_q": "Which insect spreads diseases like Dengue and Malaria?",
        "quiz_options": ["A) Houseflies", "B) Mosquitoes", "C) Ants"],
        "quiz_a": "B"
    }
}

DEFAULT_GUIDELINES = {
    "region": "General India",
    "risk": "Seasonal Flu, Diarrhoea & Cold Infections",
    "prevention": [
        "Maintain clean toilet hygiene and always flush after use.",
        "Wash your hands before eating and after using the restroom.",
        "Cover your mouth with your elbow when coughing or sneezing."
    ],
    "quiz_q": "When is it most critical to wash your hands with soap?",
    "quiz_options": ["A) Before eating and after using the toilet", "B) Only when your hands look visibly dirty", "C) Right before going to sleep"],
    "quiz_a": "A"
}

def slow_print(text, delay=0.02):
    """Prints text slowly to make it look like a dynamic, engaging school application terminal."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def run_project_sanitaire():
    slow_print("\n=======================================================")
    slow_print("      WELCOME TO PROJECT SANITAIRÈ DIGITAL PORTAL    ")
    slow_print("      Building Health Literacy, One Classroom at a Time  ")
    slow_print("=======================================================")
    
    # User Input Collection
    student_name = input("\nEnter Student Name: ").strip().title()
    location = input("Enter your Current City/District in India: ").strip().title()
    
    slow_print(f"\nHello {student_name}! Fetching local health data for {location}...")
    time.sleep(1)
    
    # Database matching logic
    data = HEALTH_DATABASE.get(location, DEFAULT_GUIDELINES)
    
    # Display Health Information Segment
    print("\n-------------------------------------------------------")
    print(f"📍 REGION DETECTED         : {data['region']} ({location})")
    print(f"⚠️ HIGH LOCAL HEALTH RISK  : {data['risk']}")
    print("-------------------------------------------------------")
    
    slow_print("\n YOUR ACTIONABLE HEALTH PREVENTION STEPS:")
    for idx, step in enumerate(data['prevention'], 1):
        slow_print(f"  {idx}. {step}")
        time.sleep(0.5)
        
    # Interactive 5-Minute Engagement Quiz Segment
    print("\n-------------------------------------------------------")
    slow_print("QUICK DAILY HEALTH QUIZ FOR STUDENTS")
    print("-------------------------------------------------------")
    slow_print(f"Question: {data['quiz_q']}")
    for option in data['quiz_options']:
        print(f"  {option}")
        
    answer = input("\nType your answer (A, B, or C): ").strip().upper()
    
    if answer == data['quiz_a']:
        print("\n🎉 CORRECT! Excellent job! You are keeping yourself and your school safe.")
    else:
        print(f"\n❌ Not quite! The correct answer was {data['quiz_a']}.")
        slow_print("Remember this rule to build healthy habits every day!")
        
    print("\n=======================================================")
    print("✨ Thank you for completing your daily session! See you tomorrow! ✨")
    print("=======================================================\n")

if __name__ == "__main__":
    run_project_sanitaire()
