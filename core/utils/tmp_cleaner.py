import os
import shutil
import threading
from datetime import datetime, timedelta
from django.conf import settings

TMP_DIR = os.path.join(settings.BASE_DIR, 'tmp')
NEXT_RUN = None

def delete_tmp_folder():
    
    global NEXT_RUN

    now = datetime.now()
    
    if NEXT_RUN is None or now >= NEXT_RUN:
        
        if os.path.exists(TMP_DIR):
            
            shutil.rmtree(TMP_DIR)
            os.makedirs(TMP_DIR)
            
            print(f"[{now}] ✅ Cleaned tmp/")
            
        else:
            
            print(f"[{now}] ⚠️ tmp/ does not exist")


        NEXT_RUN = now + timedelta(days=1)


    threading.Timer(3600, delete_tmp_folder).start()
