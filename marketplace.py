from alchemy import get_transaction_receipt


def is_opensea_purchase(tx_hash):

    receipt = get_transaction_receipt(tx_hash)

    if "result" not in receipt:
        return False

    logs = receipt["result"]["logs"]

    # Known OpenSea Seaport contracts
    SEAPORT_CONTRACTS = {
        "0x0000000000000068f116a894984e2db1123eb395".lower(),  # Seaport 1.6
        "0x00000000006c3852cbef3e08e8df289169ede581".lower(),  # Seaport 1.5
    }

    for log in logs:
        if log["address"].lower() in SEAPORT_CONTRACTS:
            return True

    return False