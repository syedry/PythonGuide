#Store key-value pairs. You use the key to access the corresponding value. 
#Where a list index is always a number, a dictionary key can be a different data type, like a string, integer, float, or even tuples

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

print(file_counts["txt"])

print("jpg" in file_counts)
print("html" in file_counts)

del file_counts["py"]
print(file_counts)

for ext, amount in file_counts.items():
  print("There are {} files with the .{} extension".format(amount, ext))

print(file_counts.keys())
print(file_counts.values())