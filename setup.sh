#!/bin/bash

echo "Starting Django environment setup..."

set -e

cd "$(dirname "$0")"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then

    echo "❌ Python 3 not found. Please install it before continuing."
    exit 1

fi

# Check if virtualenv is installed, if not install it
if ! python3 -m virtualenv --version &> /dev/null; then

    echo "🔧 Installing virtualenv..."
    python3 -m pip install --upgrade pip
    python3 -m pip install virtualenv

fi

# Create virtual environment if it does not exist
if [ ! -d "venv" ]; then

    echo "📦 Creating virtual environment..."
    python3 -m virtualenv venv

else

    echo "✅ Virtual environment already exists."

fi

# Activate virtual environment
echo "⚙️  Activating virtual environment..."
source ./venv/bin/activate

# Install dependencies
if [ -f "./requirements.txt" ]; then

    echo "📚 Installing dependencies from requirements.txt..."
    pip3 install -r requirements.txt

    playwright install chromium

else

    echo "⚠️  requirements.txt not found. Skipping dependency installation."

fi

# Generate .env from .env-example if exists
if [ ! -f ".env" ] && [ -f ".env-example" ]; then

    echo "📄 Generating .env from .env-example..."
    cp .env-example .env

elif [ -f ".env" ]; then

    echo "✅ .env file already exists."

else

    echo "⚠️  No .env-example found. Skipping .env creation."

fi

# Create empty SQLite database if it does not exist
if [ ! -f "db.sqlite3" ]; then

    echo "🗄️  Creating empty SQLite database..."
    python manage.py migrate

else

    echo "✅ db.sqlite3 database already exists."

fi

echo "✅ Setup completed! To activate the virtual environment, run:"
echo "   source venv/bin/activate"
