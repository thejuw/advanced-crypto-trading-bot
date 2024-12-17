from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime

@dataclass
class Asset:
    symbol: str
    current_weight: float
    target_weight: float
    volatility: float
    correlation: Dict[str, float]
    constraints: Dict[str, float]
    cost: float
    current_price: float
    position_size: float
    last_update: datetime

@dataclass
class RebalanceResult:
    trades: List[Dict[str, float]]
    expected_risk: float
    expected_cost: float
    new_weights: Dict[str, float]
    timestamp: datetime