=================================================  Clasificarea intrebarilor ==================================================

🧠 1. Întrebări complete (executabile direct)
Conțin suficiente informații pentru a interoga direct baza de date.

„Care este diagnosticul pacientului Ion Popescu din 03.02.2024?”

„Ce diagnostic are pacientul ID12345 pentru consultația din 12 aprilie 2023?”

„Ce diagnostic a primit Maria Ionescu în ultima consultație?”

„Ce internări a avut pacientul ID98765 în ultimii 3 ani?”

„Ce boli cronice are pacientul Andrei Pavel?”

„Care este istoricul de tratamente pentru pacientul Ion Popescu?”

🤔 2. Întrebări incomplete (necesită context sau clarificări)
Chatbotul le poate interpreta doar dacă există un context anterior sau va cere detalii.

🔹 Fără specificarea pacientului:
„Ce diagnostic are?”
→ dacă anterior s-a vorbit despre un pacient, va folosi acel context.

„Ce simptome a avut înainte de internare?”
→ chatbotul trebuie să știe despre care internare/pacient e vorba.

🔹 Fără specificarea intervalului:
„Ce tratamente a urmat?”
→ când? pentru ce episod? trebuie clarificat.

„Există istoric de diabet?”
→ pentru cine? în ce perioadă?

🧾 3. Exemple de întrebări combinate sau complexe
Chatbotul ar trebui să fie capabil să le gestioneze pe baza contextului acumulat.

„Pacientul Ion Popescu, născut în 1962, are istoric de hipertensiune?”

„Vreau datele de laborator relevante pentru episodul de pe 12 ianuarie”

„Este același diagnostic ca cel din iunie anul trecut?”

🧹 4. Comenzi conversaționale speciale (context manager)
„Am un alt pacient acum”
→ setează un nou pacient în context

„Șterge contextul actual” / „Începe o consultație nouă”
→ golește contextul conversațional

„Ține minte că pacientul e alergic la penicilină”
→ adaugă o informație contextuală care poate fi utilizată ulterior

„Ce știi până acum despre pacientul actual?”
→ rezumă informațiile stocate în sesiune


==================================================== Intentii si informatii =========================================================

🔹 INTENTS (acțiuni posibile)
Intent	Descriere
get_diagnosis	Cere un diagnostic pentru un pacient
get_history	Cere istoricul medical general
get_hospitalizations	Cere detalii despre internări
get_treatments	Ce tratamente a primit pacientul
get_lab_results	Ce analize are pacientul
summarize_patient	Cere un rezumat al datelor disponibile
set_patient_context	Setați pacientul activ
clear_context	Șterge pacientul/consultația curentă
unknown	Dacă întrebarea nu e înțeleasă

🔹 SLOTS (date extrase din întrebare)
Slot	Exemplu	Tip
nume_pacient	„Ion Popescu”	string
id_pacient	„ID12345”	string
data	„03.02.2024”	date
boala	„hipertensiune”, „COVID-19”	string
tip_date	„diagnostic”, „internări”, „tratamente”	enum
interval	„ultimii 2 ani”, „din 2023”	date range
simptome	„tuse, febră”	list


====================================================== SETUP =================================================================
0. install Rust
1. install requirments/txt
2. pip install transformers torch
3. Instalează Microsoft Visual C++ Redistributable 2015–2022
Descarcă și instalează de aici: 👉 https://aka.ms/vs/16/release/vc_redist.x64.exe
pip install transformers datasets torch scikit-learn pandas
4. pip install firebase-admin

