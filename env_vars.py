import os

email_user = os.environ.get('EMAIL_USER')
email_pass = os.environ.get('EMAIL_PASS')
secret_key = os.environ.get('SECRET_KEY')
sql_uri = os.environ.get('SQLALCHEMY_DATABASE_URI')

print(email_user)
print(email_pass)
print(secret_key)
print(sql_uri)
