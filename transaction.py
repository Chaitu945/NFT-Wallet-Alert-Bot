from alchemy import get_transaction_receipt

SEAPORT_CONTRACTS = {
    "0x0000000000000068f116a894984e2db1123eb395",
    "0x00000000006c3852cbef3e08e8df289169ede581",
}


def classify_transaction(tx_hash):

    receipt = get_transaction_receipt(tx_hash)

    result = receipt.get("result")

    if not result:
        return {
            "type": "RECEIVED",
            "marketplace": None,
        }

    logs = result.get("logs", [])

    for log in logs:

        address = log["address"].lower()

        if address in SEAPORT_CONTRACTS:

            return {
                "type": "PURCHASE",
                "marketplace": "OpenSea",
            }

    return {
        "type": "RECEIVED",
        "marketplace": None,
    }