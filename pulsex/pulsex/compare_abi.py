# This script assumes you have both ABIs in JSON format saved locally.

import json

def load_abi(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def compare_abis(abi1, abi2):
    abi1_funcs = {item['name'] for item in abi1 if item['type'] == 'function'}
    abi2_funcs = {item['name'] for item in abi2 if item['type'] == 'function'}

    only_in_abi1 = abi1_funcs - abi2_funcs
    only_in_abi2 = abi2_funcs - abi1_funcs
    in_both = abi1_funcs & abi2_funcs

    return only_in_abi1, only_in_abi2, in_both

# Load ABIs
pulsex_abi = load_abi('pulsex_abi.json')  # Replace with your actual file path
uniswapv2_abi = load_abi('uniswapv2_abi.json')  # Replace with your actual file path

# Compare ABIs
only_in_pulsex, only_in_uniswapv2, in_both = compare_abis(pulsex_abi, uniswapv2_abi)

# Print differences
print("Functions only in PulseX ABI:", only_in_pulsex)
print("Functions only in UniswapV2 ABI:", only_in_uniswapv2)
print("Functions in both ABIs:", in_both)

# You can run this script locally to get the differences in the function names between the two ABIs.
# Ensure you have the correct file paths for your ABIs.

