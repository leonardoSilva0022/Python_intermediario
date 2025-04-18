import os
from web3 import Web3
from web3.middleware import geth_poa_middleware
from dotenv import load_dotenv
import json

# Carregar variáveis de ambiente
load_dotenv()

# Configurações
ALCHEMY_API_KEY = os.getenv("ALCHEMY_API_KEY")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
WALLET_ADDRESS = "your_wallet_address"  # Substitua pelo endereço da sua carteira MetaMask

# Conectar à rede Base via Alchemy
BASE_RPC_URL = f"https://base-mainnet.g.alchemy.com/v2/{ALCHEMY_API_KEY}"
w3 = Web3(Web3.HTTPProvider(BASE_RPC_URL))

# Adicionar middleware para compatibilidade com Base (PoA)
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Verificar conexão
if not w3.is_connected():
    raise Exception("Não foi possível conectar à rede Base")

# Configurar conta
account = w3.eth.account.from_key(PRIVATE_KEY)

# Endereços dos contratos Uniswap V3 na Base (verificar no docs.uniswap.org)
NONFUNGIBLE_POSITION_MANAGER_ADDRESS = "0xC36442b4a4522E871399CD717aBDD847Ab11FE88"
UNISWAP_V3_FACTORY_ADDRESS = "0x33128a8fC17869897dcE68Ed026d694621f6FDfD"

# ABI simplificado do NonfungiblePositionManager (apenas função mint)
NONFUNGIBLE_POSITION_MANAGER_ABI = json.loads('''
[
    {
        "constant": false,
        "inputs": [
            {
                "components": [
                    {"name": "token0", "type": "address"},
                    {"name": "token1", "type": "address"},
                    {"name": "fee", "type": "uint24"},
                    {"name": "tickLower", "type": "int24"},
                    {"name": "tickUpper", "type": "int24"},
                    {"name": "amount0Desired", "type": "uint256"},
                    {"name": "amount1Desired", "type": "uint256"},
                    {"name": "amount0Min", "type": "uint256"},
                    {"name": "amount1Min", "type": "uint256"},
                    {"name": "recipient", "type": "address"},
                    {"name": "deadline", "type": "uint256"}
                ],
                "name": "params",
                "type": "tuple"
            }
        ],
        "name": "mint",
        "outputs": [
            {"name": "tokenId", "type": "uint256"},
            {"name": "liquidity", "type": "uint128"},
            {"name": "amount0", "type": "uint256"},
            {"name": "amount1", "type": "uint256"}
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
''')

# Configurar contrato
position_manager = w3.eth.contract(
    address=NONFUNGIBLE_POSITION_MANAGER_ADDRESS,
    abi=NONFUNGIBLE_POSITION_MANAGER_ABI
)

# Função para adicionar liquidez
def add_liquidity(
    token0,
    token1,
    fee,
    tick_lower,
    tick_upper,
    amount0_desired,
    amount1_desired,
    amount0_min,
    amount1_min,
    recipient,
    deadline
):
    # Construir a transação
    mint_params = {
        "token0": token0,
        "token1": token1,
        "fee": fee,
        "tickLower": tick_lower,
        "tickUpper": tick_upper,
        "amount0Desired": amount0_desired,
        "amount1Desired": amount1_desired,
        "amount0Min": amount0_min,
        "amount1Min": amount1_min,
        "recipient": recipient,
        "deadline": deadline
    }

    transaction = position_manager.functions.mint(mint_params).build_transaction({
        "from": WALLET_ADDRESS,
        "nonce": w3.eth.get_transaction_count(WALLET_ADDRESS),
        "gas": 2000000,
        "gasPrice": w3.eth.gas_price
    })

    # Assinar a transação
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

    # Enviar a transação
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

    return tx_receipt

# Exemplo de uso
if __name__ == "__main__":
    # Parâmetros para o pool (exemplo com USDC/WETH, ajustar conforme necessário)
    TOKEN0 = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"  # USDC na Base
    TOKEN1 = "0x4200000000000000000000000000000000000006"  # WETH na Base
    FEE = 3000  # 0.3% fee tier
    TICK_LOWER = -887220  # Faixa de preço inferior
    TICK_UPPER = 887220   # Faixa de preço superior
    AMOUNT0_DESIRED = 1000000  # 1 USDC (6 decimais)
    AMOUNT1_DESIRED = 0        # 0 WETH (ajustar conforme proporção)
    AMOUNT0_MIN = 0
    AMOUNT1_MIN = 0
    RECIPIENT = WALLET_ADDRESS
    DEADLINE = int(w3.eth.get_block("latest")["timestamp"]) + 1200  # 20 minutos

    # Adicionar liquidez
    try:
        receipt = add_liquidity(
            TOKEN0,
            TOKEN1,
            FEE,
            TICK_LOWER,
            TICK_UPPER,
            AMOUNT0_DESIRED,
            AMOUNT1_DESIRED,
            AMOUNT0_MIN,
            AMOUNT1_MIN,
            RECIPIENT,
            DEADLINE
        )
        print(f"Transação bem-sucedida! Hash: {receipt.transactionHash.hex()}")
    except Exception as e:
        print(f"Erro: {e}")