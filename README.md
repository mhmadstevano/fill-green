<p align="center">
  <img width="779" height="210" alt="image" src="https://github.com/user-attachments/assets/c35274e7-cf30-4462-b0ac-6ac08ead329a" />
</p>

# Git Commit Generator

A small Python script that automatically generates commits for a given date range.  
Useful for filling the GitHub contribution graph, testing Git workflows, or experimenting with commit history.  

## ✨ Features
- Set **start and end date** for commits
- Flexible commits per day: random range (e.g. COMMITS_PER_DAY = (2, 4))
- Automatic commit timestamps
- Optional push to remote (`origin`)

## 🔧 Requirements
- Python **3.10+** must be installed on your system
- Git must be available in `$PATH`

## 🚀 Quick start

### ✨ Clone the repository:

```bash
git clone https://github.com/lifan2029/fill-green.git
```

### ✨ Delete old `.git` directory

#### Linux / macOS
```bash
rm -rf .git
```

#### Windows (CMD)
```bash
rmdir /s /q .git
```

#### Windows (Powershell)
```bash
Remove-Item -Recurse -Force .git
```

### ✨ Install dependency:

```bash
pip install GitPython
```

### ✨ Before running the script, open `main.py` and set the parameters:

```python
COMMITS_PER_DAY = (2, 4)     # number of commits per day (fixed: 3 or range: (2, 4))
START_DATE = "2024-01-01"    # first commit date
END_DATE   = "2024-10-04"    # last commit date
```

### ✨ Start script and enjoy
```bash
python main.py
```

## ⭐ Support

If you like this project, please consider giving it a **star** on GitHub!  
It helps others discover the repo and motivates me to improve it 🚀
