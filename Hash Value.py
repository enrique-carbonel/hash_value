import sys
import hashlib

def main():
    if len(sys.argv) < 2:
        print("No input file provided.")
        return

    if len(sys.argv) < 3:
        print("Hash algorithm not provided, using the default sha256 hash.")
        algorithm = 'sha256'
    else:
        algorithm = sys.argv[2]

    file_name = sys.argv[1]

    try:
        with open(file_name, "rb") as f:
            h = hashlib.new(algorithm)
            h.update(f.read())

        with open("output.txt", "w") as o:
            o.write(f"Hash for {file_name}: {h.hexdigest()}\n")
            o.write(f"Digest size (bytes): {h.digest_size}\n")
            o.write(f"Hash algorithm: {algorithm}\n")

    except FileNotFoundError:
        print("Failed to open", file_name)

if __name__ == "__main__":
    main()
