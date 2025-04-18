# 1. flush()
# Open a file in write mode
with open('example.txt', 'w') as file:
    file.write('Hello, World!')
        # Flush the output buffer to ensure the data is written to the file
    file.flush()

# 2. detach()
import io
buffer = io.BytesIO(b'Some initial binary data: x00x01')
stream = io.BufferedReader(buffer)
detached_buffer = stream.detach()

# 3. fileno()
file = open('example.txt', 'r')
fd = file.fileno()
print(f'The file descriptor is: {fd}')
  

  

