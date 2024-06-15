import os

def get_environment_variable(var_name):
    """Get the value of the environment variable or return None if it does not exist."""
    return os.environ.get(var_name)

def main():
    # Print all environment variables
    print("All Environment Variables:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")

    # Get a specific environment variable
    var_name = 'ComSpec'  # You can change this to any environment variable you want to access
    var_value = get_environment_variable(var_name)

    if var_value:
        print(f"\nValue of '{var_name}': {var_value}")
    else:
        print(f"\nEnvironment variable '{var_name}' is not set.")

if __name__ == "__main__":
    main()