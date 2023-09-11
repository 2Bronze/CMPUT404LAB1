import requests as rq

# Print request version
def main():
    print(rq.__version__)
    # Get google
    response = rq.get("https://www.google.com")
    print(response)
    # Get raw python script and print the text
    raw_script_res = rq.get("https://raw.githubusercontent.com/2Bronze/CMPUT404LAB1/main/requestsverion.py")
    print(raw_script_res.text)
    
if __name__ == "__main__":
    main()


