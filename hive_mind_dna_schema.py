import json
import requests

# REDACTED FOR GITHUB SECRECY
HIVE_ENDPOINT = "https://kvantix.tech/api/v1/hivemind/sync"
HIVE_SECRET = "REDACTED_API_KEY" 

def broadcast_trade_dna_to_swarm(asset, trade_metrics, profit_pct):
    """
    [PUBLIC SHOWCASE] 
    Constructs the 12-dimensional 'DNA String' of a closed trade and uploads it 
    to the Global Hive Mind for collective reinforcement learning.
    """
    
    # Constructing the X-Ray Payload Schema
    payload = {
        "secret_key": HIVE_SECRET,
        "asset": asset.upper(),
        "macro_risk": trade_metrics.get("macro_risk", 0.0),
        "smart_money": trade_metrics.get("smart_money_flow", 0.0),
        "trend_exhaustion": trade_metrics.get("exhaustion_index", 0.0),
        "temporal_consensus": trade_metrics.get("temporal_weight", 0.0),
        
        # DNA at exact moment of entry
        "dna_at_entry": trade_metrics.get("entry_dna", {}),
        
        # Trade Lifecycle Metrics
        "metrics": {
            "max_drawdown_pct": trade_metrics.get("max_drawdown", 0.0),
            "duration_seconds": trade_metrics.get("duration", 0),
            "market_regime": trade_metrics.get("regime", "neutral"),
            "obi": trade_metrics.get("orderbook_imbalance", 0.0),
            "bot_settings": {
                "sl": trade_metrics.get("stop_loss", -5.0),
                "tp": trade_metrics.get("take_profit", 10.0),
                "tsl": trade_metrics.get("trailing_stop", 1.5)
            }
        },
        "profit_pct": profit_pct
    }
    
    print(f"📦 [HIVE DEBUG] Payload constructed. DNA Strength: Risk({payload['macro_risk']}) / Flow({payload['smart_money']})")
    
    # Transmission (Simulated for showcase)
    # response = requests.post(HIVE_ENDPOINT, json=payload)
    return json.dumps(payload, indent=4)
