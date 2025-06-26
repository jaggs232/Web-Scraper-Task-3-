import requests
from bs4 import BeautifulSoup

try:
    print("Getting webpage...")
    url = "https://httpbin.org/html" 
    page = requests.get(url)
    print("✓ Got webpage!")
    

    soup = BeautifulSoup(page.content, 'html.parser')
    
    headlines = soup.find_all('h1')
    

    with open('headlines.txt', 'w') as file:
        file.write("TEST HEADLINES\n")
        file.write("-" * 20 + "\n\n")
        
        if headlines:
            for i, headline in enumerate(headlines, 1):
                title = headline.get_text().strip()
                file.write(f"{i}. {title}\n")
                print(f"{i}. {title}")
        else:
            file.write("No headlines found\n")
            print("No headlines found")
    
    print("\n✓ Done! Check 'headlines.txt' file")
except Exception as e:
    print(f"Error: {e}")
    print("\nTry installing libraries:")
    print("pip install requests beautifulsoup4")
