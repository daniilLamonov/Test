from tronpy.providers import HTTPProvider
from tronpy import Tron
from tronpy.exceptions import AddressNotFound
from dotenv import load_dotenv
import os

load_dotenv()
TRON_API_KEY = os.getenv("TRON_API_KEY")

def get_wallet_info(address: str) -> dict:
    client = Tron(HTTPProvider(api_key=TRON_API_KEY))

    try:
        resources = client.get_account_resource(address)
        balance = float(client.get_account_balance(address))

    except AddressNotFound:
        return {"error": "Address not found"}

    bandwidth_used = resources.get("NetUsed") or resources.get("freeNetUsed") or 0
    net_limit = resources.get("NetLimit", 0)
    free_net_limit = resources.get("freeNetLimit")
    bandwidth_limit = net_limit + free_net_limit
    energy_used = resources.get("EnergyUsed", 0)
    energy_limit = resources.get("EnergyLimit", 0)

    total_bandwidth = int(bandwidth_limit) - int(bandwidth_used)
    total_energy = energy_limit - energy_used

    return {
        "address": address,
        "balance": balance,
        "bandwidth": total_bandwidth,
        "energy": total_energy,
    }
