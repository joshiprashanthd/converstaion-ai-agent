import sys

sys.path.append("../..")
from groq_model import Llama3_1_70B_Versatile
from prompts.extract_parameter.ExtractL1Parameter import ExtractL1Parameter, QNA
from typing import List, Dict
from prompts.extract_parameter.ExtractL3Parameter import ExtractL3Parameter
from pprint import pprint


model = Llama3_1_70B_Versatile()
prompt1 = ExtractL1Parameter(model)
prompt2 = ExtractL3Parameter(model)
answers: List[QNA] = [
    {
        "question": "How was your day?",
        "answer": "Pretty productive! I managed to finish all my tasks and even had some time to work out."
        },
        {
        "question": "How was your sleep last night? Did you wake up feeling refreshed or still tired? What do you think affected it?",
        "answer": "I didn’t sleep well last night. I woke up a couple of times and felt pretty tired in the morning. I think it was because I spent too much time on my phone right before bed, and my mind was still racing."
        },
        {
        "question": "How were your energy levels today? Did you feel a dip at any particular time? What do you think caused it?",
        "answer": "My energy levels were okay in the morning, but I definitely felt a dip around 3 PM. I think it was because I skipped my usual afternoon snack, so my blood sugar might have dropped a bit. Next time, I’ll try to keep a snack handy."
        }

    ]

L1_parameters: List[str] = ['routine', 'sleep', 'diet', 'work', 'personality and inclinations', 'mental state']

L3_parameters: Dict[str, List[str]] = {
    'routine': ['bedtime', 'wakeup time', 'duration', 'consistency', 'duration', 'no. of breaks', 'timings', 'busy-ness', 'intensity', 'stress', 'breaks duration', 'type/details', 'frequency', 'duration', 'intensity', 'consistency', 'timings', 'meal timings', 'meal frequencies', 'hydration level', 'meal quantity', 'breakfast time', 'lunch time', 'dinner time', 'snacks time', 'practices/details', 'duration', 'timings', 'time spent', 'interests', 'activities involved in', 'frequency', 'eating environment', 'bathing', 'teeth brusing', 'env cleanliness', 'clothes washing', 'medications', 'alcohol', 'caffeine', 'drugs', 'smoking', 'tobaco', 'sedentary time', 'commute time', 'commute mode', 'commute ease', 'commute tireness', 'type', 'duration', 'purpose', 'timings'],

    'sleep':['total hours', 'Number of naps and duration', 'Sleep cycle', 'Time required for falling asleep', 'bed time', 'naps in day', 'nap down time', 'nap up time', 'consistency', 'no. of times awakened at night', 'ease of falling asleep', 'restfullness', 'efficiency', 'overall quality', 'snoring', 'waking up feeling', 'waking up ease', 'latency', 'Heart rythm/ palpitations', 'Breathing and snuffling', 'location', 'temperature of surroundings', 'noise levels', 'lights', 'Thermals', 'pre sleep screen time', 'suppliments', 'reading', 'physical activity', 'relaxation techniques', 'food intake', 'presleep hygiene', 'work related activity', 'music', 'podcasts', 'writing', 'Meditation', 'Hypnosis', 'caffeine intake', 'last meal', 'alcohol consumption', 'last meal time', 'After sleep refreshment', 'Apnea', 'Asthma/bronchitis', 'Melatonin', 'Narcolepsy', 'Hypersomnolence', 'Insomnia', 'Movement disorders', 'vividness and recall ability', 'duration', 'tone/type/theme', 'no. of dreams', 'effect on sleep and post sleep', 'Lucid dreaming', 'Somnambulism', 'Triggers', 'thoughts', 'stress', 'anxiety/worry', 'mood', 'fatigue', 'Pace', 'Effect of sleep on emotions.'],

    'diet': ['food quality', 'Food freshness', 'Organic percentage', 'breakfast time', 'lunch time', 'dinner time', 'snacks time', 'breakfast frequency', 'lunch frequency', 'dinner frequency', 'snacks frequency', 'daily water intake quantity', 'daily other liquid intake quantity', 'intervals in between water intake', 'fruit juices quantity', 'fruit juices type', 'soft drink quantity', 'soft drink types', 'hydration satisfaction', 'Mastication', 'Time taken per morsel', 'breakfast quantity', 'lunch quantity', 'snacks quantity', 'dinner quantity', 'talking while eating', 'tv/phone/gadgets while eating', 'working while eating', 'morning water intake', 'water intake before sleep', 'water intake after meals', 'Proteins', 'Carbohydrates', 'Vitamins', 'Electrolytes', 'Fats', 'Fibres', 'minerals', 'quality of ingedrients', 'hygiene of the cook', 'Hygiene of place', 'alcohol', 'caffeine', 'substances', 'smoking', 'tobacco', 'tea', 'allergies/disease/ailments history', 'family allergies/disease/ailments history', 'digestive issues', 'appetite', 'health suppliments'],


    'work': ['job nature', 'industry', 'job role', 'salary', 'emplyment type', 'on-site/remote', 'office location', 'work satisfaction', 'motivation', 'work-life balance', 'professional aspirations', 'milestones', 'job security', 'burnouts', 'relationships with colleagues', 'work hours', 'breaks', 'night shifts', 'commute time', 'overtime', 'flexible hours', 'sick leaves', 'vacation days', 'cleanliness', 'lighting', 'Noise Levels', 'commute mode', 'Workspace Ergonomics', 'Amenities', 'screen time', 'recognition and rewards', 'activities', 'outings', 'diversity and inclusion', 'stress', 'peer support'],

    'personality and inclinations': ['determination', 'tolerance', 'purpose of life', 'purpose of work', 'work attachment through purpose', 'work attachment through results', 'dutifulness/sincereness', 'irritation', 'risk ability/adventure/courage', 'biasness/cheating tendency', 'respect by others', 'expectation of respect', 'charitible', 'consoling', 'divinity perception', 'sense control', 'truthfulness', 'austerity', 'punctuality', 'cleanliness', 'favourite food', 'favorite juice', 'favorite season', 'favorite colour', 'carvings', 'knowledge depth', 'wellfare activities', 'skill level', 'knowledge gaining proclivity', 'sports playing', 'passion or hobby', 'arts and culture', 'interests', 'money making', 'administration', 'simply working', 'optimism', 'ideal people/inspirations', 'Spiritual inclinations', 'Morals', 'Religion', 'enthusiam', 'endeavour/hard working nature', 'energetic in work', 'visionary', 'Ambitious', 'purpose motivations', 'monetory motivations', 'social good motivation', 'administrative motivation', 'fearfulness', 'grief on faliures/loss', 'desire for gain (lobha)', 'anger for small things (krodha)', 'controlled anger', 'enjoying tendency (kaam)', 'bewilderment in challenging situations (moha)', 'self pride (mada)', 'pride on achievements (mada)', 'jelosy tendency (matsarya)', 'memory', 'innovative', 'decision making', 'imaginative', 'discrimination ability', 'methodological approach', 'advising', 'focus', 'Family', 'Friends', 'Parasocial and online', 'relations at work', 'Community', 'Teachers/Superiors', 'Pets', 'Sexuality', 'Relationship conflicts', 'self esteem', 'Substance abuse', 'Orientation', 'Suicidal or homicidal thoughts rating', 'Tremors', 'Assault history', 'Family psychiatric history', 'height', 'weight', 'complexion', 'gait', 'voice', 'hair colour', 'iris colour', 'activities', 'personal groom', 'voice', 'strength', 'restful/restless', 'speech', 'movement', 'built', 'sleep', 'dreams', 'appetite', 'immunity', 'thirst', 'fatigue'],

    'mental state': ['calmness', 'thoughts', 'mood variability', 'emotional awareness', 'emotional expression', 'emotional connections', 'stability', 'emotional intelligence', 'support', 'emotional health', 'Apathy', 'Elevation', 'sadness', 'irritability', 'Resilience', 'anxiety', 'mood swings', 'psychotic', 'personality disorder', 'eating disorder', 'addiction', 'trauma', 'stress', 'depression', 'sleepdisorder', 'Neurodevelopmental', 'substance-related', 'Genetic', 'Obsessions and compulsions', 'mental equilibrium', 'psychological well being', 'social well being', 'habits', 'coping mechanism', 'stress management', 'awareness', 'support', 'cognitive functioning', 'personal experiences', 'personal history', 'medical history', 'family history', 'life transitions', 'awareness', 'calmness', 'fatigue']

}

response = prompt1(answers, L1_parameters)

print("Response from ExtractL1Parameter:")
pprint(response)
print()

for key, value in response.items():
    try:
        print(f"Processing key: {key}")
        pprint(prompt2(value, L3_parameters[key]))
    except Exception as e:
        print(f"Error processing key {key}: {e}")
