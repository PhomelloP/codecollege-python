from pathlib import Path

# # Read contents of my_name.txt
path = Path('my_name.txt')
contents = path.read_text()
print(contents)

# # Split the contents into lines and print each line
lines = contents.splitlines()
for line in lines:
    print(line)

# Create and write to new_file.txt
new_path = Path('new_file.txt')
new_path.write_text('Today was a day that was being a day.')

with new_path.open('a') as file:
    file.write('\nInformation is integral to the development of young minds')
    

# Print contents of new_file.txt
print(new_path.read_text())
