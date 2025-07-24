from discord_interactions import verify_key
from os import getenv

# TODO: figure out sam stuff, it deploys shit but don't know what it deployed
# TODO: layers weren't created so it doesn't know about dependencies
# TODO: apparently it doesn't know what to do about the import from cloudwatch
# TODO: fix verify_key issue with not able to read body cause of string and bytes
PING_PONG = {"type": 1}
RESPONSE_TYPES = {
    "PONG": 1,
    "ACK_NO_SOURCE": 2,
    "MESSAGE_NO_SOURCE": 3,
    "MESSAGE_WITH_SOURCE": 4,
    "ACK_WITH_SOURCE": 5,
}


def ping_pong(body):
    if body.get("type") == 1:
        return True
    return False


def lambda_handler(event, context):
    print(f"event {event}")
    # verify the signature
    try:
        is_verified = verify_key(
            raw_body=event.get("body"),
            signature=event.get("headers", {}).get("x-signature-ed25519"),
            timestamp=event.get("headers", {}).get("x-signature-timestamp"),
            client_public_key=getenv("DISCORD_PUBLIC_KEY"),
        )
        print(is_verified)
    except Exception as e:
        print(f"[UNAUTHORIZED] Invalid request signature: {e}")
        return {
            "statusCode": 401,
            "body": "Unauthorized",
            "headers": {"Content-Type": "application/json"},
        }

    # check if message is a ping
    body = event.get("body-json")
    if ping_pong(body):
        return PING_PONG

    # dummy return
    return {
        "type": RESPONSE_TYPES["MESSAGE_NO_SOURCE"],
        "data": {
            "tts": False,
            "content": "BEEP BOOP",
            "embeds": [],
            "allowed_mentions": [],
        },
    }
