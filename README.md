# freeCodeCamp Certification Projects 🐍

All the certification projects and labs from the freeCodeCamp Python certification course.

## 📂 Projects

### 1. User Config Manager
`useronfigmanager.py`

A simple settings manager that lets you add, update, delete, and view user configuration settings stored in a dictionary. Built around string formatting, dictionary operations, and key/value normalization.

**Functions:**

- **`add_setting(settings, key_value)`**
  Adds a new setting to the dictionary.
  - Converts both key and value to lowercase before storing
  - Fails gracefully if the key already exists, without overwriting it
  - Returns a success or error message accordingly

- **`update_setting(settings, key_value)`**
  Updates the value of an existing setting.
  - Converts both key and value to lowercase
  - Fails gracefully if the key doesn't exist yet
  - Returns a success or error message accordingly

- **`delete_setting(settings, key)`**
  Removes a setting from the dictionary.
  - Converts the key to lowercase before checking/removing
  - Returns a success message if deleted, or an error if not found

- **`view_settings(settings)`**
  Displays all current settings.
  - Returns `"No settings available."` if the dictionary is empty
  - Otherwise returns a formatted, multi-line summary with each key capitalized


## 🛠️ Tech Stack
- Python 3
- Core dictionary and string manipulation (no external libraries)

## 📌 Status
Actively adding new certification projects as I progress through the course.
