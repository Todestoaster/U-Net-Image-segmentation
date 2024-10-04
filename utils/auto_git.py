import os
import subprocess
import sys

def git_push_master():
    """
    Führt einen git push -u origin master Befehl aus, um das Repository mit den neuesten Änderungen zu aktualisieren.
    """
    try:
        print("Aktualisiere Repository mit 'git push'...")
        subprocess.run("git push -u origin master", shell=True, check=True)
        print("Repository erfolgreich hochgeladen.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Git Pull: {e}")
        sys.exit(1)


def git_pull():
    """
    Führt einen git pull Befehl aus, um das Repository mit den neuesten Änderungen zu aktualisieren.
    """
    try:
        print("Aktualisiere Repository mit 'git pull'...")
        subprocess.run("git pull origin master", shell=True, check=True)
        print("Repository erfolgreich aktualisiert.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Git Pull: {e}")
        sys.exit(1)
        

def install_requirements(requirements_file='requirements.txt'):
    """
    Installiert Abhängigkeiten aus einer requirements.txt Datei mit pip.
    :param requirements_file: Der Pfad zur requirements.txt Datei.
    """
    if os.path.exists(requirements_file):
        try:
            print(f"Installiere Abhängigkeiten aus '{requirements_file}'...")
            subprocess.run(f"pip install -r {requirements_file}", shell=True, check=True)
            print("Abhängigkeiten erfolgreich installiert.")
        except subprocess.CalledProcessError as e:
            print(f"Fehler bei der Installation der Abhängigkeiten: {e}")
            sys.exit(1)
    else:
        print(f"Die Datei '{requirements_file}' wurde nicht gefunden.")


def git_status():
    """
    Zeigt den aktuellen Git-Status des Repositories an.
    """
    try:
        print("Zeige aktuellen Git-Status...")
        subprocess.run("git status", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Anzeigen des Git-Status: {e}")
        sys.exit(1)


def backup_project(backup_dir='backups'):
    """
    Erstellt ein Backup des aktuellen Projekts in einem angegebenen Backup-Verzeichnis.
    :param backup_dir: Verzeichnis, in dem das Backup gespeichert werden soll.
    """
    try:
        os.makedirs(backup_dir, exist_ok=True)
        subprocess.run(f"cp -r . {backup_dir}", shell=True, check=True)
        print(f"Projekt erfolgreich in '{backup_dir}' gesichert.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Erstellen des Backups: {e}")
        sys.exit(1)


def show_help():
    """
    Zeigt die verfügbaren Funktionen dieses Skripts an.
    """
    print("""
Verfügbare Funktionen:
- git_pull(): Führt einen Git-Pull aus.
- git_push_master(): Führt einen Git-Push auf master branch aus.
- install_requirements(requirements_file='requirements.txt'): Installiert Abhängigkeiten aus requirements.txt.
- git_status(): Zeigt den Git-Status an.
- backup_project(backup_dir='backups'): Erstellt ein Backup des aktuellen Projekts.
    """)

if __name__ == "__main__":
    show_help()