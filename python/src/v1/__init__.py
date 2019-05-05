from flask import Blueprint, request, Response
import constants
import pymongo

api = Blueprint("v1", __name__)

@api.route("get_mongo")
def get_mongo():
    is_replicated = request.args.get("replication", "false")
    if is_replicated.lower() == "true":
        return constants.get_mongo(is_replicated=True)
    elif is_replicated.lower() == "false":
        return constants.get_mongo(is_replicated=False)
    else:
        return "Wrong value for replication parameter", 400

@api.route("test_mongo")
def test_mongo():
    host = request.args.get("host")
    port = request.args.get("port", "27017")
    if host is None or constants.host_regex.match(host) is None or int(port) > 65535 or int(port) < 1:
        return "Wrong host or port value", 400
    try:
        client = pymongo.MongoClient(f'mongodb://{host}:{port}/', socketTimeoutMS=5000, connectTimeoutMS=5000, serverSelectionTimeoutMS=5000)
        ping_response = client.test.command("ping")["ok"]
        return str(ping_response == 1.0), 200
    except pymongo.errors.ServerSelectionTimeoutError as e:
        return f"False", 200

@api.route("get_rabbit")
def get_rabbit():
    return constants.get_rabbit()