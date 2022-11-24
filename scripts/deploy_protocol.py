import sys
import asyncio
from starknet_py.net.account.account_client import (AccountClient)
from starknet_py.net.signer.stark_curve_signer import KeyPair
from starkware.crypto.signature.signature import private_to_stark_key
from starknet_py.net.gateway_client import GatewayClient
from utils import deployContract
from pathlib import Path

#Configure Admin AccountClient
private_key = int(sys.argv[0])
account_address = int(sys.argv[1],16)
public_key = private_to_stark_key(private_key)
signer_key_pair = KeyPair(private_key,public_key)
client = AccountClient(address=account_address, client=GatewayClient(net=str(sys.argv[3])), key_pair=signer_key_pair, supported_tx_version=1)

async def deployKakarot():

    print("----------------------------------")
    print("--- Deploying Kakarot Protocol ---")
    print("----------------------------------")
    print(".")
    print(".")
    print(".")

    #################################
    #                               #
    #   DECLARE & DEPLOY CONTRACTS  #
    #                               #
    #################################

    # Declare EVM Contract

    # Declare Kakarot

    # Deploy ERC20

    # Deploy Kakarot Proxy
    print("Deploying Kakarot Proxy")
    compiled_contract = Path("./build/", "kakarot_proxy.json").read_text("utf-8")
    contract_address = await deployContract(client=client,compiled_contract=compiled_contract,calldata=[
        account_address,
        eth.contract_address,
        contract_account_class.class_hash
    ])
    print("Kakarot Proxy Address: ",contract_address)

    # Deploy Registry
    print("Deploying Account Registry")
    compiled_contract = Path("./build/", "account_registry.json").read_text("utf-8")
    contract_address = await deployContract(client=client,compiled_contract=compiled_contract,calldata=[])
    print("Account Registry Address: ",contract_address)

    ##########################
    #                        #
    #   CONFIGURE CONTRACTS  #
    #                        #
    ##########################   

    # Configure Kakarot Proxy
    print("...Configuring Kakarot Proxy...")
    # Set Kakarot Implementation
    # Set Solver Registry
    
    invocation = await hubContract.functions["set_solver_registry"].invoke(solverRegistryContract.address,max_fee=50000000000000000000)
    print("Setting Solver Registry...")
    await invocation.wait_for_acceptance()
    #Set Trade Executioner
    print("Setting TradeExecutioner Hash...")
    invocation = await hubContract.functions["set_executor"].invoke(execution_contract_hash,max_fee=50000000000000000000)
    await invocation.wait_for_acceptance()

asyncio.run(deployKakarot())

