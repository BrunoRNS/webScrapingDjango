from datetime import datetime, timedelta
from django.conf import settings
from pathlib import Path
import threading
import shutil

TMP_DIR = Path(settings.BASE_DIR) / 'tmp'
AGE_LIMIT_DAYS = 3

def delete_old_tmp_folders():
    """
    Deletes any tmp folders older than AGE_LIMIT_DAYS days -> 3.

    This function is intended to be run as a background thread. If the tmp folder
    does not exist, it just returns without doing anything.

    :return: None
    """
    
    if not TMP_DIR.exists():
        
        # We just ignore it in those cases..
        return

    cutoff_time = datetime.now() - timedelta(days=AGE_LIMIT_DAYS)

    for folder in TMP_DIR.iterdir():
        
        if folder.is_dir():
            
            folder_mtime = datetime.fromtimestamp(folder.stat().st_mtime)
            
            if folder_mtime < cutoff_time:
                
                try:
                    
                    shutil.rmtree(folder)
                    print(f"[CLEANER] 🧹 Deleted: {folder.name} (modified: {folder_mtime})")
                    
                except Exception as e:
                    
                    print(f"[CLEANER] ⚠️ Failed to delete {folder.name}: {e}")


def run_tmp_cleaner_async():
    """
    Runs delete_old_tmp_folders as a background thread.
    
    This function does not wait for the thread to finish. It just starts the
    thread and returns immediately.
    
    :return: None
    """
    
    thread = threading.Thread(target=delete_old_tmp_folders, daemon=True)
    thread.start()
