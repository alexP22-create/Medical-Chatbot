from intent_component import classify_intent, extract_slots

intrebare = "Ce diagnostic are pacientul Ion Popescu din 03.02.2024?"

intent = classify_intent(intrebare)
slots = extract_slots(intrebare)

print("Intent:", intent)
print("Slots:", slots)