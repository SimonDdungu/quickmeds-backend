import os
from storages.backends.s3boto3 import S3Boto3Storage

class SupabaseImageStorage(S3Boto3Storage):
    access_key     = os.getenv("SUPABASE_S3_ACCESS_KEY")
    secret_key     = os.getenv("SUPABASE_S3_SECRET_KEY")
    bucket_name    = os.getenv("SUPABASE_S3_BUCKET")
    endpoint_url   = os.getenv("SUPABASE_S3_ENDPOINT")
    region_name    = os.getenv("SUPABASE_S3_REGION")
    default_acl    = "public-read"
    file_overwrite = False
    custom_domain = os.getenv("SUPABASE_CUSTOM_DOMAIN")