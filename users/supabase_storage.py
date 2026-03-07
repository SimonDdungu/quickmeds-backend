from django.core.files.storage import Storage
from django.conf import settings
from supabase import create_client
import io

class SupabaseStorage(Storage):
    def __init__(self):
        self.client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        self.bucket = "QuickMeds"

    def _save(self, name, content):
        content.seek(0)
        data = content.read()
        self.client.storage.from_(self.bucket).upload(name, io.BytesIO(data))
        return name

    def url(self, name):
        # return f"{settings.SUPABASE_URL}/storage/v1/object/public/{self.bucket}/{name}"
        return f"https://kmmrgijtqahiilujqbck.storage.supabase.co/storage/v1/s3/{name}"

    def exists(self, name):
        return False