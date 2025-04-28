from intent_component import classify_intent, extract_slots
from firebase_connector import get_diagnosis, get_hospitalizations

def handle_user_request(text):
    intent = classify_intent(text)
    slots = extract_slots(text)

    patient_name = slots.get('nume_pacient')
    date = slots.get('data')

    if intent == 'get_diagnosis':
        return get_diagnosis(patient_name, date)
    elif intent == 'get_hospitalizations':
        return get_hospitalizations(patient_name, date)
    else:
        return "Încă nu pot răspunde la acest tip de întrebare."

def main():
    print("Chatbot medical - scrie 'q' sau 'Q' pentru a ieși.")
    while True:
        user_input = input("\nTu: ").strip()
        
        if user_input.lower() == 'q':
            print("Închidem chatbot-ul. La revedere!")
            break

        if not user_input:
            continue  # dacă utilizatorul apasă doar Enter, nu procesăm nimic

        response = handle_user_request(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
