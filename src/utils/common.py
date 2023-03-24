def generate_hash_password(plaintext):
    from app import bcrypt
    return bcrypt.generate_password_hash(plaintext,11).decode('UTF-8')

def is_boolean (var):
    if (isinstance(var, bool)):
        return True
    
    bool_chars = ["true", "false", "ok", "ko", "yes", "no"]
    return var is not None and any(c == "{}".format(var).lower() for c in bool_chars)

def is_not_empty (var):
    if (isinstance(var, bool)):
        return var
    elif (isinstance(var, int)):
        return not var == 0
    elif (isinstance(var, list)):
        return len(var) > 0
    empty_chars = ["", "null", "nil", "false", "none"]
    return var is not None and not any(c == "{}".format(var).lower() for c in empty_chars)

def is_true (var):
    false_char = ["false", "ko", "no", "off"]
    return is_not_empty(var) and not any(c == "{}".format(var).lower() for c in false_char)

def is_false (var):
    return not is_true(var)

def is_empty (var):
    return not is_not_empty(var)

def is_numeric (var):
    if (isinstance(var, int)):
        return True
    return is_not_empty(var) and str(var).isnumeric()

def is_disabled (var):
    return is_empty(var) or "changeit" in var

def exists_entry(dictionary, key):
    return key in dictionary and is_not_empty(dictionary[key])

def safe_compare_entry(dictionary, key, expected_value):
    return exists_entry(dictionary, key) and is_not_empty(expected_value) and dictionary[key] == expected_value

def safe_contain_entry(dictionary, key, expected_contained_value):
    return exists_entry(dictionary, key) and is_not_empty(expected_contained_value) and expected_contained_value in dictionary[key]

def safe_get_entry_with_default(dictionary, key, default_value):
    return default_value if not exists_entry(dictionary, key) else dictionary[key]

def safe_get_entry(dictionary, key):
    return safe_get_entry_with_default(dictionary=dictionary, key=key, default_value=None)
