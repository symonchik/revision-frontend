from dotenv import dotenv_values

config = dotenv_values(".env")

SUPABASE_URL = config['SUPABASE_URL']