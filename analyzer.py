import ollama
import os

client = ollama.Client(host='http://host.docker.internal:11434')

def analyze_logs(file_path):
    if not os.path.exists(file_path):
        print(f"Błąd: Plik {file_path} nie istnieje.")
        return

    # Wczytanie logów
    with open(file_path, 'r', encoding='utf-8') as file:
        log_content = file.read()

    print("--- Analizowanie logów przez AI (Llama 3) ---")

    # Przygotowanie promptu
    prompt = f"""
    Jesteś doświadczonym Inżynierem DevOps. Przeanalizuj poniższe logi serwera.
    1. Znajdź wszystkie błędy (ERROR) i ostrzeżenia (WARNING).
    2. Wyjaśnij krótko, co mogło pójść nie tak.
    3. Zaproponuj konkretne kroki naprawcze (np. komendy Linux lub zmiany w konfiguracji).

    Logi do analizy:
    {log_content}
    """

    # Połączenie z lokalnym modelem
    try:
        response = client.chat(model='llama3', messages=[
            {'role': 'user', 'content': prompt},
        ])
        
        print("\n### RAPORT AI ###\n")
        print(response['message']['content'])
        
        # Zapis raportu do pliku
        with open("raport_naprawczy.txt", "w", encoding='utf-8') as f:
            f.write(response['message']['content'])
            print("\nRaport został zapisany w pliku raport_naprawczy.txt")

    except Exception as e:
        print(f"Wystąpił błąd podczas komunikacji z AI: {e}")

if __name__ == "__main__":
    analyze_logs('server.log')