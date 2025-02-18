import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase credentials from the downloaded JSON file
cred = credentials.Certificate("skillmatcher-firebase.json")  # Your Firebase key file
firebase_admin.initialize_app(cred)

# Connect to Firestore Database
db = firestore.client()

# Function to save resume data to Firestore
def save_resume_data(user_id, resume_data):
    db.collection("resumes").document(user_id).set(resume_data)

# Function to retrieve job listings from Firestore
def get_all_jobs():
    jobs_ref = db.collection("jobs")
    return [job.to_dict() for job in jobs_ref.stream()]

