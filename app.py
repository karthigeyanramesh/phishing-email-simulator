"""
The below modules are required to fetch the user details 
we could then use those information to find more data
"""

from datetime import datetime
import os
import json
import logging
from flask import Flask, send_file, request

app = Flask(__name__)

# Create the logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename="logs/download_logs.txt",  # This is your log file where user info will be logged
    level=logging.INFO,  # Set to INFO so it will capture the user info logs
    format="%(asctime)s - %(message)s"  # Add timestamp to each log entry
)

# Configure logging to save logs in the desired folder
# Logs will be saved in the 'logs/' folder - So each user will have their info 
# on the same page in different lines
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/download')
def download_pdf():
    """
    The following function gets the user's data
    """
    # Capture user information from the request
    user_info = {
        "ip_address": request.remote_addr,
        "user_agent": request.headers.get('User-Agent'),
        "referrer": request.headers.get('Referer', 'No referrer'),
        "accept_language": request.headers.get('Accept-Language', 'Unknown'),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Log the user information in the JSON format
    logging.info("User Info: %s", json.dumps(user_info))

    # Optionally, print the JSON object to the console (for debugging purposes)
    print(user_info)

    # Provide the file path to your PDF
    pdf_path = 'data-link-layer.pdf'

    return send_file(pdf_path, as_attachment=True)

# Render will do the job for us

# if __name__ == '__main__':
#     app.run(debug=False, port=5000)
