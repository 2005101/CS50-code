def main():
    name=input("File name: ")
    if ".gif" in name:
        print("image/gif")
    elif ".jpg" in name:
        print("image/jpeg")
    elif ".jpeg" in name:
        print("image/jpeg")
    elif ".png" in name:
        print("image/png")
    elif ".pdf" in name:
        print("image/pdf")
    elif ".txt" in name:
        print("image/txt")
    elif ".zip" in name:
        print("image/zip")
    else:
        print("application/octet-stream")

main()
