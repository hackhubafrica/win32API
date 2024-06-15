import hashlib

def hash_file(file_path):
    try:
        with open(file_path, "rb") as f:
            file_content = f.read()
            hash_value = hashlib.sha256(file_content).hexdigest()
            return hash_value
    except Exception as e:
        print(f"Failed to hash file {file_path}: {str(e)}")
        return None

# Example usage
file_path = "C:\\Windows\\System32\\kernel32.dll"
hash_value = hash_file(file_path)
if hash_value:
    print(f"Hash value of {file_path}: {hash_value}")