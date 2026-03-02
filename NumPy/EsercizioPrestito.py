from __future__ import annotations
import re
from dataclasses import dataclass
from typing import Any,Dict,List,Optional,Tuple
import numpy as np

@dataclass
class CleanRecord:
    age: int
    income: float
    debts: int
    credit_score: int
    approved: int
#classe per parsing/sanificazione
class FieldParser:

    def parse_int(self, value: Any) -> Optional[int]:
        if value is None:
            return None
        if isinstance(value, str):
            txt = value.strip()
            if txt == "" or txt.lower() in {"n/a", "na", "??"}:
                return None
            txt = re.sub(r"[^\d\-]", "", txt)
            if txt == "" or txt == "-":
                return None
            try:
                return int(txt)
            except ValueError:
                return None
        if isinstance(value, (int, np.integer)):
            return int(value)
        return None

    def parse_income(self, value: Any) -> Optional[float]:
        if value is None:
            return None
        if isinstance(value, (int, float, np.integer, np.floating)):
            return float(value)
        if not isinstance(value, str):
            return None

        txt = value.strip().lower()
        if txt in {"", "n/a", "na", "??"}:
            return None

        k_match = re.fullmatch(r"(-?\d+)\s*k", txt)
        if k_match:
            return float(k_match.group(1)) * 1000.0

        txt = txt.replace("€", "").replace(" ", "").replace(".", "")
        try:
            return float(txt)
        except ValueError:
            return None

    def parse_approved(self, value: Any) -> Optional[int]:
        if value is None:
            return None
        if isinstance(value, (int, np.integer)):
            return int(value)
        if not isinstance(value, str):
            return None

        txt = value.strip().lower()
        if txt in {"1", "yes", "y", "si", "sì", "true"}:
            return 1
        if txt in {"0", "no", "n", "false"}:
            return 0
        return None
'''
#def parse_float(self,value,Any:)
def parse_income(self,value: Any) -> Optional[float]:
    if  value is None:
        return None
    if isinstance(value,int,float, np.integer,np.floating):
        income=float(value)
        return income
    if not isinstance(value,str):
        return None
    txt=value.strip().lower()
    if txt in {"","n/a","na","??"}:
        return None
    k_match=re.fullmatch(r"[(-+]\d+)\s*k",txt)
    if k_match:
        return float(k_match.group(1))*1000.0
    txt=txt.replace("€","").replace(" ","").replace(".","")
    try:
        return float(txt)
    except ValueError:
        return None
def parse_approved(self,value: Any) -> Optional[int]:
    if value is None:
        return None
    if isinstance(value,(int, np.integer)):
        return int(value)
    #return None
    if not isinstance(value,str):
        return None
    txt=value.strip().lower()
    if txt in {"1","yes","y","si","sì","true"}:
        return 1
    if txt in {"0","no","n","f","false"}:
        return 0
    return None
    '''
class RecordValidator:
    def is_valid(self,rec: CleanRecord) -> bool:
        if rec.age <18 or rec.age >99:
            return False
        if rec.income <=0:
            return False
        if rec.debts <0 or rec.debts >50:
            return False
        if rec.credit_score <0 or rec.credit_score > 850:
            return False
        if rec.approved not in (0,1):
            return False
        return True
class PreprocessingPipeline:
    def __init__(self,parser: FieldParser,validator: RecordValidator):
        self.parser = parser
        self.validator = validator
        self.dropped_records: int = 0
        self.kept_records: int = 0

    def clean_records(self, raw_records: List[Dict[str, Any]]) -> List[CleanRecord]:
        cleaned = []

        for record in raw_records:
            age = self.parser.parse_int(record.get("age"))
            income = self.parser.parse_income(record.get("income"))
            debts = self.parser.parse_int(record.get("debts"))
            credit_score = self.parser.parse_int(record.get("credit_score"))
            approved = self.parser.parse_approved(record.get("approved"))

            if None in (age, income, debts, credit_score, approved):
                self.dropped_records += 1
                continue

            rec = CleanRecord(age, income, debts, credit_score, approved)

            if not self.validator.is_valid(rec):
                self.dropped_records += 1
                continue

            cleaned.append(rec)
            self.kept_records += 1

        return cleaned
    def build_xy(self,cleaned:List[CleanRecord]) -> Tuple[np.array,np.array]:
        X=np.array([
            [r.age,r.income,r.debts,r.credit_score] for r in cleaned],
            dtype=float
        )
        y=np.array(
            [r.approved for r in cleaned],
        dtype=int
        )
        return X,y
    def add_feature_engineering(self, X: np.ndarray)-> np.ndarray:
        income= X[:,1]
        debts=X[:,2]
        debt_to_income= debts / income
        debt_to_income=debt_to_income.reshape(-1,1)
        X_enhanced = np.hstack((X,debt_to_income))
        return X_enhanced
    def minmax_normalize(self,X:np.ndarray)-> np.ndarray:
        min_col = np.min(X,axis=0)
        max_col = np.max(X,axis=0)
        denom=(max_col-min_col)
        denom[denom==0]=1.0
        X_norm=(X-min_col)/denom
        return X_norm

    def train_test_split(
            self,
            X: np.ndarray,
            y: np.ndarray,
            train_ratio: float = 0.8,
            seed: int = 42
    ):

        idx = np.arange(len(X))
        rng = np.random.default_rng(seed)
        rng.shuffle(idx)

        train_size = int(len(idx) * train_ratio)

        train_idx = idx[:train_size]
        test_idx = idx[train_size:]

        X_train = X[train_idx]
        X_test = X[test_idx]
        y_train = y[train_idx]
        y_test = y[test_idx]

        return X_train, X_test, y_train, y_test