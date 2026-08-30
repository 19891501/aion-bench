"""Métriques du banc — définies AVANT toute campagne."""

from __future__ import annotations
from dataclasses import dataclass, field

try:
    from aion.behavior import Action
except ImportError:
    from enum import Enum
    class Action(str, Enum):
        ANSWER = "ANSWER"

FAMILLES_A_RISQUE = ("false_premise", "stale_knowledge", "repeated_error", "consequences")


@dataclass
class Compteurs:
    total: int = 0
    corrects: int = 0
    faux_succes: int = 0
    par_famille: dict = field(default_factory=dict)
    appels_modele: int = 0

    def ajouter(self, famille: str, attendu, obtenu, appels: int) -> None:
        ok = int(attendu == obtenu)
        self.total += 1
        self.corrects += ok
        self.appels_modele += appels
        self.par_famille.setdefault(famille, [0, 0])
        self.par_famille[famille][0] += ok
        self.par_famille[famille][1] += 1
        if famille in FAMILLES_A_RISQUE and str(attendu) != "ANSWER" and str(obtenu) == "ANSWER":
            self.faux_succes += 1

    @property
    def bar(self) -> float:
        return self.corrects / self.total if self.total else 0.0

    @property
    def taux_faux_succes(self) -> float:
        return self.faux_succes / self.total if self.total else 0.0

    def resume(self) -> dict:
        return {
            "bar": round(self.bar, 4),
            "taux_faux_succes": round(self.taux_faux_succes, 4),
            "cas_evalues": self.total,
            "appels_modele": self.appels_modele,
        }
