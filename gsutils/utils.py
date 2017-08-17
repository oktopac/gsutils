from google.cloud import storage
import os

def gs_download_if_required(bucket, path, output):
    gsclient = storage.Client()

    if os.path.exists(output):
        return
    bucket = gsclient.get_bucket(bucket)
    blob = bucket.blob(path)
    blob.download_to_filename(output)
