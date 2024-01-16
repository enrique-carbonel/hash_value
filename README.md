# hash_value
Python script that calculates the hash value of a file using the hashlib library and saves the result to an output file.

FUNCTION MAIN: 
  Checks if the script is provided with the necessary command-line arguments (input file path and hash algorithm).
  If no input file is provided, it prints an error message and exits.
  If no hash algorithm is provided, it uses the default sha256.
  Opens the specified input file in binary mode for reading.
  Checks if the provided hash algorithm is available; if not, it defaults to sha256.
  Creates a hashlib object based on the chosen hash algorithm.
  Reads the content of the input file and updates the hashlib object with it.
  Opens an output file in write mode.
  Writes the hash value, digest size, and algorithm information to the output file.
  Closes both the input and output files.
