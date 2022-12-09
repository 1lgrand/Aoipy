# Soon..`
global clients


def loadBotItems(bot):
    """Not for client-side use"""
    global clients
    clients = bot


def botUsername():
    global clients
    return clients.user


def botName():
    global clients
    return clients.user.name


def botID():
    global clients
    return clients.user.id


def botDiscriminator():
    global clients
    return clients.user.discriminator


def botOwnerID():
    global clients
    return clients.owner_id


def botIsOwner() -> bool:
    global clients
    return clients.is_owner
