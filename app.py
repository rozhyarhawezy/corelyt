import mysql.connector
from db import get_db_connection 
from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
import pdfplumber
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import uuid
import os
import joblib

# ------------------------------

import mysql.connector
from db import get_db_connection 
from flask import Flask, render_template
from datetime import date

# getting the connection
try:
    conn = get_db_connection()
    if conn.is_connected():
        print("Connected database successfully!")
    conn.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")


app = Flask(__name__)
app.secret_key = "my_super_secret_key_123!"  # MUST be set here

# ==============================================================

from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "hidden_secret_key"  # Secret key placeholder

# ==============================================================
# LOGIN ROUTES
# ==============================================================

@app.route('/')
def login_page():
    return render_template('login.html')  # Login page

@app.route('/login', methods=['POST'])
def login():
    # --- Logic hidden ---
    return redirect(url_for('dashboard'))

# ==============================================================
# DASHBOARD
# ==============================================================

@app.route('/dashboard')
def dashboard():
    # --- Logic hidden ---
    return render_template('dashboard.html')

# ==============================================================
# TO-DO EXAMPLE
# ==============================================================

@app.route('/add_todo', methods=['POST'])
def add_todo():
    # --- Logic hidden ---
    return redirect(url_for('dashboard'))

# ==============================================================
# CV ANALYZER (ML placeholder)
# ==============================================================

@app.route('/analyze_cv', methods=['POST'])
def analyze_cv():
    # --- Logic hidden ---
    return render_template('result.html', chance=0.0, name="Name", skills=[], languages=[])

# ==============================================================
# EMPLOYEE LIST
# ==============================================================

@app.route('/employees')
def employees():
    # --- Logic hidden ---
    return render_template('employees.html', employees=[])

# ==============================================================
# LOGOUT
# ==============================================================

@app.route('/logout')
def logout():
   #-- Logic hidden -- 
    return redirect(url_for('login_page'))

# ==============================================================
# --------
# ==============================================================

if __name__ == '__main__':
    app.run(debug=True)