import os
import boto3
import pandas as pd
from botocore.exceptions import NoCredentialsError, ClientError
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

# Print de las variables para verificar
print("AWS_ACCESS_KEY_ID:", os.getenv("AWS_ACCESS_KEY_ID"))
print("AWS_SECRET_ACCESS_KEY:", os.getenv("AWS_SECRET_ACCESS_KEY"))
print("AWS_BUCKET_NAME:", os.getenv("AWS_BUCKET_NAME"))


def download_csv_from_s3(bucket_name, s3_key, local_path=None):
    """
    Descarga un archivo CSV desde S3 usando credenciales.
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
        # Descargar archivo a ruta temporal
        temp_path = local_path or "temp.csv"
        os.makedirs(os.path.dirname(temp_path), exist_ok=True)
        s3.download_file(bucket_name, s3_key, temp_path)

        # Leer CSV con pandas
        df = pd.read_csv(temp_path)

        # Guardar en disco si se especifica
        if local_path:
            df.to_csv(local_path, index=False)
            print(f"✅ Archivo guardado en {local_path}")

        return df

    except NoCredentialsError:
        print("❌ No se encontraron credenciales de AWS.")
    except ClientError as e:
        print(f"❌ Error al descargar {s3_key}: {e}")
    return None


if __name__ == "__main__":
    # Bucket y claves desde .env
    bucket = os.getenv("AWS_BUCKET_NAME", "desafio-rkd")

    # Archivos a descargar (usando claves)
    files_to_download = {
        "netflix_titles.csv": "data/raw/netflix.csv",
        "disney_plus_titles.csv": "data/raw/disney.csv"
    }

    for s3_key, local_path in files_to_download.items():
        df = download_csv_from_s3(bucket, s3_key, local_path)
        if df is not None:
            print(f"📊 {s3_key} → {len(df)} filas")
