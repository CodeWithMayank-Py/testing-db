import os
from dotenv import load_dotenv
import psycopg2
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL')

try:
    conn = psycopg2.connect(DATABASE_URL)
    logger.info("Connection to database successful!")
    conn.close()
except Exception as e:
    logger.error(f"Error: {e}")
