import sys
import urllib.request
import json

def check(token):
    try:
        req = urllib.request.Request(
            "https://discord.com/api/v9/users/@me",
            headers={"Authorization": token}
        )
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read())
    except:
        return None

if __name__ == "__main__":
    token = sys.argv[1]
    user = check(token)
    if user:
        print(f"valid token!")
        print(f"user: {user.get('username')}")
        print(f"id: {user.get('id')}")
        print(f"nitro: {bool(user.get('premium_type'))}")
    else:
        print("invalid token")
