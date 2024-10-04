import os
import subprocess
import sys

def freeze_conda_environment(env_name=None, output_file='environment.yml'):
    """
    Speichert die aktuelle Conda-Umgebung in einer .yml Datei.
    :param env_name: Name der Conda-Umgebung. Wenn keine angegeben, wird die aktive Umgebung verwendet.
    :param output_file: Dateiname für die gespeicherte Umgebung.
    """
    try:
        if env_name is None:
            env_name = subprocess.check_output("conda info --envs | grep '*' | awk '{print $1}'", shell=True).decode('utf-8').strip()
        
        print(f"Speichere Conda-Umgebung '{env_name}' in '{output_file}'...")
        subprocess.run(f"conda env export --name {env_name} > {output_file}", shell=True, check=True)
        print(f"Umgebung erfolgreich in '{output_file}' gespeichert.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Speichern der Conda-Umgebung: {e}")
        sys.exit(1)