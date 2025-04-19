from authlib.jose import JsonWebToken
from pathlib import Path

# Path to current file (jwt_utils.py)
current_dir = Path(__file__).parent

# File paths
private_key_path = current_dir / "private_key.pem"
public_key_path = current_dir / "public_key.pem"
# private key creation: openssl genrsa -out private_key.pem
# public key creation: openssl rsa -in private_key.pem -pubout -out public_key.pem

# REMOVE PRIVATE AND PUBLIC key from github
# algorithm used for token creation
header = {"alg": "RS256"}
private_key = ""
public_key = ""

with open(private_key_path, "r") as file:
    private_key = file.read()

with open(public_key_path, "r") as file:
    public_key = file.read()


jwt = JsonWebToken(["RS256"])


# create token
def create_token(payload: dict) -> str:
    """create token for authenticated user"""
    token = jwt.encode(header, payload, private_key)
    return token.decode()


# decode token to get payload
def decode_token(token: str) -> dict:
    """decode token and send back the payload data"""
    return jwt.decode(token, public_key)
