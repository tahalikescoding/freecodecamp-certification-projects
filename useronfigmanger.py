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

