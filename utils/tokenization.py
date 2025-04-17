from authlib.jose import JsonWebToken

# private key creation: openssl genrsa -out private_key.pem
# public key creation: openssl rsa -in private_key.pem -pubout -out public_key.pem

# algorithm used for token creation
header = {"alg": "RS256"}
private_key = ""
public_key = ""

with open("private_key.pem", "r") as file:
    private_key = file.read()

with open("public_key.pem", "r") as file:
    public_key = file.read()


jwt = JsonWebToken(["RS256"])


# create token
def create_token(payload: dict) -> str:
    """create token for authenticated user"""
    token = jwt.encode(header, payload, private_key)
    return token.decode()


def decode_token(token: str) -> dict:
    """decode token and send back the payload data"""
    return jwt.decode(token, public_key)
