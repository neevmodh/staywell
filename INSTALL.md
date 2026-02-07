# 🚀 Installation & Setup Guide

## Prerequisites

Before you begin, ensure you have:
- **Python 3.8 or higher** installed
- **pip** package manager
- **Terminal/Command Prompt** access
- **Web browser** (Chrome, Firefox, Safari, or Edge)

---

## Step-by-Step Installation

### 1. Navigate to Project Directory

```bash
cd staywell
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**Expected output**:
```
Collecting streamlit
Collecting pandas
Collecting numpy
Collecting matplotlib
Collecting seaborn
...
Successfully installed streamlit-X.X.X pandas-X.X.X ...
```

**If you encounter permission errors**, try:
```bash
pip install --user -r requirements.txt
```

### 3. Verify Installation

Run the system test:
```bash
python test_system.py
```

**Expected output**:
```
============================================================
STAYWELL SYSTEM TEST
============================================================
Testing imports...
✅ All imports successful
...
✅ ALL TESTS PASSED - System is ready!
```

---

## Running the Application

### Method 1: Streamlit Web Interface (Recommended)

```bash
streamlit run app.py
```

**What happens**:
1. Streamlit server starts
2. Browser opens automatically at `http://localhost:8501`
3. Application loads with the main dashboard

**If browser doesn't open automatically**:
- Manually navigate to: `http://localhost:8501`
- Or use the "Local URL" shown in terminal

**To stop the server**:
- Press `Ctrl+C` in terminal

### Method 2: Command Line Analysis

For batch processing without UI:
```bash
python analysis_script.py data/sample_students.csv
```

**Output**: Statistical report printed to terminal + results CSV saved

---

## Troubleshooting

### Issue: "Command not found: streamlit"

**Solution**:
```bash
# Ensure pip installed correctly
pip list | grep streamlit

# If not found, reinstall
pip install --upgrade streamlit
```

### Issue: "ModuleNotFoundError: No module named 'X'"

**Solution**:
```bash
# Install missing module
pip install X

# Or reinstall all dependencies
pip install -r requirements.txt --force-reinstall
```

### Issue: "Port 8501 already in use"

**Solution**:
```bash
# Use a different port
streamlit run app.py --server.port 8502
```

### Issue: Charts not displaying

**Solution**:
```bash
# Reinstall matplotlib and seaborn
pip install --upgrade matplotlib seaborn
```

### Issue: CSV upload fails

**Possible causes**:
1. **Incorrect column names** - Must match exactly: `sleep_hours`, `study_hours`, `screen_time`, `stress_level`, `attendance`
2. **Invalid values** - Check ranges (hours: 0-24, stress: 1-5, attendance: 0-100)
3. **Missing data** - Ensure no empty cells
4. **Wrong encoding** - Save CSV as UTF-8

---

## Platform-Specific Instructions

### macOS

```bash
# If using Homebrew Python
brew install python3
pip3 install -r requirements.txt
python3 test_system.py
streamlit run app.py
```

### Windows

```bash
# Use Command Prompt or PowerShell
cd staywell
pip install -r requirements.txt
python test_system.py
streamlit run app.py
```

### Linux

```bash
# May need python3 explicitly
sudo apt-get install python3-pip  # Ubuntu/Debian
pip3 install -r requirements.txt
python3 test_system.py
streamlit run app.py
```

---

## Virtual Environment (Recommended)

Using a virtual environment keeps dependencies isolated:

### Create Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### Install in Virtual Environment

```bash
pip install -r requirements.txt
python test_system.py
streamlit run app.py
```

### Deactivate

```bash
deactivate
```

---

## Verifying Installation

### Quick Check

```bash
# Check Python version
python --version  # Should be 3.8+

# Check pip
pip --version

# Check installed packages
pip list
```

### Full System Test

```bash
# Run comprehensive test
python test_system.py

# Should show:
# ✅ ALL TESTS PASSED - System is ready!
```

### Test with Sample Data

```bash
# CLI test
python analysis_script.py data/sample_students.csv

# Should generate report and save results
```

---

## First Run Checklist

After installation, verify:

- [ ] All dependencies installed (`pip list`)
- [ ] System test passes (`python test_system.py`)
- [ ] Streamlit starts (`streamlit run app.py`)
- [ ] Browser opens to app
- [ ] Sample data loads
- [ ] All tabs accessible
- [ ] Charts display correctly
- [ ] CSV upload works
- [ ] Manual entry works

---

## Performance Optimization

### For Large Datasets (1000+ students)

```bash
# Increase memory limit
streamlit run app.py --server.maxUploadSize 200
```

### For Slow Loading

```bash
# Enable caching
streamlit run app.py --server.enableCORS false
```

---

## Updating the Application

### Update Dependencies

```bash
pip install --upgrade -r requirements.txt
```

### Clear Cache

```bash
# Clear Streamlit cache
streamlit cache clear
```

---

## Uninstallation

### Remove Dependencies

```bash
pip uninstall -r requirements.txt -y
```

### Remove Virtual Environment

```bash
# Deactivate first
deactivate

# Remove directory
rm -rf venv  # macOS/Linux
rmdir /s venv  # Windows
```

---

## Getting Help

### Check Logs

Streamlit logs appear in terminal - look for error messages

### Test Individual Components

```python
# Test imports
python -c "import streamlit; import pandas; print('OK')"

# Test data loading
python -c "import pandas as pd; df = pd.read_csv('data/sample_students.csv'); print(len(df))"
```

### Common Solutions

1. **Restart terminal** after installation
2. **Update pip**: `pip install --upgrade pip`
3. **Check Python path**: `which python` (macOS/Linux) or `where python` (Windows)
4. **Reinstall from scratch**: Delete venv and start over

---

## Next Steps

After successful installation:

1. **Read QUICKSTART.md** for usage guide
2. **Explore sample data** to learn interface
3. **Upload your CSV** for real analysis
4. **Review METHODOLOGY.md** for statistical details
5. **Check UI_GUIDE.md** for feature overview

---

## System Requirements

### Minimum
- Python 3.8+
- 2GB RAM
- 100MB disk space
- Modern web browser

### Recommended
- Python 3.9+
- 4GB RAM
- 500MB disk space
- Chrome or Firefox browser

---

## Support

If you encounter issues:

1. Run `python test_system.py` to diagnose
2. Check error messages in terminal
3. Verify Python version: `python --version`
4. Ensure all dependencies installed: `pip list`
5. Try in a fresh virtual environment

---

**Installation complete! Run `streamlit run app.py` to start.** 🚀
