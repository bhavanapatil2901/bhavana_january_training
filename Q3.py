def save_error(error, errors=None):
    if errors is None:      # safe handling of mutable default
        errors = []
    errors.append(error)
    return errors

# Multiple calls
print(save_error("E1"))
print(save_error("E2"))
print(save_error("E3"))
