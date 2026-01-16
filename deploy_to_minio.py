import boto3

def upload_to_minio(file_path, bucket_name, object_name):
    s3 = boto3.resource(
        's3',
        endpoint_url='http://localhost:9000',
        aws_access_key_id='minioadmin',
        aws_secret_access_key='minioadmin'
    )
    s3.Bucket(bucket_name).upload_file(file_path, object_name)

if __name__ == "__main__":
    upload_to_minio("output/transformed.csv", "data-bucket", "transformed.csv")
