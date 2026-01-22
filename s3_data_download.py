import os
import boto3
import pandas as pd
from botocore.exceptions import NoCredentialsError, ClientError
from dotenv import load_dotenv

# Cargar variables desde .env si existen
load_dotenv()

def download_csv_from_s3(bucket_name, s3_key, local_path=None):
    """
    Descarga un archivo CSV desde S3 y opcionalmente lo guarda en disco.
    Devuelve un DataFrame de pandas.
    
    Parámetros:
    - bucket_name: nombre del bucket S3
    - s3_key: ruta/nombre del archivo en S3
    - local_path: ruta local donde guardar el archivo (si es None, no se guarda)
    """
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )

    try:
        # Descargar a memoria
        obj = s3.get_object(Bucket=bucket_name, Key=s3_key)
        df = pd.read_csv(obj["Body"])

        # Guardar en disco si se especifica
        if local_path:
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            df.to_csv(local_path, index=False)
            print(f"✅ Archivo guardado en {local_path}")

        return df

    except NoCredentialsError:
        print("❌ No se encontraron credenciales de AWS.")
    except ClientError as e:
        print(f"❌ Error al descargar {s3_key}: {e}")
    return None


if __name__ == "__main__":
    # Bucket flexible: desde .env o argumento
    bucket = os.getenv("AWS_BUCKET_NAME", "desafio-rkd")

    # Lista flexible de archivos a descargar
    files_to_download = {
        "raw/netflix.csv": "data/raw/netflix.csv",
        "raw/disney.csv": "data/raw/disney.csv"
    }

    for s3_key, local_path in files_to_download.items():
        df = download_csv_from_s3(bucket, s3_key, local_path)
        if df is not None:
            print(f"📊 {s3_key} -> {len(df)} filas")

