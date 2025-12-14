import json
from pathlib import Path
from datetime import datetime
import shutil


BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "Data"
DATA_DIR.mkdir(exist_ok=True)

DB_FILE = DATA_DIR / "database.json"

BACKUP_DIR = DATA_DIR / "Backup"
BACKUP_DIR.mkdir(exist_ok=True)

class Storage:
    def __init__(self, db_file=DB_FILE):
        self.db_file = Path(db_file)


    def load(self):
        if not self.db_file.exists():
            return {}
        
        with open(self.db_file, 'r', encoding="utf-8") as file:
            return json.load(file)
        

    def save(self, data:dict):
        temp_file = self.db_file.with_suffix(".tmp")

        with open(temp_file, 'w', encoding="utf-8") as file:
            return json.dump(data, file, indent=2)
        
        temp_file.replace(self.db_file)


    def backup(self):
        if self.db_file.exists():
            return None
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = BACKUP_DIR / f"database_{timestamp}.json"
        shutil.copy2(self.db_file, backup_file)

        return backup_file