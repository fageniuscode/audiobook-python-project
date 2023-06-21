import PyPDF2
import pyttsx3

# Lecture du fichier PDF
pdfReader = PyPDF2.PdfReader('java.pdf')

# Initialisation du moteur de synthèse vocale
speaker = pyttsx3.init()

for page_num in range(len(pdfReader.pages)):
    # Extraction du texte de la page
    page = pdfReader.pages[page_num]
    text = page.extract_text()
    
    # Lecture du texte
    speaker.say(text)
    speaker.runAndWait()

# Arrêt du moteur de synthèse vocale
speaker.stop()

# Sauvegarde du texte en audio
engine = pyttsx3.init()
engine.save_to_file(text, 'audio.mp3')
engine.runAndWait()
