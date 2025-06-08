from django.apps import AppConfig


class CoreConfig(AppConfig):
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        
        from core.utils.tmp_cleaner import delete_tmp_folder
        delete_tmp_folder()

