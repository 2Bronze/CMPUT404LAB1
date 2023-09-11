import requests as rq

# Print request version
def main():
    print(rq.__version__)
    response = rq.get("https://www.google.com")
    print(response)
    
if __name__ == "__main__":
    main()


