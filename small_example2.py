def fetch_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()
            quote = data[0]["q"]
            author = data[0]["a"]
            return f"“{quote}” — {author}"
        else:
            return "Failed to fetch a quote. Please try again later."
    except Exception as e:
        return f"An error occurred: {e}"