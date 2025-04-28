import firebase_admin
from firebase_admin import credentials, firestore

KEY_PATH = ""
cred = credentials.Certificate(KEY_PATH)
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_patient_document(patient_name):
    patients_ref = db.collection('pacienti')
    query = patients_ref.where('nume_complet', '==', patient_name).limit(1).stream()

    for doc in query:
        return doc.to_dict()

    return None

def get_diagnosis(patient_name, date=None):
    patient = get_patient_document(patient_name)
    if not patient:
        return f"Pacientul {patient_name} nu a fost găsit."

    diagnoses = patient.get('diagnostice', [])

    if date:
        for diag in diagnoses:
            if diag.get('data') == date:
                return f"Diagnosticul din {date} pentru {patient_name} este: {diag.get('diagnostic')}"
        return f"Nu am găsit diagnostic pentru {patient_name} pe {date}."
    else:
        if diagnoses:
            latest = sorted(diagnoses, key=lambda x: x['data'], reverse=True)[0]
            return f"Ultimul diagnostic pentru {patient_name} este: {latest.get('diagnostic')}"
        else:
            return f"Nu există diagnostice înregistrate pentru {patient_name}."
