# Optimized code:
import Globals
import requests

# All functions have been refactored to use less code, setting the same payload and header values for each. 
# These can now be set outside of each function and passed in as parameters.
# The code is now more readable and easier to maintain.
def PassPromptToSelfBot(prompt : str, payload, header):
    payload["data"]["options"] = [{"type":3,"name":"prompt","value":prompt}]
    payload["data"]["application_command"] = {
                                "id":"938956540159881230",
                                "application_id":"936929561302675456",
                                "version":"994261739745050686",
                                "default_permission":True,
                                "default_member_permissions":None,
                                "type":1,
                                "name":"imagine",
                                "description":"There are endless possibilities...",
                                "dm_permission":True,
                                "options":[{"type":3,"name":"prompt","description":"The prompt to imagine","required":True}]
                            }
    response = requests.post("https://discord.com/api/v9/interactions", json = payload, headers = header)
    return response

def Upscale(index : int, messageId : str, messageHash : str, payload, header):
    payload["message_id"] = messageId
    payload["data"]["custom_id"] = "MJ::JOB::upsample::{}::{}".format(index, messageHash)
    response = requests.post("https://discord.com/api/v9/interactions", json = payload, headers = header)
    return response


def MaxUpscale(messageId : str, messageHash : str, payload, header):
    payload["message_id"] = messageId
    payload["data"]["custom_id"] = "MJ::JOB::upsample_max::1::{}::SOLO".format(messageHash)
    response = requests.post("https://discord.com/api/v9/interactions", json = payload, headers = header)
    return response


def Variation(index : int, messageId : str, messageHash : str, payload, header):
    payload["message_id"] = messageId
    payload["data"]["custom_id"] = "MJ::JOB::variation::{}::{}".format(index, messageHash)
    response = requests.post("https://discord.com/api/v9/interactions", json = payload, headers = header)
    return response

# Set payload and header values to be used by each function
payload = {"type":3,
    "guild_id":Globals.SERVER_ID,
    "channel_id":Globals.CHANNEL_ID,
    "message_flags":0,
    "application_id":"936929561302675456",
    "session_id":"1f3dbdf09efdf93d81a3a6420882c92c",
    "data":{"component_type":2}}
header = {
    'authorization' : Globals.SALAI_TOKEN
}