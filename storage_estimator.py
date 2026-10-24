# Storage Estimator
size_mb = float(input("Enter file size in MB: "))
count = int(input("Enter number of files: "))
total_mb = size_mb * count
print("Total storage needed:", total_mb, "MB")
print("Estimate complete")
print("Total in GB:", total_mb / 1024)