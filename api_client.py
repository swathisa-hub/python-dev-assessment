import requests

def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Error: Failed to fetch users.")
            return None

        users = response.json()

        if num_users > len(users):
            print(f"Only {len(users)} users available. Showing all of them.")
            num_users = len(users)

        for i in range(num_users):
            user = users[i]
            try:
                name = user["name"]
                email = user["email"]
                city = user["address"]["city"]
                print(f"Name: {name}, Email: {email}, City: {city}")
            except KeyError:
                print("Some user information is missing.")
    except requests.exceptions.RequestException:
        print("Network error occurred.")
    except Exception:
        print("Something went wrong.")
        
print("Fetching 3 users:")
fetch_and_display_users(3)

print("\nFetching 15 users (more than available):")
fetch_and_display_users(15)