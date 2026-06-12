import requests
from datetime import datetime

def get_weather(location="Thiruvananthapuram"):
    try:
        # format=3 provides a short format with weather condition and temperature
        url = f"https://wttr.in/{location}?format=3"
        response = requests.get(url)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        return f"Could not fetch weather: {e}"

def get_quote():
    try:
        url = "https://zenquotes.io/api/random"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        return f"\"{quote}\" - {author}"
    except requests.exceptions.RequestException as e:
        return f"Could not fetch quote: {e}"

def main():
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    weather = get_weather("Thiruvananthapuram") # Defaulting to London as a generic example
    quote = get_quote()

    summary = f"""
======================================
         DAILY PULSE SUMMARY
======================================
Date/Time : {date_str}

Weather   : {weather}

Quote of the Day:
{quote}
======================================
"""
    
    print(summary)
    
    # Save the summary to a file so it can be downloaded via GitHub Actions
    with open("daily_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    
    print("Summary saved to summary.txt")

if __name__ == "__main__":
    main()
