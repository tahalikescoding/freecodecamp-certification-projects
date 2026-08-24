"""
CERTIFICATION PROJECT 1

You should define a function named add_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair

add_setting function should:

Convert the key and value to lowercase.
If the key setting exists, return Setting '[key]' already exists! Cannot add a new setting with this name.
If the key setting doesn't exist, add the key-value pair to the given dictionary of settings and return Setting '[key]' added with value '[value]' successfully!.
The messages returned should have the key and value in lowercase.
You should define a function named update_setting with two parameters representing a dictionary of settings and a tuple containing a key-value pair.

update_setting function should:

Convert the key and value to lowercase.
If the key setting exists, update its value in the given dictionary of settings and return: Setting '[key]' updated to '[value]' successfully!
If the key setting doesn't exist, return Setting '[key]' does not exist! Cannot update a non-existing setting.
The messages returned should have the key and value in lowercase.
You should define a function named delete_setting with two parameters representing a dictionary of settings and a key.

delete_setting function should:

Convert the key passed to lowercase.
If the key setting exists, remove the key-value pair from the given dictionary of settings and return Setting '[key]' deleted successfully!
If the key setting does not exist, return Setting not found!
The messages returned should have the key in lowercase.
You should define a function named view_settings with one parameter representing a dictionary of settings.

view_settings function should:

Return No settings available. if the given dictionary of settings is empty.
If the dictionary contains any settings, return a string displaying the settings. The string should start with Current User Settings: followed by the key-value pairs, each on a new line and with the key capitalized. For example, view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}) should return:
Current User Settings:
Theme: dark
Notifications: enabled
Volume: high

For testing the code, you should create a dictionary named test_settings to store some user configuration preferences.

"""


test_settings = {"theme":'dark' , "volume":"high"}

def add_setting(setting , new_settings):
    old_settings = setting.copy()
    setting.clear()
    for key , value in old_settings.items():
        setting[key.lower()] = value.lower()
    new_key , new_value = new_settings
    if new_key.lower() in setting:
        return f"Setting '{new_key.lower()}' already exists! Cannot add a new setting with this name."
    else:
        setting[new_key.lower()] = new_value.lower()
        return f"Setting '{new_key.lower()}' added with value '{setting[new_key.lower()]}' successfully!"

def update_setting(setting , update_settings):
    old_settings = setting.copy()
    setting.clear()
    for key , value in old_settings.items():
        setting[key.lower()] = value.lower()
    update_key , update_value = update_settings 
    if update_key.lower() in setting:
        setting[update_key.lower()] = update_value.lower()
        return f"Setting '{update_key.lower()}' updated to '{update_value.lower()}' successfully!"
    else:
        return f"Setting '{update_key.lower()}' does not exist! Cannot update a non-existing setting."

def delete_setting(setting , key):
    key = key.lower()
    if key in setting:
        setting.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(setting):
    if not setting:
        return "No settings available."
    else:
        result ="Current User Settings:\n"
        for key,value in setting.items():
            result += f"{key.capitalize()}: {value.lower()}\n"
        return result

